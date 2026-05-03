#writing data in text file
a=open("D:/demo/myfile.txt","w")               #writing mode
a.write("this is myfile \n")
a.write("my name is usha")
a.close()
print("program completed")

#read data in text file
b=open("D:/demo/myfile.txt",'r')
print(b.read())
print(b.readline())
print(b.readlines())
#only first line is printed
b.close()

#append new line
b=open("D:/demo/myfile.txt",'a')
b.write("\nmy surname is nazare")
b.close()