#1 Container object
#2 Container's iter logic
#3 Iterator Object

iterList=[2,4,5,3,2,5,3,5,3]

iterator= iter(iterList)
#Implementation
while True:
    try:
        #Go to next element, starting from begining 
        item=next(iterator)
    except StopIteration:
        break
    else:
        print(item)