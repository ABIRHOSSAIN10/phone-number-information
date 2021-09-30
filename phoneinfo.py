import phonenumbers,os
try:
     import phonenumbers
except:
      os.system("pip install phonenumbers")
os.system("xdg-open https://www.facebook.com/profile.php?id=100051548076449")
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import length_of_geographical_area_code
cyan='\033[1;96m'
green='\033[1;92m'
red='\033[1;92m'
os.system('clear')
logo=("""\033[1;91m
\033[1;91m  _____      _____ _   _ ______ ____  
\033[1;91m |  __ \    |_   _| \ | |  ____/ __ \ 
\033[1;91m | |__) |_____| | |  \| | |__ | |  | |
\033[1;91m |  ___/______| | | . ` |  __|| |  | |
\033[1;91m | |         _| |_| |\  | |   | |__| |
\033[1;91m |_|        |_____|_| \_|_|    \____/ 
                                      
	\033[1;94mAuthor:ABIR HOSSAIN                                     
""")
print(logo)
jp=("\033[1;95mif you give any space or rong number you get error")
print()
def menu():
	phoneNumber = phonenumbers.parse(input("\033[1;92mENTER NUMBER \033[1;97m :"))
	print(red+"__________________________________________________________________")
	print(cyan+"|parse.phonwnumber \033[1;93m: "+str(phoneNumber))
	print(red+"__________________________________________________________________")
	print(cyan+"|country \033[1;93m:" +geocoder.description_for_number(phoneNumber,'en'))    
	print(red+"__________________________________________________________________")
	timeZone = timezone.time_zones_for_number(phoneNumber)
	print(cyan+"|timezone \033[1;93m:"+str(timeZone))
	print(red+"__________________________________________________________________")
	from phonenumbers import carrier
	valid = phonenumbers.is_valid_number(phoneNumber) 
	print(cyan+"|oparetor name \033[1;93m:"+str(carrier.	name_for_number(phoneNumber,'en')))
	print(red+"__________________________________________________________________")
	print(cyan+"|country code \033[1;93m:"+str(phoneNumber.country_code))
	print(red+"__________________________________________________________________")
	print(cyan+"|national number \033[1;93m:"+str(phoneNumber.							national_number))
	print(red+"__________________________________________________________________")
	print(cyan+"|number valid \033[1;93m:"+str(valid))
	print(red+"__________________________________________________________________")
	print(cyan+"|possible number \033[1;93m:"+str(phonenumbers.is_possible_number(phoneNumber)))
	print(red+"__________________________________________________________________")
	print(cyan+"|region code \033[1;93m:"+str(phonenumbers.region_code_for_number(phoneNumber)))
	print(red+"__________________________________________________________________")
	print()
	input("Back")
	os.system("clear")
	print(logo)
	print()
	print(jp)
	menu()
if __name__ == '__main__':
	menu()
