f = open(r'C:\Users\AMIT_GORE\Desktop\Ashish.txt','w+',encoding='UTF-8')

f.write('powerpork\n')
f.write('indrag\n')
f.write('mishti\n')
f.write('sankarshan')
f.flush()
s=f.read()
print(s)



