import json
from itertools import permutations
import base64
import requests
import validators
# Get response from request
res = {
    "instructions": "Impressive! Kudos to you that you are in this step. With this response, you have a stringified array of strings as part of urlObject property. As part of this step you need to find the actual URL from the urlObject. \n             Now you must be wondering how you will find that? We will now tell you how we actually created this urlObject so that you can do reverse engineering to get it back. On the very first step, we encoded the actual URL using base64 encoding. Then we split the base64 encoded URL for every 50 characters \n             to get an array of strings. Then we have randomly shuffled the array so the orders become random. Then we have stringified the array of strings and sent you as part of urlObject property.\n             Now please try to find out the correct URL. Don't try to find it manually and rather write a code in your favorite language to find it easily. \n             Once you have found the correct URL, paste it into a browser and from there you will get the next instruction :-)\n             All the best!",
    "urlObject": "[\"b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW\",\"50cnkuMTAxMzkwOTE1PVdoMXNERXh3a21kbXNhSXgtcWVsYWh5\",\"lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS\",\"JTQwZ21haWwuY29tLXE5ZzJMZU1QYnF5Z0tMbjEmZW50cnkuMT\",\"aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU\",\"k1NDA1MDMwND1xZWxhaHlAZ21haWwuY29t\"]"
}
# response is already in dictionary format
url = res["urlObject"]
newURL = ["b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW" , "50cnkuMTAxMzkwOTE1PVdoMXNERXh3a21kbXNhSXgtcWVsYWh5" ,  "lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS" , "JTQwZ21haWwuY29tLXE5ZzJMZU1QYnF5Z0tMbjEmZW50cnkuMT" , "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU" , "k1NDA1MDMwND1xZWxhaHlAZ21haWwuY29t"]

p = list(permutations(newURL))
arr = []
for i in p:
    a = ""
    for j in i:
        a += j
    link = base64.b64decode(a)
    if validators.url(link):
        response = requests.get(link)
        arr.append(response)

print(arr)