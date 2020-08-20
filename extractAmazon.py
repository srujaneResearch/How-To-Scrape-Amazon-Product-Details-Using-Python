#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 12:50:05 2020

@author: soul
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-



from bs4 import BeautifulSoup as bs
import re
import os


im = input("Enter Affiliate Image Link\n")

al = input("Enter Affiliate link for button\n")

productfile = input("Enter Product File path\n")

filename=input("Enter File NAme\n")

pathdestination = os.path.join(os.environ["HOME"],"Desktop",filename+".txt")

with open(productfile) as web:

    soup = bs(web,'html.parser')


#soup = bs(html,'html.parser')

#print(soup)


tags = soup.find_all('div', style="overflow:hidden;")

tb = tags[0].find_all('table')

table = tb[0]

det = {}
data = {"Os":{},"HDD":{},"Ram":{},"GC":{},"Dp":{},"Product":{},"Battery":{}}

for i in table.tbody.contents:
    if i == '\n':
        pass
    else:

        tg = i.contents
        if re.search(r"screen|Resolution|Screen Size", tg[0].string):
            #print(i.th.string.strip())
            #data["HDD"] = {}
            data["Dp"].update({tg[0].string.strip() : tg[1].string.strip()})
        elif re.search(r"Brand|Series|Colour|model|Model Name|Operating system", tg[0].string.strip()):
            data["Product"].update({tg[0].string.strip() : tg[1].string.strip()})

        elif re.search(r"Processor",tg[0].string):
            #print(i.th.string.strip())
            #print(i.td.string.strip())
            det[tg[0].string.strip()] = tg[1].string.strip()

            #details[i.th.string] = i.td.string

        elif re.search(r"Operating System",tg[0].string.strip()):

            #print(i.th.string.strip())
            #print(i.td.string.strip())
            #data["Os"] = {}
            data["Os"][tg[0].string.strip()] = tg[1].string.strip()

        elif re.search(r"RAM|Memory", tg[0].string.strip()):
            #data["Ram"] = {}
            data["Ram"].update({tg[0].string.strip(): tg[1].string.strip()})

        elif re.search(r"Hard", tg[0].string.strip()):
            #data["HDD"] = {}
            data["HDD"].update({tg[0].string.strip() : tg[1].string.strip()})
        elif re.search(r"Graphics", tg[0].string.strip()):
            #data["HDD"] = {}
            data["GC"].update({tg[0].string.strip() : tg[1].string.strip()})
        elif re.search(r"Battery",tg[0].string.strip()):
            data["Battery"].update({tg[0].string.strip() : tg[1].string.strip()})





    #print(type(i))

with open(pathdestination,"w") as file:

    if "Series" in data["Product"].keys():
        model = "Series"
    elif "Model Name" in data["Product"].keys():
        model = "Model Name"
    else:
        model = "Item model number"

    file.write("<h1>"+data["Product"]["Brand"]+" "+data["Product"][model]+"</h1>\n")
    file.write("<div><br /></div>\n")

    file.write(im)
    file.write("<div><br /></div>\n")
    file.write("<h5>Product Specifications</h5>\n")
    file.write("<table>\n")

    for i in data["Product"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["Product"][i]+"</td>\n")
        file.write("</tr>\n")
    file.write("</table>\n")
    file.write("<div><br /></div>\n")
    file.write("<h5>Operating System specification</h5>\n")
    file.write("<table>\n")

    for i in data["Os"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["Os"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")

    file.write("<h5>Display Technology</h5>\n")
    file.write("<div><br /></div>\n")
    file.write("<table>\n")

    for i in data["Dp"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["Dp"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")
    file.write("<h5>Processor Details</h5>\n")
    file.write("<div><br /></div>\n")
    file.write("<table>\n")

    for i in det.keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+det[i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")
    file.write("<h5>RAM Specifications</h5>\n")
    file.write("<div><br /></div>\n")
    file.write("<table>\n")

    for i in data["Ram"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["Ram"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")
    file.write("<h5>Hard Disk Specifications</h5>\n")
    file.write("<div><br /></div>\n")

    file.write("<table>\n")

    for i in data["HDD"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["HDD"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")
    file.write("<h5>Graphics Card</h5>\n")
    file.write("<div><br /></div>\n")
    file.write("<table>\n")

    for i in data["GC"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["GC"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")
    file.write("<div><br /></div>\n")
    file.write("<h5>Battery Specifications</h5>\n")

    file.write("<table>\n")

    for i in data["Battery"].keys():
        file.write("<tr>\n")
        file.write("<th>"+str(i)+"</th>\n")
        file.write("<td>"+data["Battery"][i]+"</td>\n")
        file.write("</tr>\n")

    file.write("</table>")

    file.write("<a class=\"clickb\" href=\""+al+"\">Buy At Amazon</a>\n")
    file.write("<div><br /></div>")
print("Your file is saved At:\n",pathdestination)   
