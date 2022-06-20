import requests
import json

def putALlDataInfile(lst):
    with open('json_data.json', 'w',encoding="utf-8") as outfile:
        outfile.write("{")
        for i in range(len(lst)):
            res=requests.get(lst[i])
            ans=f"{i+1}:{res.text},\n"
            outfile.write(ans)
            print(f"Done with Ang {i+1}!!!")
        outfile.write("}")
        # fl.write(json.dumps(res.text,sort_keys=True, indent=4))
    # fl.close()

#the lines below will get all info of angs from gurbaninow api
# mainUrl="https://api.gurbaninow.com/v2/ang/"
# allAngsUrl=[mainUrl+str(i) for i in range(1,1431)]
# putALlDataInfile(allAngsUrl)

def getLessData():
    with open("json_data.json",encoding="utf-8") as f:
        data=json.load(f)
    fw=open("lessData.json",'w',encoding="utf-8")
    fw.write("{")
    for i in data:
        angInfo=data[i]["page"]
        theDataWeWant=[i["line"]["larivaar"] for i in angInfo]
        fw.write(f'"{i}":{theDataWeWant},\n')
        print(f"Done With ang {i}!!!")
    fw.write("}")
    fw.close()
"""
This function above gets all the data generated from
the comanads above. The json file generated was like
100 mb and had data that is not needed so this function
just gets all the data we want and puts in a file.
""" 
# getLessData()

def averageLines():
    with open("lessData.json",encoding="utf-8") as f:
        data=json.load(f)
    lenOfAngs=[len(data[i]) for i in data]
    avg=sum(lenOfAngs)/len(lenOfAngs)
    print(avg)
# averageLines()

def putInTxtFile():
    with open("lessData.json",encoding="utf-8") as f:
        data=json.load(f)
    fw=open("SGGSJi.txt",'w',encoding='utf-8')
    for i in data:
        fw.write(f"\n\nAng {i}\n\n")
        for j in data[i]:
            fw.write(f"{j['unicode']}\n")
    fw.close()
putInTxtFile()