This program can successfully extract the product details of any laptop available in amazon.in website.

The code is written in python using the BeautifulSoup module.

I created this program to scrap out product details of laptops for my amazon affiliate blog.

The program uses BeautifulSoup, you have to save the product page in your computer and then provide that file path to the program.
The BeautifulSoup will then parse the given file and extract the product specifications.

I did not use the urllib module to directly parse the webpage using the link, because amazon servers sometime disallows the automated request to servers.

This program does the all automation work of extracting product specification of a laptop page and creates a test file with html table of specifications for me.

When you run this program, It will ask you 4 inputs:

1. Provide a image affiliate link of the product
2. Provide a text link for button
3. file path, where the html page of that product page you have saved.
4. the name of output file you want.

Output Of the program:

Output of the program will be a text file.
