### A program that takes the length of the password and generates a random password.print

import random 

passlen = int(input("Enter the length of the password = "))

s = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ!@#$%^&*()?<>{}[]1234567890"

p = "".join(random.sample(s,passlen))

print(p)

