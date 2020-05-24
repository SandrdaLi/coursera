
#!/usr/bin/python3

import os
import requests
import json

path = "/home/student-04-8509cc2bbce2/supplier-data/descriptions/"
dirs = os.listdir( path )


for item in dirs:
    temp={}
    name = ['name', 'weight', 'description']
    i = 0
    with open(path+item) as f :
        lines = f.readlines()
    for i in range(len(name)):
        temp[name[i]]=lines[i].rstrip("\n")
    temp['weight']=temp['weight'].replace(" lbs","")
    temp['image_name']=item.replace("txt","jpeg")

    print(temp)
    data=json.dumps(temp)
    headers = {'Content-type': 'application/json'}
    response = requests.post("http://34.72.235.182/fruits/", data=data,headers=headers)
    print("status_code "+ str(response.status_code))

