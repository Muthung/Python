## Import OS, msvcrt
import os, whois, pyfiglet, random, pyqrcode, phonenumbers
import msvcrt as m
import tkinter as tk

## Function for waiting for key press
def wait():
    m.getch()

## Clear screen before to show menu, cls is MS Windows command
os.system('cls')

## Menu Options

ans=True
while ans:
    print("""
    --------------------------------------
    |       My Python Trial Programs      |
    |       muthunguclintn@gmail.com      |
    --------------------------------------
    
    1: Body mass generator.
    2: Domain name information.
    3: Font art.
    4: Invoice generator.
    5: Number guess.
    6: Password generator.
    7: Phone info.
    8: QR code generator and reader.
    9: RPS.
    10: Saving calculator.
    11: Email Box.
    12: Exit/Quit.
    """)

ans=input("Choose a number (1-12): ")

### Body mass index is calculated from weight and height of a person
### Dividing a persons Weight (kg) by Height (m) then divide by Height (m)

height = float(input("Enter your Height (cm) = "))
weight = float(input("Enter your Weight (Kg) = "))

height = height/10
bmi = weight/(height*height)

print("Fount It !!! Your Body Mass Index is = ", bmi)
if(bmi > 0 ):
    if(bmi <= 16 ):
        print("Bro get yourself Food, you starving.")
    
    elif(bmi <=18.5 ):
        print(" Hey you are underweight ")

    elif(bmi <=25 ):
        print("Bro Congrats. You are Healthy ")

    elif(bmi <=30 ):
        print("Hahaha !!!, U extra bro, Overweight ")
    
    else:
        print("You are severly overweight. peace. ")
    
else:
    ("enter valid details")
    

## Domain-Name-Information

from xml import dom
import whois
domain=input("Enter the Domain: ")
domain_info = whois.whois(domain)
for key, value in domain_info.items():
    print(key,':', value)


### Font Art

import pyfiglet
font=input("Enter your Chosen Name : ")
font_art=pyfiglet.figlet_format(font)
print(font_art)


### Invoice Generator

########## product and price for my items

product1_name, product1_price = 'Smartphone', 100
product2_name, product2_price = 'Computer', 200
product3_name, product3_price = 'Accommodation', 300

########## company name and information 

company_name = 'Alkebulan Enterprises'
company_address = '00100 & 30208'
company_city = 'Nairobi $ Kapsara'

########## ending message

message = 'Thanks for shopping with us today!'

########## a top border 

print('*' * 50)

########## company information first 

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

########## line between sections

print('=' * 50)

########## header for section of items

print('\tProduct Name\tProduct Price')

########## a statement for each item 

print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

########## a line between sections 

print('=' * 50 )

########## header for section of total

print('\t\t\tTotal')

########## calculate total price and print out 

total = product1_price + product2_price + product3_price 
print('\t\t\t${}'.format(total))

########## a line between sections

print('=' * 50)

########## thank you message

print('\n\t{}\n'.format(message))

########## bottom order

print('*' * 50)



### Number Guess

random_number = random.randint(7, 49)       # Variable to store the random numbers, Randit returns a random number depending on range set.
tries = 1       # Variable tries = 1 

username = input("Hello Friend, Whats your username ? ")       # User input 
print("Hello", username + ", ",)

question = input ("Wanna play a game ? [Yes/No] ")
if question == "No":
    print("Chickens are out, I see ")

if question == "Yes":
    print("I have a number between  7 and 49 ")

    guess = int(input("Guess a number : "))
    if guess > random_number:
        print("Too high my friend, Have another go.")
    
    if guess < random_number:
        print("Too Low my friend, Have another go.")


    while guess != random_number:   # While loop till the != random_number
        tries += 1      # increase tries by 1, with each loop

        guess = int(input("Give it another try."))
        if guess < random_number:
            print("Too Low my friend, Have another go. ")

    if guess == random_number:
        print("Holy !!! You Win ! The number was ", random_number, "and it only took ", tries, "tries")
        


### Password Generator


passlen = int(input("Enter the length of the password = "))

s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ!@#$%^&*()?<>{}[]1234567890"

p = "".join(random.sample(s,passlen))
print(p)


### QR-Code


from pyqrcode import QRCode

# String which represent the QR code

s = "https://www.youtube.com/watch?v=xjDjIWPwcPU"

# Generate QQr code 

url = pyqrcode.create(s)

# Create and save the png file naming "qrcode.png"

url.svg("panther.svg", scale = 8 )


### RPS


choices = ["Rock", "Paper", "Scissors"]

computer = random.choice(choices)

