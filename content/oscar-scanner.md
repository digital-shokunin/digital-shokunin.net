Title: Oscar scanner 
Date: 2014-01-05 21:00
Tags: python 
Slug: grocery-scanner
Category: Code
Author: David Mitchell
Summary: Barcode scanner that automatically populates your grocery list on your phone and other interesting discoveries

[Oscar][oscar] is a Python project utilizing the Raspberry Pi w/ UPC barcode reader 
to scan barcodes on items you keep stocked in your pantry or fridge, when 
scanned, ideally when you run out of an item just before throwing the packaging
or container away, it will populate your grocery list with the item reminding 
you that you need to pick up more of that item on your next shopping trip. 
Since it's written in Python, it could easily be adapted to run on almost 
any device with Linux on it and a USB port that is networked. I've been 
working on a [fork of it][oscar-fork] for Python3/Arch and using the 
[miniature UPC reader from Adafruit][upc-scanner].

My work on the [GTK indicator][GTK-indicator] has kind of stalled, I've 
lost interest but I might pick it up later if I'm ever motivated to work 
out the kinks in it.

[oscar]: https://github.com/danslimmon/oscar
[oscar-fork]: https://github.com/digital-shokunin/oscar/tree/python3
[upc-scanner]: https://www.adafruit.com/products/1203
[GTK-indicator]: http://digital-shokunin.net/indicator-project.html




