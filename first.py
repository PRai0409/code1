#PROGRAM 1

print("PROGRAM 1")
fname =input("Enter any filename :")
print("Output :")
op=fname.split(".")
#print(type(op))
print("filename : ",op[0])
print("extension : ",op[1])

#PROGRAM 2
print("\nPROGRAM 2")
fnum = int(input("Enter first number :"))
#print(type(fnum))
snum = int(input("Enter second number :"))
total=sum([fnum,snum])
print("Sum of numbers :",total)

#PROGRAM 3
print("\nPROGRAM 3")
alist=[10,20,30,10,35,20,67,89,20,10]
print("Unique list:",list(set(alist)))

#PROGRAM 4
print("\nPROGRAM 4")
fname =input("Enter the string : ")
#1.uppercase 2.count of p 3.replace python to ruby 4.count number of words 
#5. count number of char 6.remove spaces --Python is general purpose interpreted cross platform programming language--
print("Uppercase:",fname.upper())
print("Count of p:",fname.count("p"))
print("Replace:",fname.replace("Python","Perl"))
print("Number of words:",len(fname.split(" ")))
print("Number of characters:",len(fname))
print("Removed spaces",fname.strip())

#PROGRAM 5
print("\nPROGRAM 5")
alist=list()
alist.append(10)
alist.append(20)
alist.append(50)
alist.extend([90,20,45,32,645,32,90,65,43,23,55,4,32,50])
print("First list:",alist)
blist=list(set(alist))
print("Unique list:",blist)
blist.remove(50)
blist.sort(reverse=True)
print("Desc sort:",blist)
print("Tuple",tuple(blist))

'''
----------------------OUTPUT--------------------
PROGRAM 1

Enter any filename :hello.py
Output :
filename :  hello
extension :  py

PROGRAM 2

Enter first number :78

Enter second number :87
Sum of numbers : 165

PROGRAM 3
Unique list: [67, 35, 10, 20, 89, 30]

PROGRAM 4

Enter the string : Python is general purpose interpreted cross platform programming language
Uppercase: PYTHON IS GENERAL PURPOSE INTERPRETED CROSS PLATFORM PROGRAMMING LANGUAGE
Count of p: 5
Replace: Perl is general purpose interpreted cross platform programming language
Number of words: 9
Number of characters: 73
Removed spaces Python is general purpose interpreted cross platform programming language

PROGRAM 5
First list: [10, 20, 50, 90, 20, 45, 32, 645, 32, 90, 65, 43, 23, 55, 4, 32, 50]
Unique list: [32, 65, 4, 645, 10, 43, 45, 50, 20, 55, 23, 90]
Desc sort: [645, 90, 65, 55, 45, 43, 32, 23, 20, 10, 4]
Tuple (645, 90, 65, 55, 45, 43, 32, 23, 20, 10, 4)
'''