player = False
comp_score = 0
players_score = 0

while True:
    player = input("Rock, Paper or Scissors? ").capitalize()

    ### conditions

    if player == computer:
        print("Amazing !!!, A Tie.")
    
    elif player == "Rock":
        if computer == "Paper":
            print("You lose !", computer, "covers", player)
            comp_score += 1

        else:
            print("Amazing !!! You Win !", player, "smashes", computer)
            players_score += 1

    elif player == "Paper":
        if computer == "Scissors":
            print("You Lose...", computer, "cut", player)
            comp_score += 1

        else:
            print("Amazing !!! You Win", player, "covers", computer)
            players_score += 1

    elif player == "Scissors":
        if computer == "Rock":
            print("You Lose...", computer, "smashes", player)
            comp_score += 1

        else:
            print("Amazing !!! You Win", player, "cut", computer)
            players_score += 1

    elif player == "End":
        print("Final Scores : ")
        print(f"CPU:{cpu_score}")
        print(f"player:{players_score}")

        break

### Savings Calculator
# Takes on the salary of a person with travel, food and miscellaneous
# tkinter library
# create the main window
# add widget to main window 
# apply event functionalities to the buttons


def exit():
    window.destroy()

def clear_all():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.config(state = 'normal')
    e5.delete(0, tk.END)
    e5.config(state = 'disabled')

def cal_savings():
    e5.config(state = 'normal')
    e5.delete(0, tk.END)
    e5.config(state = 'disabled')
    
    salary = int(e1.get())
    
    total_expenditure = int(e2.get()) + int(e3.get()) + int(e4.get())
    savings = salary - total_expenditure
    
    e5.config(state = 'normal')
    e5.insert(0, savings)
    e5.config(state = 'disabled')





window = tk.Tk()
window.geometry("300x400")
window.config(bg = "#f39c12")
window.resizable(width = False, height = False)
window.title('Savings Calculator')

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()

l1 = tk.Label(window, text = "Enter the values", font = ("Arial", 20), fg = "Black", bg = "White")

l2 = tk.Label(window, text = " Total salary : ", font = ("Arial", 10), fg = "Black", bg = "White")
e1 = tk.Entry(window, font = ("Arial", 11), textvariable = v1)

l3 = tk.Label(window, text = " Travel : ", font = ("Arial", 10), fg = "Black", bg = "White")
e2 = tk.Entry(window, font = ("Arial", 11), textvariable = v2)

l4 = tk.Label(window, text = " Food : ", font = ("Arial", 10), fg = "Black", bg = "White")
e3 = tk.Entry(window, font = ("Arial", 11), textvariable = v3)

l5 = tk.Label(window, text = " Miscellaneous : ", font = (" Arial ", 10), fg = "Black", bg = "White")
e4 = tk.Entry(window, font = (" Arial ", 11), textvariable = v4)

b1 = tk.Button(window, text = "Calculate your savings ", font = (" Arial", 15), command = cal_savings)

l6 = tk.Label(window, text = "Your savings : ", font = (" Arial ", 10), fg = "Black", bg = "White")
e5 = tk.Entry(window, font = (" Arial ", 11), state = 'disabled', textvariable = v5)

b2 = tk.Button(window, text = "Clear the values ", font = (" Arial ", 15), command = clear_all)
b3 = tk.Button(window, text= "Exit the application", font = (" Arial ", 15), command = exit)

l1.place(x = 50, y = 20)
l2.place(x = 20, y = 70)
e1.place(x = 120, y = 70)
l3.place(x = 20, y = 100)
e2.place(x = 120, y = 100)
l4.place(x = 20, y = 130)
e3.place(x = 120, y = 130)
l5.place(x =20, y = 160)
e4.place(x = 120, y =160)
l6.place(x = 20, y =260)
e5.place(x = 120, y = 260)
b2.place(x = 70, y = 300)
b3.place(x = 60, y = 350)

window.mainloop()



### Get information about a phone number ###
### Country name                         ###
### Network provider                     ###
### Geocoder : to know the location      ###



from phonenumbers import geocoder

from phonenumbers import carrier

# for time zone names

from phonenumbers import timezone

# from phone_iso3166.country import *

input_number = input("Enter the phone number : ")
phone_number = phonenumbers.parse(input_number)
carrier_number = phonenumbers.parse(input_number)
tz_number = phonenumbers.parse(input_number)

print(geocoder.description_for_number(phone_number, 'en'))
print(carrier.name_for_number(carrier_number, "en"))
print(timezone.time_zones_for_number(tz_number))

# print(phone_country(input_number))