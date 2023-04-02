import phonenumbers
from phonenumbers import timezone , geocoder ,carrier

number = input("Enter phone number : ")
phone = phonenumbers.parse(number, None)

time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone , "en")
reg = geocoder.description_for_number(phone,"en")

print("Number : " , phone)
print({"TimeZone" : car,"Company" :car ,"Region" : reg})