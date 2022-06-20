import json

masterAllShabads={}

def getUniqueShabadsFromFiles(file):
    with open(file,encoding="utf-8") as f:
        data=json.load(f)
        for i in data:
            if i not in masterAllShabads:
                masterAllShabads[i]=data[i]
getUniqueShabadsFromFiles("./allShabads.json")
getUniqueShabadsFromFiles("./NoRepeatsAllShabads.json")
getUniqueShabadsFromFiles("./2NoRepeatsAllShabads.json")
print(len(masterAllShabads))

fw=open("MasterALLShabads.json",'w',encoding='utf-8')
fw.write("{\n")
for i in masterAllShabads:
    val=masterAllShabads[i].replace("\"","\'").replace("\n","\\n")
    fw.write(f'"{i}" : "{val}",\n') 
fw.write("\n}")
fw.close()

# fw=open("lessData.json",'w',encoding="utf-8")
