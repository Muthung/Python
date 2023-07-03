## Import os, whois, pyfiglet, random, pyqrcode, phonenumbers, xml

from random import randint
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
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
    


while True:
    print("\n --------------------------"+
          "\n|   Menu Driven Program    |"+
          "\n| muthunguclintn@gmail.com |"
          "\n ---------------------")
    print("\n 1. Body Mass Index.")
    print(" 2. Rock, Paper, Scissors.")
    print(" 5. quit")
    choice=int(input("Enter a number (1-10): "))
    
    if choice==1:
        myBMI()
        
    elif choice==2:
        RoPaSc()

    elif choice==3:
        break
    
    else:
        print("Please enter the correct choice")
