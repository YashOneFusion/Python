# Create a Factory localizer
# Create different localizers which implement Factory Localizer

import base64
import binascii

class Base64:
    def __init__(self):
        print('Converting message to Base64: \n')
    def encode(self,message):
        self.message=message
        return base64.b64encode(b'{self.message}')
    
class Hex:
    def __init__(self):
         print("Converting the message to Hex code: ")
    def encode(self, message):
         self.message=(message)
         return binascii.hexlify(b'{self.message}')
        


def Factory( message, format="None"):
        if format=="None":
            print("No Format given...\n")
        elif format=="BASE64":
            print(Base64().encode(message))
        elif format=="HEX":
            print(Hex().encode(message))
        
        else:
            raise ValueError(format)

Factory("Test Sample 123")
Factory("Test Sample 123",format="HEX")

Factory("Test Sample 123",format="BASE64")
