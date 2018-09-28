from gtts import gTTS
import os
from pygame import mixer
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import smtplib
coordinates = "31.712391, 76.525928"
def do_geocode(coordinates, recursion = 0):
     geolocator = Nominatim()
     try:
        
          location = geolocator.reverse(coordinates)
          return location.address
     except GeocoderTimedOut:
          if recursion > 10:     
             raise e

          time.sleep(1) 
          
          return do_geocode(coordinates, recursion=recursion + 1)
address = do_geocode(coordinates)
#print(address)

data = address.split(",")[:3]
main_addr = (', '.join(data))
print(main_addr)

tts = gTTS(main_addr, lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
filename = 'good.mp3'
mixer.init()
mixer.music.load(filename)
mixer.music.play()

spaced_message = main_addr.replace("\u012b", " ")
mail = smtplib.SMTP('smtp.gmail.com', 587)  
mail.ehlo()
mail.starttls()
mail.login('sendermailID', 'password')
mail.sendmail('sendermailID', 'receivermailID', spaced_message)
mail.close()




















