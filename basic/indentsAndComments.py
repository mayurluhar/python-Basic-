# print("Mayur")
# print("zinal")

# x= """
#     Error are part of programming
#                           -Mayur
# """
# print(x)

# x= input("enter number:")
# y = input("enter Color:")
#
# print(x,y)


#LIST
# myList = [2,"mayur", 1.1]
# myList1 = [3,"Zinal", 5.6]
# chnage = myList[1] = "Aayushi"
# print(myList)



#TUPLE
# myTuple = (5,"Jhon")
# myTuple[1] = "popai"
# print(myTuple)

#DICIONARY
# myD = {
#     "one": 1,
#     "two": "mayur",
#     "three": "Luhar"
# }
# print(myD.values())


#IF AND ELSE CONDITIONS

# myReview = int(input("Giver review 5 or 0"))
#
# if(myReview == 5):
#     print("thank you so much")
# elif(myReview == 0):
#     print("sorry for this expirence")
# else:
#     print("sorry for that")

#WHILE LOOP
# num = 0
# while(num < 10):
#     print(num+1,"hello World")
#     num = num +1
#
# print("program ended")


#FOR LOOP

# numRange = list(range(0, 10))
# #print(numRange)
# numRange = ["mayur", "zinal"]
# for num in numRange:
#     print(num, end=";")

#BREAK AND CONTINUE

# num = "helloWorld"
# for ls in num:
#     if ls == 'o':
#         continue
#     print(ls)
#
# print("outside of loop")


# import  random,math
# random.seed(100)
# print(random.random())
#
# print(min(1,7,9,-7))
#
# print(math.sqrt(6))

#LIST

# mcu = ["ironman", "thor", "loki"]
# dc = ["batman", "superman", "flash"]
#
# print(dc)
# del dc[1]

#dc.append("flash")
#dc.remove("batman")
# dc.insert(1, "superman")
# dc.reverse()
# print(dc + mcu)

#s= '{0} to {1}.in'
# string = "LearnCodeOnline"
# print(string[:9])
#print(s.format('Welcome','lCO'))

# num = "123456"
# for n in num:
#     print(n)

#n = "Learn Code Online"
# # while i in n:
# #     print(i, end= " ")
# for name in n.split():
#     print(n, end=",")

# print(3*1**3)
#print(~10)
#
# def userInfo(name, email, phoneNum=0):
#     print("Name is: ", name)
#     print("email is:", email)
#     print("phone Num is:", phoneNum)
#     return
#
# userInfo("mayur luhar", "mayueluhar274@gmail.com", 7383573666)

#
# def added(*n):
#     sum = 0
#     for i in n:
#         sum = sum + i
#     return sum
#
#
# x= input("Enter first Digit:")
# y= input("Enter second Digit:")
#
#
#
# print(added(int(x),int(y)))
# add= lambda  n1,n2: n1 + n2;
# print(add(2,4))



# def calculator():
#     x = int(input("""Enter Your the Choice:
#                     1 for +,
#                     2 for - ,
#                     3 for * ,
#                     4 for /,
#                     5 to exit:"""))
#     while(x < 5):
#         if(x == 1):
#             d1 = input("Enter digit one")
#             d2 = input("Enter digit one")
#
#             def add(n1,n2):
#                 print("addition is:",n1+n2);
#
#
#             add(int(d1), int(d2))
#         elif(x == 2):
#             d1 = input("Enter digit one")
#             d2 = input("Enter digit one")
#
#             def add(n1, n2):
#                 print("subtraction is:", n2 - n1);
#
#             add(int(d1), int(d2))
#             break
#         elif(x == 3):
#             d1 = input("Enter digit one")
#             d2 = input("Enter digit one")
#
#             def add(n1, n2):
#                 print("Multiplication is:", n1 * n2);
#
#             add(int(d1), int(d2))
#             break
#         elif(x == 4):
#
#             d1 = input("Enter digit one")
#             d2 = input("Enter digit one")
#
#             def add(n1,n2):
#                 print("Division is:",n1/n2);
#
#             add(int(d1),int(d2))
#             break
#
#         else:
#             print("Exit");
#             break


# num = 16465
#
# if(num > 1):
#     for i in range(2, num):
#         if(num%i == 0):
#             print("%d this is not a prime num.."%(num))
#             print(i,"times",num//i, "is",num)
#             break
#         else:

#             print("%d this is a prime num"%(num))
#
# x = int(input("lower"))
# y = int(input("upper"))
#
# for number in range(x, y):
#     if(number > 1):
#         for i in range(2, number):
#             if(number % i == 0):
#                 break
#         else:
#             print(number)

num = 5
fact =1

if(num < 1):
    print("negative")
elif(num == 0):
    print("1")
else:
    while(num != 0):
            fact = fact * num
            num = num -1
    print(fact)

    # for i in range(1, num + 1):
    #     fact = fact * i
    # print(fact)