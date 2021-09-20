# String
## Slicing and Indexing

mystr='university'
print(mystr[3],mystr[-7],mystr[7],mystr[-3])
print(mystr,len(mystr),type(mystr),id(mystr))
print(mystr[1],mystr[-9])
print(mystr[3:6])
print(mystr[::2],mystr[1::2],mystr[::-1])
print(mystr[6:])


mysaa='saGarGupTA'
print(mysaa,len(mysaa),type(mysaa),id(mysaa))
print(mysaa.upper())
print(mysaa.lower())
print(mysaa.capitalize())
print(mysaa.title())
print(mysaa.swapcase())


mystr="sagarabcde"
print(mystr,mystr.isalpha(), mystr.isalnum(),mystr.isdigit())
mystr='15234'
print(mystr,mystr.isalpha(), mystr.isalnum(),mystr.isdigit())
mystr='abdgjd#@@#$123456'
print(mystr,mystr.isalpha(), mystr.isalnum(),mystr.isdigit())


mystr='university'
print(mystr.find('k'))




# List

## Join convert list to a character
list1=['charity', 'should', 'begin', 'at', 'home']
print(list1,type(list1))
mystr="- ".join(list1)
print(mystr,type(mystr))



### Dealing with the List
#List is mutable
list=[100,2,3,2,4,2]
print(list,len(list),type(list))
print(max(list),min(list))
print(sum(list),sum(list)/len(list))

###   ADDING CHARCTER INTO THE LIST

list4=['mmanjari','hindi','urdu']
print(list4,len(list4))
list4.append("golden")
list4.append('kalu')
print(list4,len(list4))
list4.insert(1,'sagar')
print(list4)


### REMOVE METHOD
list4=['mmanjari','hindi','urdu']
print(list4)
list4.remove('urdu')
print(list4)
del list4[1]
print(list4)
