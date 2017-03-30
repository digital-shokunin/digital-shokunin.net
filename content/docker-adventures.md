Title: Adventures with Docker
Date: 2014-11-02 21:00
Tags: devops, linux 
Slug: docker-adventures
Category: DevOps
Author: David Mitchell
Summary: Playing with docker, and fun uses for docker

I've completely messed up my Docker install on the server I was using it 
on so take my post with a grain of salt. I've been messing with Docker
for over a year and found it advantageous for a lot of situations. The 
main thing a Docker container or LXC containers provide me in general, 
is a sandbox within which to experiment that doesn't require running a 
full virtual machine, an extra server, or modifying the native OS settings
to try out various applications, packages, or have a self contained 
environment for using certain software so I can keep it isolated from
my base or default environment. One obvious application is doing development.

I've also been using it to play some with Ansible and Salt. Deploying to 
containers rather than having to setup servers.

Currently, I get errors or my server freezes when doing a build.
If anyone knows how to fix the errors below I would love to know.

     
     Error pulling image (trusty) from ubuntu, Driver devicemapper failed to get image rootfs
     Error mounting '/dev/mapper/docker/...
      on '/var/lib/docker/devicemapper/mnt/5f18d94c3eca21bc3212ab66ed7aad11dccf9d4b4128401deae2b0c0c1286132': invalid argument 41
      
Update: Freezing issue is a [known issue](https://github.com/docker/docker/issues/7395) on Arch on Digital Ocean as well as the [devmapper error](https://github.com/docker/docker/issues/4036).
