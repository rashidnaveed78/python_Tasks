"""a=1
c=3.2
d= "naveed"
e= complex(2+3)
print(e)

print(a)
a1=2
b = "rashid"
print(b)
print(a + a1)

print("The type of a is", type(a))
print( "The type of b is", type(b))
print("The type of a1 is", type(a1))
print("The type of c is" , type(c))
print("The type of d is", type(d))
print("The tyoe of e is", type(e))"""


"""print(2+5)
print(15*2)
print(15/2)
print(15-2)
print(15%6)
print(5**3)"""

"""n=15
m=7
ans1= n+m
print("Addition of",n, "and",m,"is", ans1)
ans2= n-m
print("Subtraction of" ,n,"and",m, "is" , ans2)
ans3= n/m 
print("Division of" ,n, "and" ,m, "is" ,ans3)
ans4=n*m
print("Multiplication of" ,n, "and", m, "is" ,ans4)
ans5=n%m
print(" Modulus of" ,n, "and" ,m, "is", ans5 )
ans6=n//m 
print("Floor division of" ,n, "and",m, "is" , ans6)"""


#Create simple Calculator

"""print("Calculator")

a=20
b=2

print("The value of a", a, "+" ,3, "is" ,a+b)
print("The value of a", a, "-" ,3, "is" ,a-b)
print("The value of a", a, "*" ,3, "is" ,a*b)
print("The value of a", a, "/" ,3, "is" ,a/b)
print("The value of a", a, "%" ,3, "is" ,a%b)
print("The value of a", a, "//" ,3, "is" ,a//b)"""

"""print("\nSimple Calculator")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")"""




#Simple Calculator

"""num1=float(input("Enter first number: "))
operater= input("Enter operater (+,-,*,/):")
num2=float(input("Enter second number:"))

if operater =="+":
    print("Result:",num1 +num2)
elif operater =="-":
    print("Result:",num1-num2)
elif operater =="*":
    print("Result:",num1*num2)
elif operater == "/":
    if num2 != 0:
        print("Result:", num1/num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")"""



#Type casting 

"""a="1"
b="2"

print(int(a) + int(b))  


string= "15"
number =7
string_number = int(string)
sum= number + string_number
print("The sum of both the numbers is:", sum)"""

#implicit typecasting

"""a= 7.9
b= 8
print(a+b)"""

#input function

"""a=input("Enter your Namer:")
print("My name is",a) """


"""#Strings

firstname="harry"
friend:"rashid"
anotherfriend ='rahat' 
Secondname='''hi rashid
hey i am good
i am also good'''


print("Hello,"+ Secondname)

print(firstname[0])
print(firstname[1])
print(firstname[2])
print(firstname[3])

print("for use a for loop)\n")


for character in Secondname:
    print(character)"""

"""#String slicing

names="rashid,naveed"
print (names[0:6])

print(len(names))



fruit= "Mango"
lenMango="lenfruit" 

print("Mango has five",lenMango)

print("fruit"[0:4])
print("fruit"[0:-2])
print("fruit"[-1:-2])"""



#nm= "Harry"
#print(nm[-4:-2])""""




#String Method in python
#strings are immutable

"""a= "harry is a good boy!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))  #remove any trelling character
print(a.replace("harry","rashid"))
print(a.split(" "))

blogHeading ="introduction of TMC"
print(blogHeading.capitalize())

str1="welcome to TMC"
print(str1.center(50))  # for center

print(len(str1.center(50)))

a="harry"
print(a.count("harry"))

str1="welcome to the TMC"
print(str1.endswith("!!!"))

str1="welcome to the TMC"
print(str1.endswith("to", 4, 10))



print(str1.find("is"))"""

#Str1="He is name us Dab. He is an honest man"
#print(Str1.find("ishh"))
#print(Str1.index("ishh"))

#str1="WelcomeTotheTMC"
# print(str1.isalnum())


# str1 = "welcome00"
# print(str1.isalpha())

# str1 = "Welcome00"
# print(str1.islower())

# str1 = "Welcome00"
# print(str1.isprintable())


# str1 = "    "
# print(str1.isspace())

# str1 = "Welcome00"
# print(str1.istitle())

# str1 = "We Welcome00"
# print(str1.startswith("we"))

# str1 = "Welcome00"
# print(str1.swapcase())

# str1 = "Welcome00"
# print(str1.title())





# a=int(input("Enter your age:"))
# print("your age is:",a)

# # print(a>18)
# # print(a<=18)
# # print(a!=18)
# # print(a>18)


# if(a>18):
#     print("you can driver")
    
# else:
#     print("You cannot driver")



# appleprice=70
# budget=200
# if(appleprice <= budget):
#     print("Alexa, add 1 kg to Apples to the cart")
# elif (budget-appleprice>70):
#     print("its ok to buy")

# else:
#     print("Alexa, do not add apples to the cart")



num=1
if(num<0):
    print("number us negative.")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is greater then 20")
    else:
        print("numbe is greater than 20")
else:
    print("number us zero")
        

