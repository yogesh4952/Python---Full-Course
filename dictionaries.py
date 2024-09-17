#Dictionaries -> just like structure in C, Accesing , updating putting vallues are same as c

# person = {

# "name":"Yogesh Shah",
# "age":17,
# "gender":"Male",
# "is_csit_student":True
# }

# person["name"]=  'Yuvraj Shah'
# print(person.get("name"))

# person["birth_date"] = "20 dec 2006"
# print(person["birth_date"]);

# print(person["is_csit_student"])
# if (person["is_csit_student"]):
#     print("Eligible");
# else:
#     print("Not eligible")


# Mapping 

number = input('Phone number: ');

digits_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
} 

output = ''
for ch in number:
    output += digits_mapping.get(ch,"!") + " ";

print(output)
