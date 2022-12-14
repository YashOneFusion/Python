import base64

#Target
class Target:
    def translate(self):
        return "Connect to Adapter"
#Adaptee
class Adaptee:
    def message(self):
        return 'aGVsbG8gd29ybGQ='
#Adapter
class Adapter(Target, Adaptee):
    def translate(self):
        return base64.b64decode(self.message())

# Creating client code
def client(target: Target):
    print(target.translate())

if __name__=='__main__':
    tg = Target()
    client(tg)
    print('\n')
    adaptee=Adaptee()
    print(f'Adaptee: without adapter: {adaptee.message()}')
    print('\nUsing Adapter now :\n')
    adapter = Adapter()
    client(adapter)
