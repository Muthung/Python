### Get information about a phone number ###
### Country name                         ###
### Network provider                     ###
### Geocoder : to know the location      ###

import phonenumbers

from phonenumbers import geocoder

from phonenumbers import carrier

# for time zone names

from phonenumbers import timezone

# from phone_iso3166.country import *

input_number = input("Enter the phone number : ")

phone_number = phonenumbers.parse(input_number)

carrier_number = phonenumbers.parse(input_number)

tz_number = phonenumbers.parse(input_number)

print(geocoder.description_for_number(phone_number, 'en'))

print(carrier.name_for_number(carrier_number, "en"))

print(timezone.time_zones_for_number(tz_number))

# print(phone_country(input_number))