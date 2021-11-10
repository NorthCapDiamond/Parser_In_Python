from  json2xml import json2xml

import time
t_start = time.perf_counter()

f = open("FileType/ICT.Laba4.json")
js = eval(f.read())
f.close()
xml = open("readyFiles/Library2Xml.xml", "w")
xml.write(json2xml.Json2xml(js).to_xml())

print("Время работы: %s секунд " % (time.perf_counter() - t_start))


