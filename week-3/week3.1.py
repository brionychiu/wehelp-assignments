import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
info=data["result"]["results"]

with open ("data.csv" , "w" , encoding="utf-8") as file:
    for i in info:
        addr=i["address"][5:8]
        i["file"]=i["file"].replace("JPG","jpg")
        files=i["file"].split('jpg',maxsplit=1)
        file.write(i["stitle"]+","+addr+","+i["longitude"]+","+i["latitude"]+","+files[0]+"jpg"+"\n") 
    