# sets => are used to store multiple items in a single variable
#      => unordered unchangble and unindexable
#      => can remove and add items
#      => duplicates cannot allowed

# thisset = {1,1,2,3};
# print(thisset)


# NOTE => The values True and 1 are treated as same
# NOTE => The values False and 0 are treated as same

# thisset = {"apple", "banana", "cherry"}
# print("banana" not in thisset)#False



#-----------------------------------------------------------------------------------



#adding items in the set using set property
# thisset = {1,2,3};
# thisset.add(5);
# print(thisset)

#to add items in a set from the another set we use update()
# thisset = {1,2,3,4}
# thisset1 = {"apple","banana"}#it might be tuple ,dictionaries , list
# thisset.update(thisset1);
# print(thisset)



#-----------------------------------------------------------------------------------


#remove -> use remove or discard();

# thisset = {1,2,3,4}
# thisset1 = {"apple","banana"}#it might be tuple ,dictionaries , list
# thisset1.remove("apple");


# thisset1.clear();
# print(thisset1)



#-----------------------------------------------------------------------------------


#Join sets

thisset1 = {1,2,3,4};
thisset2 = {4,5,6,7};
result  =thisset1.union(thisset2) # result = thisset1 | thisset2
result  = thisset1.intersection(thisset2)# result = thisset1 & thisset2
result =thisset1.difference(thisset2)# result = thisset1 - thisset2
# print(result) 

#difference_update()->change the original ser
# thisset1.difference_update(thisset2)
# print(thisset1)

#symmetric_difference => keep the value which are not in both set
# set3 = thisset1.symmetric_difference(thisset2)# set3 = thisset1 ^ thisset2;
# print(set3)


#symmetric_difference_update() ==> did the same but change the original set
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.symmetric_difference_update(set2)
# print(set1)


