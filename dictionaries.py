developer_experience = {
"Sunil":1.5,
"Keshav":2,
"Kristal":3
}

#to extract value in dictionaries
#print("experience of Kristal as a developer "+ developer_experience["Keshav"])
# print("experience of Sunil as a developer " + str(developer_experience.get("Sunil")))

#developer_experience.clear()

#to copy the dictionaries
# software_engineer_experience = dict(developer_experience)
# software_engineer_experience = developer_experience.copy()
# print(software_engineer_experience)

#loop
for x,y in developer_experience.items() :
    print (x,y)

for x in developer_experience :
    print (x)

for x in developer_experience :
    print (developer_experience[x])

for x in developer_experience.values() :
    print (x)

# check if key exist
if "Sunil" in developer_experience:
    print(developer_experience["Sunil"])

#length of dictionaries
print(len(developer_experience))

#adding data in dictionaries
developer_experience["Nitesh"]=3

print(developer_experience)

#del the key from dictionaries
developer_experience.pop("Sunil")
print(developer_experience)

del developer_experience["Nitesh"]
print(developer_experience)

#del the last key
developer_experience.popitem()
print(developer_experience)

project_manager= dict(Name="Surendra")
print(project_manager)

Software_Company ={
    'developers' : developer_experience,
    'project_manager' : project_manager
}

print(Software_Company)