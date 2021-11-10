import re
import time
t_start = time.perf_counter()

f = open("FileType/ICT.Laba4.json")
js = f.read()
f.close()
xml = open("readyFiles/XmlRegexBeLike.xml", "w")

alles = re.findall(r'.*',js)
alicey = ""
for i in alles:
    alicey+=i
js = eval(alicey)



def FromJsonToXml(json, separator=""):
    answer = list()  # Our final list
    codeType = type(json)  # Our code can be dictionary { "..." : ... or list {"...","..."} => different situations
    if codeType is list:
        for i in json:  # for any element in our list:
            answer.append(FromJsonToXml(i,separator))  # + 1 formed element to answer
        return "\n".join(answer)
    if codeType is dict:
        for tag in json:
            ijson = json[tag]
            answer.append("%s<%s>" % (separator,tag))
            answer.append(FromJsonToXml(ijson,"\t"+separator))
            answer.append("%s<%s/>" % (separator, tag))
        return "\n".join(answer)
    return "%s%s" % (separator,json)
xml.write(FromJsonToXml(js))
print("Время работы: %s секунд " % (time.perf_counter() - t_start))

