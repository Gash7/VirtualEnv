from BankAssignment.ProductCatrgory.Product import*
file = open(r'C:\Users\AMIT_GORE\Desktop\Ashish.txt')
flag = False
listofBussinessProductFromFile =[]
listofHomeuseProductFromFile =[]
listofCommercialProductFromFile =[]

for line in file.readlines():
    if flag:
        print(line.rstrip('\n'))
        words = line.split(',')
        product = Product(words[0], words[1], words[2], words[3])
        if line.__contains__('B'):
            listofBussinessProductFromFile.append(line)
        elif line.__contains__('H'):
            listofCommercialProductFromFile.append(line)
        elif line.__contains__('c'):
            listofHomeuseProductFromFile.append(line)
    flag = True

print('-------------------------------------')
for product in listofBussinessProductFromFile:
 print('Type of Business Products......',product)
print('-------------------------------------')
for product in listofHomeuseProductFromFile:
 print('Type of HomeUse Products......',product)
print('-------------------------------------')
for product in listofCommercialProductFromFile:
 print('Type of Commercial Products......',product)
print('-------------------------------------')