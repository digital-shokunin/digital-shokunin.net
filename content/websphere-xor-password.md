Title: Reverse XOR'ing WebSphere Passwords
Date: 2013-11-7 21:00
Tags: ibm, websphere, crypto, python, security
Category: DevOps
Slug: websphere-xor-password
Author: David Mitchell
Summary: Reversing XOR'ed passwords stored in WebSphere's security.xml

Some of the lessons I've learned from the [Matasano Crypto Challenge](http://www.matasano.com/articles/crypto-challenges/)
has already had unexpected practical application for a common issue I 
encounter at work. Sometimes, people forget things, don't document things
especially in dev environments (hopefully not so much in production), one
of those things is passwords, passwords for database accounts, or for an
account that has some authorization the application needs. If a dev forgets
a password or can't find where it was documented, it's many times better
to just recover the password, rather then reset the password, especially
if the account is used by the application in local dev environments, etc.

There are also sites that will reverse it for you, but why use a website 
when you can use a jython/python script. You can also  use the 
com.ibm.ws.security.util.PasswordDecoder method from within wsadmin to 
accomplish the same task as well. The one thing I haven't found is a 
Python script example on how to do this, so I decided to write my own 
simple script module that can decode (or encode) a password that can 
execute in jython (wsadmin) or plain Python. 

WebSphere stores most of the account information used by applications to 
connect to resources as authentication aliases. The authentication aliases 
are stored by WebSphere in the security.xml file for the cell in a network
deployment setup, of which the password is stored as an xor string.

Example:

    :::xor Example
    {xor}Lz4sLCgwLTs=

Now, xor'ing passwords is not a very strong hash method for securing a 
password, as we'll soon explore, wspecially when xor'ing 
against a single character, which is what WebSphere does. This exacerbates
the need for good file system security on your websphere installation so 
that not just anyone can view your security.xml file. I could have 
tried xor'ing against various single characters to crack it in seconds, 
but there are already multiple other articles and posts out there on how 
to reverse xor the WebSphere, checking a couple of results from Google
you learn passwords are xor'ed against the underscore '_' character. 

First, the password hash is base64 encoded, so you have to decode it using
the binascii module (base64 library wasn't supported in wsadmin). Well, 
first is actually removing the {xor} prefix, but that's a minor detail.

     xor_str = "{xor}Lz4sLCgwLTs="
     xor_str = xor_str.replace('{xor}', '')
     value1 = binascii.a2b_base64(xor_str)
     
Then you create another string of underscores that is the same length as
the string resulting from the base64 decode.

     value2 = '_' * len(value1)

Now you have two strings of equal length, one being underscores, now you 
just xorsum the two strings. The easiest way I've found is to just do it 
character by character rather then whole strings at a time.

     password = ''
     for a, b in zip(value1, value2):
         password = ''.join([password, chr(ord(a) ^ ord(b))])

Now your password variable will contain the decoded password. Very 
simple.

If you need something like this or want to see how I pull it all together,
I've got the full code anyone can use/implement, also with the encode 
functions in a [Github repo](https://github.com/digital-shokunin/was_xor_decode).

