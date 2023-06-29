## Import os, whois, pyfiglet, random, pyqrcode, phonenumbers, xml

from random import randint
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import json
import random
import os
import socket

## This is a program for displaying  Body Mass Index
## upon User input of Height and Weight
##
##

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
    
## This is a program for scraping information from websites
## Information such as text, links, images, tables...
##

def Webscrapper():
    # Prompt user for URL to scrape
    url = input("Enter the URL to scrape: ")

    # Prompt user for types of information to extract
    info_types = input("Enter the types of information to extract (text, links, images): ").split()

    # Set up rotating user agents
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
    ]

    # Set up headers with a random user agent
    headers = {'User-Agent': random.choice(user_agents)}

    # Make request to the URL with headers
    response = requests.get(url, headers=headers)

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract desired information based on user input
    data = {}
    for info_type in info_types:
        if info_type == "text":
            data["text"] = soup.get_text()
        elif info_type == "links":
            data["links"] = [link.get('href') for link in soup.find_all('a')]
        elif info_type == "images":
            data["images"] = [image.get('src') for image in soup.find_all('img')]
    
    #Set default path in Documents to save JSON output to
    default_path=os.path.join(os.path.expanduser('~'), 'Documents', 'web_scraper_output.json')

    # Output data in JSON format
    with open(default_path, 'w') as outfile:
        json.dumps(data, outfile, indent=4)
        print(f"JSON output saved to {default_path}")

## Port Scanner
## I have used 'socket module'


while True:
    print("\n --------------------------"+
          "\n|   Menu Driven Program    |"+
          "\n| muthunguclintn@gmail.com |"
          "\n ---------------------")
    print("\n 1. Body Mass Index.")
    print(" 2. Rock, Paper, Scissors.")
    print(" 3. Web Scrapper.")
    print(" 4. port_scanner")
    print(" 5. quit")
    choice=int(input("Enter a number (1-10): "))
    
    if choice==1:
        myBMI()
        
    elif choice==2:
        RoPaSc()
    
    elif choice==3:
        Webscrapper()
        
    elif choice==4:
        port_scanner()

    elif choice==5:
        break
    
    else:
        print("Please enter the correct choice")
