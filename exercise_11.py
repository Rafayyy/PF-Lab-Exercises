# -*- coding: utf-8 -*-
"""Exercise 11

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IBkEzezHDRt9U2snnH7jWFRIWTzByxdm

##1
"""

dic = { }

while True :
    product = input("Enter the name of product(enter 0 for exit): ")

    if product=="0":
        break

    else:
        
        price = int(input("Enter the price of product = ")) 
     
        dic [ product ] = price

while True:

    name= input("Enter the name of the product to know the price (enter 0 to exit): ")
    
    if name=="0":
        break
    else:
        if name not in dic:
            print('Name of the product is Invalid')
  
        else:
            print("Price of product is ",dic[name])
            print()

"""##2"""

dic={'Lux':100, "Bonus":300, "Rice":500}

amount=int(input("Enter an amount (in dollars) to check products less than amount: "))

product_less=[price for price in dic if dic[price]<amount]

print("the products whose price is less than the amount: ", product_less)

"""##3"""

#a

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

user_input= input("Enter Name of a month: ")

for key, values in year.items():
     if user_input == key: 
        print( values)

#b

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

sorted_year ={key:year[key] for key in sorted(year)}

print(sorted_year.keys())

#c

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

for keys,values in year.items():
    if int(values) == 31:

      print(keys)

#d

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

user_input= input("Enter Name of a month: ")

for key, values in year.items():
     if user_input in key: 
        print( values)

"""##4"""

ids = {'Rafay' : "1234", 'Ibraheem' : "pan",'Ahmed' : "rawalpindi",'Bilal' : "900", 'Shadab' : "666",'Afridi' : "555",'Tehreem' : "444",'Faheem' : "333",'Maryum' : "222",'Zainab' : "111" }

username = input("Enter username : ")

if username in ids :

    password = input("Enter password : ")

    if ids[username] == password :
        print ("You have successfully logged in")
    else :
        print ("Invalid password.")
else :
    print ("Your account doesnot exisst")

"""##5"""

dic ={}
lstwin = []
lstrec = []
while True :
    name = input ("Enter the name of team (enter 0 for exit)= ")
    if name == "0" or name == "0" :
        break

    else :
        win = int (input("Enter the matches won = "))
        loss = int(input("Enter the matches lost = "))
        print()
        dic [ name ] = [ win , loss ]
        lstwin += [ win ]
        if win > 0 :
            lstrec += [ name ]
#a
nam = input ("Enter the name of team For Winning = ")
print ("Winning percentage = ",dic [ nam ][0] *100 / (dic [nam ][0] + dic[nam ][1] ))
print()
#b
print("Winning list of all team = ",lstwin)
#c
print("Team who has winning records are ",lstrec)

"""##6"""

def team():

   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(team())

"""##7"""

matrix=[1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def creatList():
    matrix_dict={}

    for num in range(len(matrix)):
        key = matrix[num]
        value = matrix.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())

"""##8"""

import random

all_cards ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1=[]
player2 =[]
for card in range(cards):
    c1 =random.choice(list(all_cards.values()))
    c2= random.choice(list(all_cards.values()))
    player1.append(c1)
    player2.append(c2)
print(player1,player2)

if sum(player1) > sum(player2):
    print("Player 1 wins with ",sum(player1)," Against Player 2 with",sum(player2))
elif sum(player2) > sum(player1):
    print("Player 2 wins with ",sum(player2)," Against Player 1 with",sum(player1))