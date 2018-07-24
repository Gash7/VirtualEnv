


try:
   fh = open(r"C:\Users\AMIT_GORE\DesktopAshish.txt")
   fh.write("This is my test file for exception handling!!")


except FileNotFoundError:
   print('File not found error')



except :
   print("Written content in the file successfully")

''''

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(1)))
print (int(KelvinToFahrenheit(505.78)))
print(int(KelvinToFahrenheit(-253)))



#try:
   #fh = open(r"C:\Users\AMIT_GORE\Desktop\Ashish.txt", "r")
   #fh.read()
#finally:
   #print("Error: can\'t find file or read data")
'''