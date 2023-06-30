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
import selenium import webdriver
import selenium.webdriver.chrome.options import Options


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

# Accept user input for domain or IP address
                 url = input("Enter the domain or IP address: ")

                 print("Select a technique:")
                 print("1. HTML Parsing")
                 print("2. Regular Expressions")
                 print("3. Headless Browsers")
                 technique = input("Enter the technique number: ")

# The type of data to be extracted
                 print("Select the type of data to be extracted:")
                 print("1. Text")
                 print("2. Links")
                 print("3. Images")
                 print("4. Tables")
                 data_type = input("Enter the data type number: ")

# The for techniques to employ
                 print("Select techniques to employ (maximum 2):")
                 print("1. Limit Requests (Rate and Frequency)")
                 print("2. Use of Proxies")
                 print("3. Randomize User-Agent")
                 print("4. Session Management")
                 techniques = input("Enter the technique numbers separated by a comma (e.g., 1,2): ").split(",")

# Initialize empty dictionary for storing scraped data
                 scraped_data = {}

# Perform web scraping based on user selections
                 if technique == '1':
    # HTML Parsing
                     if '1' in techniques:
        # Limit Requests (Rate and Frequency) technique
                         rate_limit = int(input("Enter the rate limit (in seconds): "))
                         frequency_limit = int(input("Enter the frequency limit (in requests per minute): "))
                         time.sleep(rate_limit)
                         time_elapsed = 0
                         request_count = 0
                         start_time = time.time()

                         response = requests.get(url)
                         soup = BeautifulSoup(response.content, 'html.parser')
                         if data_type == '1':
        # Extract text
                             text = soup.get_text()
                             scraped_data['text'] = text
                         elif data_type == '2':
        # Extract links
                             links = [link.get('href') for link in soup.find_all('a')]
                             scraped_data['links'] = links
                         elif data_type == '3':
        # Extract images
                             images = [image.get('src') for image in soup.find_all('img')]
                             scraped_data['images'] = images
                         elif data_type == '4':
        # Extract tables
                             tables = [str(table) for table in soup.find_all('table')]
                             scraped_data['tables'] = tables

                     elif technique == '2':
    # Regular Expressions
                        if '1' in techniques:
        # Limit Requests (Rate and Frequency) technique
                            rate_limit = int(input("Enter the rate limit (in seconds): "))
                            frequency_limit = int(input("Enter the frequency limit (in requests per minute): "))
                            time.sleep(rate_limit)
                            time_elapsed = 0
                            request_count = 0
                            start_time = time.time()

                        response = requests.get(url)
                        data = response.text
                        if data_type == '1':
        # Extract text
                            text = re.findall(r'<[^>]*>([^<]+)<[^>]*>', data)
                            scraped_data['text'] = text
                        elif data_type == '2':
        # Extract links
                            links = re.findall(r'<a\s+href=["\'](.*?)["\']', data)
                            scraped_data['links'] = links
                        elif data_type == '3':
        # Extract images
                            images = re.findall(r'<img\s+src=["\'](.*?)["\']', data)
                            scraped_data['images'] = images
                        elif data_type == '4':
        # Extract tables
                            tables = re.findall(r'<table[^>]*>(.*?)</table>', data, re.DOTALL)
                            scraped_data['tables'] = tables

                     elif technique == '3':
    # Headless Browsers
                         if '1' in techniques:
        # Limit Requests (Rate and Frequency) technique
                             rate_limit = int(input("Enter the rate limit (in seconds): "))
                             frequency_limit = int(input("Enter the frequency limit (in requests per minute): "))
                             time.sleep(rate_limit)
                             time_elapsed = 0
                             request_count = 0
                             start_time = time.time()

                         chrome_options = Options()
                         chrome_options.add_argument("--headless")
                         driver = webdriver.Chrome(options=chrome_options)
                         driver.get(url)
                         if data_type == '1':
        # Extract text
                             text = driver.find_element_by_tag_name('body').text
                             scraped_data['text'] = text
                         elif data_type == '2':
        # Extract links
                             links = [link.get_attribute('href') for link in driver.find_elements_by_tag_name('a')]
                             scraped_data['links'] = links
                         elif data_type == '3':
        # Extract images
                             images = [image.get_attribute('src') for image in driver.find_elements_by_tag_name('img')]
                             scraped_data['images'] = images
                         elif data_type == '4':
        # Extract tables
                             tables = [table.get_attribute('outerHTML') for table in driver.find_elements_by_tag_name('table')]
                             scraped_data['tables'] = tables

# Save scraped data to a JSON file
                     with open('scraped_data.json', 'w') as json_file:
                         json.dump(scraped_data, json_file)

# Print status message
                     print("Scraping completed. Data saved in 'scraped_data.json' file.")

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
