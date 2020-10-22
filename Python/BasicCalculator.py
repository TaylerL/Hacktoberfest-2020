#Basic Calculator in Python without any gui.

#create functions for calculations

def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2

def mul(num1, num2):
	return num1 * num2

def div(num1, num2):
	return num1 / num2

def power(num1,num2):
	return num1**num2

def wholenum(num1, base=10):
    return base * round(num1/base)

print("Functions of the Calculator\n "\
	   "1. Addition\n " 
	   "2. Subtraction \n"
	   "3. Multiplication \n"
	   "4. Divide \n" 
	   "5. Power of Another Number \n"
	   "6. Display Number to Nearest Whole Number \n")

#Take Input From Keyword
select = input("Please Choose Between 1 to 6 from Above: ")

number_1 = float(input("Type Your First Number: "))
number_2 = float(input("Type Your Second Number: "))




if select == '1':
	print(number_1, "+", number_2, '=')
	print(add(number_1, number_2))

elif select == '2':
	print(number_1, '-', number_2, '=')
	print(sub(number_1, number_2))

elif select == '3':
	print(number_1, '*', number_2, '=')
	print(mul(number_1, number_2))

elif select == '4':
	print(number_1, '/', number_2, '=')
	print(div(number_1, number_2))

elif select == '5':
	print(number_1, 'to the Power of', number_2, '=')
	print(power(number_1, number_2))

elif select =='6':
	print(number_1, 'to Nearest Whole Number', '=')
	print(wholenum(number_1))
	print(number_2, 'to Nearest Whole Number', '=')
	print(wholenum(number_2))

else:
	print('Invalid Input! Please Try Again. ')
	
print('Thank you, Have a Great Day!')