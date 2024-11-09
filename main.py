# Program to check if the Nth bit is set or not
def setOrNot(number, n):
  # Make a mask variable by left shifting 1 (k-1) times and check if (n ANS mask) equals 1 or 0 
  
    if number & (1 << (n - 1)):
      print("\nSET")
    else:
      print("NOT SET")
number = int(input("Enter the number: "))
n = int(input("Enter the bit position: "))
setOrNot(number, n)