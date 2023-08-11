# import module

import ftplib

from ftplib import FTP

# define server ftp address

site_addr = "ftp.ubuntu.com" # vsfptd ftp server connection

# make a connection to server

ftp_obj = ftplib.FTP(site_addr)

# login to the server

ftp_obj.login()

print("Connected to " + site_addr + " . Welcome message is : Hello King ")

print(" Present working directory is : ")

# present working directory

present = ftp_obj.pwd()

print(present)

print(" Contents of the directory " + " is : ")

# content of present directory

ftp_obj.dir()

# change to " ubuntu " directory

ftp_obj.cwd("ubuntu")  # change to your desired location

print(" After change in directory : ")

print(" Present working directory is : ")

# present " ubuntu " working directory

present = ftp_obj.pwd()

print(present)

print("Content of the direcoty " + " is : ")

# content of " ubuntu " directory 

ftp_obj.dir()

# size of a file

file_size = ftp_obj.size("ls-lR.gz")

print("Size of the file ls-lR.gz is : " + str(file_size))

# change back to / directory 

print(" Go back to previous directory : [Yes/No] =  ")

answer = input()

if answer == 'Yes':
    
    print("Changed directory to : ")

    ftp_obj.cwd("/")

    present = ftp_obj.pwd()

    print(present)

elif answer == 'No':

    print("Its your rights.")

# print the welcome message

print(ftp_obj.getwelcome())

# close connection 

ftp_obj.close()
