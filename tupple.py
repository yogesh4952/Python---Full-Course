# # Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# co_ordindate = (1,2,4);


# #convert tupple into list and vice-versa
# thistuple = ("apple","banana","cherry");
# x = list(thistuple)
# x.append("mango")
# x =tuple(x)
# # print(x)

# #We can allowed to ad tupples into tupple

# fruits = ("apple","banana")
# y = ("orange",)
# fruits = fruits+ y;
# print(fruits)


##-------------------------------------------------------


# #Remove Tupple ->> we cannot remove tupple so convert into list and remove

# lamo = (1,2,3);
# x= list(lamo)
# x.remove(1);
# lamo = tuple(x)
# print(lamo)

# del lamo;


##-------------------------------------------------------



#Unpacking tupple

# fruits = ("apple","banana","Orange")
# green,yello,red = fruits;
# print(green)
# print(yello)
# print(red)


##-------------------------------------------------------
#Using asterisk
#if the number of variable is less than number of values, we can add aestrick to the variable and remaining values are added as a list


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# red,yello,*green=fruits
# red,*yello,green=fruits


#output: ['cherry', 'strawberry', 'raspberry']
# print(green)




##-------------------------------------------------------




#Loop through tuple

# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)

#looping using indexes

# for x in range(len(thistuple)):
    # print(thistuple[x])

#using while loop

# i =  0; 
# while i<len(thistuple):
#     print(thistuple[i])
#     i = i+1;




#-------------------------------------------------------


#Join Tuples

# tuple1 = ("a","b","c");
# tuple2 = (1,2,3);
# tuple3 = tuple1 + tuple2;
# multiply = tuple1*4;
# print(multiply)
#output:('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
# print(tuple3)



#-------------------------------------------------------
# tuple methods


# 1 = count()==>returns number of times a specified values ocuurs in a tuple
tuple1 = (1,1,11,1,3,3,33,3,2,1);
print(tuple1.count(1));


# w = index()==> searches the tuple for a specified value and returns the position of whe it was found

print(tuple1.index(11))