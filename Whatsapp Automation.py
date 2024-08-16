import pywhatkit as kt
import getpass as gp
#method call
#display message
print("Let's Automate WhatsApp.!!")
phone_num = gp.getpass(prompt='Phone Number (include country code, e.g., +92): ', stream=None)
#message
message = "Let's meet at book festival this Friday"
#method call
kt.sendwhatmsg(phone_num, message, 18, 24)

