#                                     Variables
# MyVariable1

Greetings = "Hello, welcome to my python scripts"

print(Greetings)

# MyVariable2

myProjects = "Here are some of the projects am working on : "

print(myProjects)

# MyVariable3

projects = ["Responsive Website", "React-native website", "Javascript Projects"]

a, b, c = projects

print(a)
print(b)
print(c)

# MyVariable4 
#Global Variable

link = "https://github.com"

def myFunction():

    print("You can view my profile page in " + link )

myFunction()

#Using global variable outside a function 

print("Here is the link: " + link)

#                           Dictionary

myDIct = {
    "Name" : " Clinton Muthungu ",
    "Profession" : " Software Developer ",
    "School" : " Kenyatta University "
}

def myName():
    
    print(myDIct)

myName()


