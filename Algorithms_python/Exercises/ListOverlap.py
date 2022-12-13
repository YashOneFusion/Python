#Compare two randomly generated lists and return elements which occur in both lists
import random
def listOverlap(): 
    finalList = []
    listA = []
    listB = []
    sizeRangeA = random.randint(1,10)
    sizeRangeB = random.randint(1,10)    
    #Generating random values for listA
    for x in range(sizeRangeA):
        listA.append(int(random.randint(1,100)))
    #Generating random values for listA
    for x in range(sizeRangeB):
        listB.append(int(random.randint(1,100)))
    #Generating elements which occurred twice or more
    for i in listA:
        for j in listB:
            if j == i:
                finalList.append(j)
            else:
                continue
    print(f'List A is :{listA}')
    print(f'List B is :{listB}')
    print(f'Occurences of Similar elements: {finalList}')


print(listOverlap())