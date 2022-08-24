def readMont(file):
    f = open(file, 'r')
    content = f.readlines()

    sex = content[0].replace("Patient's Sex: ","").replace(" \n","")
    age = content[1].replace("Patient's Age: ","").replace("Y\n","")
    age = int(age)
    cond = content[2].replace("\n","")

    f.close()
    
    return sex, age, cond


def readShenzhen(file):
    f = open(file, 'r')
    content = f.readlines()
        
    sex = content[0].split()[0]
    age = content[0].split()[1].replace("yrs","")
    age = age.replace("yr","")
    
    if "month" in age:
        age = age.replace("month", "")
        age = round(float(age) / 12)
        
    age = int(age)
    cond = content[1].replace("\n","")
    
    if cond == "":
        cond = content[2].replace("\n","")
        
    f.close()
    
    return sex, age, cond