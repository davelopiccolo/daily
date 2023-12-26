import random
import secrets
import string
import math
import numpy as np

# a = 5
# b = 6
# c = "bau"
# d = "miao"
# print(a+b)
# print(c+d)

# def sum (a,b):
    
#     print(a+b)

# sum(15,25)

# def fruit_loops (fruit):
#     for x in fruit: 
#       print(x)
    
# fruit_loops("banana")
# fruit_loops("mango")

# def classroom (classes):
#     for x in classes:
#         print(x)

# first = ["Davide" , "Aurora" , "amantediAurora"]
# first.pop(2)
# classroom(first)

# print(first[1])

# if len(first) == 3:
#     print("aurora è un pò putt")
    

# print("Aurora Tradisce?")

# options = ["yes", "no", "maybe"]

# answer = random.choice(options)
# answer2= random.choice(options)

# print(answer)

# print("cerco i pokemon nuovi?")

# print(answer2)




# print("Wise Choice") if answer == "no" else print("no comment") 

mylist = [1,2,2,3,4,5,5]
mylist = list(dict.fromkeys(mylist))
print(mylist)


dictionary = { "parola" : "suca"}
print(dictionary["parola"])


dictiolist = [ {"key" : 3} , {"key" : 4 , "name" : "DAvide"}]
print(dictiolist[1]["name"])


pokemon = [{
    "name": "Charmander",
    "typing": "fire",
    "catchrate": 15
           } ,
           {
    "name" : "Squirtle",
    "typing" : "Water",
    "catchrate" : 20            
           }]
numbers = [10,20,30,40,50,60,70,80]
def catch():
    poke = random.choice(pokemon)
    print("a Wild " + poke["name"]+ " has appeared")
    catching = random.choice(numbers)
    print("you catched " + poke["name"] + " it's a " + poke["typing"] + " type pokemon") if catching > poke["catchrate"]  else print(poke["name"] + " has fled")
    
catch()
             
numbers = [1,2,3,5,78,145,13,12]
maxim = max(numbers)
print(maxim)


def sqrt(number):
    print(math.floor(math.sqrt(number)))



sqrt(42)

def pow(number, power):
    return (math.floor(math.pow(number, power)))
    
pow(2,5)



for n in numbers:
    print(pow(n, 2))
    
    
for w in ["banana" , "apple"]:
    print("my favourite food is " + w)


for poke in pokemon:
    print(poke["name"] + " is a " + poke["typing"] + " type pokemon")
    


def passgenerator():
    letters_uppercase = string.ascii_uppercase
    letters_lowercase= string.ascii_lowercase
    digit = string.digits
    alphabet = letters_lowercase + letters_uppercase + digit    
    password_lenght = 12
    password = ""
    for i in range(password_lenght):
        password += "".join(secrets.choice(alphabet))
    print(password)
    
passgenerator()


# lower = int(input("Lower Bound : "))
# upper = int(input("Upper Bound : "))
# x = random.randint(lower, upper)

# answer = int(input("What's the number? "))

# if x == answer :
#     print ("Right! " + str(x) + " was the answer! :D")
# else :
#     print ("No , sorry! " + str(x) + " was the answer :(")    
    


# arr = np.array([[1,2,3,4,5] , [6,7,8]])
# print(arr)

arr = np.array([[1,2,3], [5,6,7], [9,10,11]])
print(arr)
print(arr.shape)
row = arr[2, :]
column = arr[:, 2]
print(row)
print(column)


lista = np.array([[1,2,3],['Davide', 'Aurora', 3]])
row2= lista[1, :]
column2 = lista[:,2]
print(column2)



class PocketMonster:
    def __init__(self, name, type):
        self.name= name
        self.type= type

pkmn1 = PocketMonster("Charmander" , "Fire")

print(pkmn1.type)

# def check_fermat(a,b,c,n):
    
#     result = a**n + b**n
    
#     print(result)
#     print(c**n)
    
#     if a**n + b**n == c**n :
#         print("Fermat was wrong!")
#     else:
#         print("looks like he's right")

# check_fermat(a=int(input("a: ")),b=int(input("b :")),c=int(input("c :")),n=int(input("n :")))
    

def absolute_val(a):
    return abs(a)

print(absolute_val(-133))

arr_try = np.array([[1,2], [5,6], [9,10]])
print(arr_try)
print(arr_try[:,1])

def spelling(word):
    for char in word:
        print(char)
    print(word[0:2])
    
spelling("love")

def in_common(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_common("Love" , "above")


    
      
