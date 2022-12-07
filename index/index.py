## Import os, whois, pyfiglet, random, pyqrcode, phonenumbers, xml

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
     
while True:
    print("\n --------------------------"+
          "\n|   Menu Driven Program    |"+
          "\n| muthunguclintn@gmail.com |"
          "\n ---------------------")
    print("\n 1. Body Mass Index.")
    print(" 2. Body2.")
    choice=int(input("Enter a number (1-10): "))
    
    if choice==1:
        myBMI()
        
    elif choice==2:
        break
    
    else:
        print("Please enter the correct choice")
