# Store input numbers:  
num1 = input('Enter Your first number: ')  
num2 = input('Enter Your second number: ')  
  
# Addition of two numbers  
sum = float(num1) + float(num2)  
# Subtraction of two numbers  
min = float(num1) - float(num2)  
# Multiplication of  two numbers  
mul = float(num1) * float(num2)  
#Division of two numbers  
div = float(num1) / float(num2)  
# Modulus of two numbers
mod = float(num1) % float(num2) 

# Display the sum  
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))  
# Display the subtraction  
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, min))  
# Display the multiplication  
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))  
# Display the division  
print('The division of {0} and {1} is {2}'.format(num1, num2, div)) 
# Display the modulus
print('The modulus of {0} and {1} is {2}'.format(num1, num2, mod))