### 11-26-2022
### Cl9nt @muthung_
### Email credentials saving.

# Modules
import getpass
import base64

# Welcome message

print("Hello Master.\n Please Sign Up or Sign In.")

# Get the Master Email and Password
master_E = getpass.getuser()
master_P = getpass.getpass("Your Master Password ?: ")

# Encode the password 
master_P_bytes = master_P.encode("ascii")
base64_bytes = base64.b64encode(master_P_bytes)

# Creating an empty dictionary
my_emails = {}

# Set a flag to indicate default email at the moment
default_email = True

while default_email:
    # Prompt user for email and password
    my_email = input("\n What is the Email?: ")
    my_passwd = input("\n What is the password?: ")
    
    #Storing the responses in a dictionary
    my_emails[my_email] = my_passwd
    
    #ask the user if they want the full list.
    Q_Quiz = input("\n Do you want to see the whole list?(Yes/No): ")
    if Q_Quiz == "no":
        default_email = False
    elif Q_Quiz == "yes":
        the_dict =my_emails.keys()
        print(the_dict)
        quit()
    
    # Adding is complte
print("\n ---------- Email-list Updated ----------")