import math
op = input("enter op(+, -, *, /, sin, cos, tan,cit, factorial, radical ): ")
if op=="+":
    num1 = int(input("enrer num1: "))
    num2 = int(input("enter num2: "))
    result = num1 + num2 
if op=="-":
    num1 = int(input("enrer num1: "))
    num2 = int(input("enter num2: "))
    result = num1 - num2
if op=="*" :
    num1 = int(input("enrer num1: "))
    num2 = int(input("enter num2: "))
    result = num1 * num2
if op=="/" :
    num1 = int(input("enrer num1: "))
    num2 = int(input("enter num2: "))
    if num2 ==0: 
        result = "error"
    else:    
        result = num1 / num2 
if op=="sin" :
    num3 = int(input("enter num1: "))
    result = math.sin(num3)
if op=="cos":
    num3 = int(input("enter num1: "))
    result = math.cos(num3)  
if op=="tan":
    num3 = int(input("enter num1: "))
    result = math.tan(num3)  
if op=="factorial":
    num3 = int(input("enter num1: "))
    result = math.factorial(num3)        
if op=="radical":
    num3 = int(input("enter num1: "))
    result = math.sqrt(num3)
if op=="cot":
    num3= 1/math.tan(num3)         
print(result)          