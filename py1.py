str1 = "Ifratul Islam Rian"
str2 = "Tamanna Sarah"
print(str1 + " " + str2)
#this is slicing for slice a specific part
print(str1[3:14])
print(str1[:14]) #print(str1[0:14])
print(str1[3:]) #print(str1[3:len(str1)])
print(str2.count("a")) #also we can write print(str2.count("anna"))


age = 25
if(age>18):
    print("can drink")
    print("can drive")
elif(age<5):
    print("Ahh shitt!! It's a child!!")
else:
    print("get out")


marks = [94.5, 87, 34, 93, 68, 97]
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)
marks.insert(5, 81)
print(marks)
marks.append(77) #add at the end
print(marks)
marks.remove(34) #remove the first occurance
print(marks)
marks.pop(4) #remove the value based on idx
print(marks) 


info = {
    "name" : "Ifratul Islam Rian",
    "CGPA" : 3.94,
    "Marks" : [85, 83, 79, 94],
    "age" : 20
}
print(type(info))
print(info)
print(info["name"])
print(info["CGPA"])
print(info["Marks"])
print(info["age"])
info["Degree"] = "B.Sc."
print(info["Degree"])
#nested dictionary
info["Marks"] = {
    "Eng. Math" : 85,
    "BNS" : 79,
    "Algorithm" : 94,
    "Discrete Math" : 83
}
print(info)
#dictionary methods
print(info.keys())
print(info.values())
print(info.items())
print(info.get("CGPA"))

#set
collection = {1,2,3,4}
print(collection)
print(type(collection))

collection.add(5)
print(collection)

collection.remove(1)
print(collection)

collection.pop() #rendomly pick and pop
print(collection)

collection.clear()
print(collection)

#Loop
i=0
while i<5:
    print("Sarah")
    i+=1
name = []
for j in range(5):
    # print("Sarah")
    name.append("Sarah")
l=0
for k in name:
    l+=1
    print(f"Case {l}: "+k)


#Fuction
def print143():
    print("I Love You Sarah apu")
    print("Sarah apu is best")
    print("Her birthday is in 28th August")
    print("She was HSC batch 22")

for i in range(10):
    print143()
