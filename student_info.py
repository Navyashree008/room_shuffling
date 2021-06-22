import json
list = []
def student_information():
    # list = []
    info = {}
    name = input("enter your full name:-")
    room_number = int(input("enter your room number:-"))
    bed_number = int(input("enter your bed number:-"))
    

    info['name'] = name
    info['room_number'] = room_number
    info['bed_number'] = bed_number
    if bed_number % 2 == 0:
        info['position'] = "upper" 
    else:
        info['position'] = "down"
    
    with open("student information.json","r") as f:
        info_dict = json.load(f)

    info_dict['user'].append(info)
    with open("student information.json","w") as f:
        json.dump(info_dict,f,indent= 3)
    
student_information()