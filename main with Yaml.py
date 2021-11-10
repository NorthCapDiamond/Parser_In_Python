import time
t_start = time.perf_counter()

f = open("FileType/ICT.Laba4.json")
js = (f.read())
f.close()
yaml = open("readyFiles/YamlBeLike.yaml", "w")


def toYaml(json):
    json = json.replace("{","")
    json = json.replace("}","")
    json = json.replace('"',"")
    Yaml = json.replace(",","")
    return Yaml

yaml.write(toYaml(js))
print("Время работы: %s секунд " % (time.perf_counter() - t_start))