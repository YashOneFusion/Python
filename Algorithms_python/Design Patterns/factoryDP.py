# Create a Factory localizer
# Create different localizers which implement Factory Localizer

# {--Currently Under Construction--}
import base64
import binascii

class Base64:
    def __init__(self):
        print('Encoding to Base64: \n')
    def encode(self,message):
        self.message=message
        return base64.b64encode(self.message)
    
class Hex:
    def __init__(self):
        print('Encoding to Hex: \n')
    def encode(self, message):
         self.message=(message)
         return binascii.hexlify(b'{self.message}')
        


def Factory(format, message):
        if format=="BASE64":
            Base64().encode(message)
        elif format=="HEX":
            Hex().encode(message)
        else:
            raise ValueError(format)

Factory('BASE64', "This is a certified test")
