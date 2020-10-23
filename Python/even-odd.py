def nums():
   num = int(input("Enter a number: "))
   if (num % 2) == 0:
      print("The number is Even")
      print("{0} is Even".format(num))
   else:
       print("The number is Odd")
      print("{0} is Odd".format(num))
      
 num()
