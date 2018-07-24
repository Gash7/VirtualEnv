#With Statement
with open('D:\python\Ashish1.txt') as file:
 data = file.readlines()
print(data)

print('------------------------------')
#Read a text file  in Python
file =open('D:\python\Ashish1.txt')#python Default operation is read mode
for line in file:
    print(line)#Looping over a file object
print (file.readlines())
print('readline' ,file.readline(3))#Readline No- 1
print('Ashish1-----', file.read())#Default Read All file
print('Ashish1-----1', file.read(30))#This read only 30 characters fron the file



#Create a text file
file = open('D:\Python\Ashish1.txt','w')

file.write('Hello World\n')
file.write('This is our new text file\n')
file.write('and this is another line\n')
file.write('Why? Because we can\n')
file.close()

#Open a text file
file = open('D:\Python\Ashish.txt','r')
#file_object  = open(“filename”, “mode”)
print(file)
print(file.readlines())
file.close()#for Closing of File
