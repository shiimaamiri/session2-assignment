name = (input("your name: "))
family = input("your family: ")
score1 = float(input("math score: "))
score2 = float(input("geometry score: "))
score3 = float(input("physics score: "))
avg = (score1+score2+score3)/3 
if avg >= 17: 
    print ("your name:", name , family ,"great")
if 12 <= avg < 17 : 
        print("your name:", name , family ,"normal")
if avg < 12: 
    print("your name:", name , family ,"fail")
