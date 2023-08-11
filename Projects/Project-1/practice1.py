## Import os, whois, pyfiglet, random, pyqrcode, phonenumbers, xml

from random import randint
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tkinter import *
from gtts import gTTS
from playsound import playsound
import requests
import json
import random
import os
import socket
import re



## This is a program for displaying  Body Mass Index
## upon User input of Height and Weight

def myBMI():
    height=float(input("Enter your Height (cm) : "))
    weight=float(input("Enter your Weight (kg) : "))
    
    height = height/10
    bmi = weight/(height*height)
    
    print("===================================================================" + 
          "\nFound It !!!, Your Body Mass Index is : ",bmi )
    if (bmi > 0):
        if(bmi <= 16):
            print("\nNB: Bruv, You need food. Don't Starve Mandem.") 
        elif(bmi <= 18.5 ):
            print("\nNB: Bruv, you are underweight. You need a Balanced Diet. ")
        elif(bmi <=25 ):
            print("\nNB: Congrats Bruv, You are Healthy. Consistency is key.")
        elif(bmi <=30 ):
            print("\nNB: Hahaha !!!, You are extra bruv. I mean Overweight.")
        else:
            print("Woow !!!, You are severly overweight. Start burning cals.")
    else:
        ("Enter valid details")
  
## This is a program for playing a game.
## Rock, Paper, Scissors.
##

def RoPaSc():
    
    #create a list of play options
    teams=["Rock", "Paper", "Scissors"]
    
    #assign a random play to the computer
    comp=teams[randint(0,2)]
    
    #set a player to False
    player=False
    
    while player==False:
        
        #set player to True
        player=input("\n ======================================="
                        "\n |Choose between : Rock, Paper, Scissors.|"
                        "\n |Enter 'q' to Quit.                     |"
                        "\n ======================================="
                        "\n : ")
        if player==comp:
            print(" \n Thats good. A Tie!")
        elif player=="Rock":
            if comp=="Paper":
                print("\n !>> Sad Mandem. You Lose!", comp, "covers", player)
            else:
                print("\n >>> Congrats Bruv. You Win!", player, "smashes", comp)
        elif player=="Paper":
            if comp=="Scissors":
                print("\n !>> Sad Mandem. You Lose!", comp, "cuts", player)
            else:
                print("\\n >>> Congrats Bruv. You Win!", player, "covers", com)
        elif player=="Scissors":
            if comp=="Rock":
                print("\n !>> Sad Mandem. You Lose!", comp, "smashes", player)
            else:
                print("\n >>> Congrats Bruv, You Win!", player, "cuts", comp)
        elif player=="q":
            break
        else:
            print("\n What is that !, not valid. Check your grammar.")
        
        #player was set to True, but we wantit to be False so the loop continues
        player=False
        comp=teams[randint(0,2)]
    
## This is a program for coverting text to speech
## Text to Speech

def tetos():

    message = text_field.get()

    speech = gTTS(text = message)

    speech.save("data.mp3")

    playsound("data.mp3")

    def exit():

        window.destroy()

    def reset():
        
        msg.set("")

    window = Tk()

    window.geometry("350x300")

    window.configure(bg='#7ad7a0')

    window.title("Tetos")

    Label(window, text = "   Tetos    ",  font = " arial 20 bold ", bg = 'black', fg = "white").pack()

    msg = StringVar()

    Label(window, text = " Enter your text here : ", font = ' arial 20 bold ', fg = "darkgreen").place(x=5, y=60)

    text_field = Entry(window, textvariable = msg, width = '30', font = ' arial 15 bold ', bg = "lightgreen")

    text_field.place(x=5, y=100)

    Button(window, text = "Next", font = 'arial 15 bold', command = tetos, width = '20', bg = 'orchid', fg = "white").place(x=35, y=140)

    Button(window, font = 'arial 15 bold', text = 'Reset', width = '20', command = reset, bg = 'darkgreen', fg = "white").place(x=35, y=190)

    Button(window, font = 'arail 15 bold', text = 'exit', width = '20', command = exit, bg = 'red', fg = "white").place(x=35, y=240)

    window.mainloop()


while True:
    print("\n --------------------------"+
          "\n|   Menu Driven Program    |"+
          "\n| muthunguclintn@gmail.com |"
          "\n ---------------------")
    print("\n 1. Body Mass Index.")
    print(" 2. Rock, Paper, Scissors.")
    print(" 3. Text to Speech.")
    print(" 4. quit.")
    choice=int(input("Enter a number (1-10): "))
    
    if choice==1:
        myBMI()
        
    elif choice==2:
        RoPaSc()

    elif choice==3:
        tetos()
        
    elif choice==4:
        break
    
    else:
        print("Please enter the correct choice")
