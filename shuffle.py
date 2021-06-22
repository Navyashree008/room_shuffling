import random
import json
room_number = [1,2,3,4,5,6,7,8,9,10]

with open("student information.json","r")as f:#opening json file to get information
    info = json.load(f)

name_list = []# to shuffele room on basis of name
for i in range(len(info['user'])):
    name_list.append(info['user'][i]['name'])

shuffled_list = [] # to store suffled information

for val in info.values():# list students information
    a = val

upper_girls = []
down_girls = []
for i in range(len(info['user'])):
    if info['user'][i]['position'] == "upper":
        upper_girls.append(info['user'][i]['name'])
    else:
        down_girls.append(info['user'][i]['name'])

name2 = []
while len(name_list) > 0:
    name = []
    for j in range(5):
        if len(upper_girls)>0:
            r_name = random.choice(upper_girls)
            upper_girls.remove(r_name)
            name_list.remove(r_name)
            name.append(r_name)
    for k in range(5):
        if len(down_girls)>0:
            r_name = random.choice(down_girls)
            down_girls.remove(r_name)
            name_list.remove(r_name)
            name.append(r_name)
    
    name2.append(name)

shuffled_list = []
count=0
i = 1
for j in name2:
    even_beds = [2,4,6,8,10]
    odd_beds = [1,3,5,7,9]
    for k in j:
        dict_of_bed_no = {}
        dict_of_bed_no['name'] = k
        print(i,"ye i hain")
        dict_of_bed_no['room_number'] = i
        for m in a:
            if m["name"] == k:
                if m["position"] == "upper":
                    if len(odd_beds)>0:
                        num = random.choice(odd_beds)
                        odd_beds.remove(num)
                        dict_of_bed_no['bed_no'] = num
                        dict_of_bed_no['position'] = "down"
                elif m["position"] == "down":
                    if len(even_beds)>0:
                        num = random.choice(even_beds)
                        even_beds.remove(num)
                        dict_of_bed_no['bed_no'] = num
                        dict_of_bed_no['position'] = "upper"
        shuffled_list.append(dict_of_bed_no) 
        count+=1
    i+=1

with open("reShuffle info.json","w")as f:
    json.dump(shuffled_list,f,indent=4)



