### Body mass index is calculated from weight and height of a person

### Dividing a persons Weight (kg) by Height (m) then divide by Height (m)

height = float(input("Enter your Height (cm) = "))

weight = float(input("Enter your Weight (Kg) = "))

height = height/100

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
