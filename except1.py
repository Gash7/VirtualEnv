try:
   fh = open("C:\\Users\AMIT_GORE\Desktop")
   #fh.write("This is my test file for exception handling!!")
   fh.readlines()
   print()
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()