"""import time
timestamp =time.strftime( '%H:%M:%S')
print(timestamp)

timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


import time
name = input('Enter your name: ')
recenttime = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
c= name.capitalize()
if(4<=Recenttime<12):
    print('GOOD MORNING',c,'its',recenttime)
elif(12>=Recenttime<17):
    print('GOOD EVENING',c,'its',recenttime)
else:
    print('GOOD NIGHT',c,'its',recenttime)
# print('Hii',name,'its',recenttime)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59"""



"""import time

name = input('Enter your name: ')
recenttime = int(time.strftime('%H'))
c = name.capitalize()

if 4 <= recenttime < 12:
    print('Good morning', c)

elif 12 <= recenttime < 17:
    print('Good afternoon', c)

elif 17 <= recenttime < 21:
    print('Good evening', c)

else:
    print('Good night', c)"""


"""x=int(input("Enter your first number"))

match x:

    case 0:
        print("x is zero") 
    case 4:
        print("x is 4")"""

"""#for Loop

name= "rashid"
for i in name:
    print(i,( ","))
    if(i=="a"):
        print("Special")

colors=["red","green","blue"]
for colors in colors:
    print(colors)
    for u in colors:
        print(u)"""



# for k in range(5):
#     print(k+1)

# for k in range (1,9):
#     print(k+1)

# for k in range(1,2000):
#     print(k)

#for k in range (1,9,2):
#    print(k)


#while loop
# i=int(input("Enter the number:"))
# i=0
# while (i!=32):
#     print(i)
#     i=i+1
# print(" done with loop")

"""count=5
while(count > 0):
    print(count)
    count=count-5
else:
    print("LOOP")"""

#break and continue

# for i in range(12):
#     if(i==10):
#         print("Stop")
#         continue

#     print("5 X", i+1,"=",5*i)

for i in range(1,101,1):
    print(i,end =  " ")
    if(i==50):
        break
    else:
        print("Mississipii")
print("Thank you")





