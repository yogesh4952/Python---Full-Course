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

# number = input('Phone number: ');

# digits_mapping = {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# } 

# output = ''
# for ch in number:
#     output += digits_mapping.get(ch,"!") + " ";

# print(output)



#-------------------------------------------------------------------------
#key()=> return all keys

# digits_mapping = {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# } 

# x  = digits_mapping.keys();
# print(x);

# #values()->return all the values
# y =digits_mapping.values();
# print(y)
# digits_mapping['year']="20 dec"
# print(y)

# z=digits_mapping.items();
# print(z) # print all the key-values pairs

# if "1" in digits_mapping:
#     print("Yes it exist")

#update()=> update the value

# digits_mapping.update({"1":"two"})
# print(digits_mapping)


#Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }

}
print(myfamily.items())
for x, obj in myfamily.items():
    for y in obj:
        print(obj[y])