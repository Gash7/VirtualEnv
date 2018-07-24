
try:
   fh = open(r"C:\Users\AMIT_GORE\DesktopAshish.txt")
   fh.write("This is my test file for exception handling!!")


except Exception:
   print("Written content in the file successfully")


except FileNotFoundError:
   print('File not found error')


