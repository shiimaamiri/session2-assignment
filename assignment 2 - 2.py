num1 = int(input("enrer num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
if num1 + num2 > num3 :
    if num1 + num3 > num2 :
        if num2 + num3 > num1 :
            print("okay ")
        else : 
            print("not okay")  
    else : 
        print("not okay")
else :
    print("not okay") 

         #حالت دیگه برای شرط مثلث بودن یا نبودن                  
      #if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1 :
      #print("okay")
      #else :
      #print("not okay") 