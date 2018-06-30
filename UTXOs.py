import random
import time
from datetime import datetime
from datetime import timezone
class TransactionOutput:


    def __init__(self):
    
        self.year = random.choice(range(2008, 2017))
        self.month = random.choice(range(1, 13))
        self.day = random.choice(range(1, 29))
        self.date = datetime(self.year, self.month, self.day)
        self.date = self.date.replace(tzinfo=timezone.utc).timestamp()
        
        #create random date 
        
        self.value = round(random.uniform(0,1),8)
    
        #create random value from 0 to 1

UTXOs = []


#create UTXOs and sort them in terms of date
for i in range(random.choice(range(6,13))):
    transaction = TransactionOutput()
    if len(UTXOs) == 0:
        UTXOs.append(transaction)

    else:
        for k in range(len(UTXOs)):
            if transaction.date < UTXOs[k].date:
                UTXOs.insert(k,transaction)
                break
            if k+1 == len(UTXOs):
                UTXOs.append(transaction)
                
    
    

#print UTXOs date and value
print ("Dates of UTXOs:")

for x in range(len(UTXOs)):
    print (UTXOs[x].date)

print ("Values of UTXOs:")

for x in range(len(UTXOs)):
    print (UTXOs[x].value)
print ("----------")


#outputs an optimal date range given amount of BTC being sent

def findrange(UTXOs,x):
    optimalOutputSums = 0
    counter = 0
    while optimalOutputSums<x:
        
        optimalOutputSums = optimalOutputSums + UTXOs[counter].value
        counter += 1
        
    optimalStartIndex = 0
    optimalEndIndex = counter-1
    '''
    Iterate through UTXOs starting from the oldest one
    until the cumulative value of outputs is
    greater than amount of BTC being sent. This creates a baseline date range.
    '''
   
    for i in range(0,len(UTXOs)):
#iterate through starting points and end points searching for optimal date range
        
        tempEndIndex = optimalEndIndex
        
        if (i > tempEndIndex):
            tempEndIndex = i
        outputSums = 0
        while outputSums < x and tempEndIndex < len(UTXOs):
            outputSums = rangeValue(UTXOs, i, tempEndIndex)
            tempEndIndex += 1
            
        if outputSums < optimalOutputSums and outputSums > x:
            optimalOutputSums = outputSums
            optimalStartIndex = i
            optimalEndIndex = tempEndIndex-1

    #print optimal date range

    print ("Optimal output: " + str(optimalOutputSums))
    print ("Optimal date range is from " + str(UTXOs[optimalStartIndex].date) + 
           " to " + str(UTXOs[optimalEndIndex].date))
   

def rangeValue(UTXOs, startIndex, endIndex):

    #given a range find the cummalivate sum of all the outputs in that range

    rangeValue = 0
    counter = startIndex
    while counter < endIndex+1:
        rangeValue = rangeValue + UTXOs[counter].value
        counter += 1
        
        
    return rangeValue

def getInput():

    totalSum = rangeValue(UTXOs, 0, len(UTXOs) -1)
    value = input("How much BTC do you want to send? The most you can send is " +
              str(totalSum)+  '\n')

    if (float(value) > totalSum):
        print("You do not have enough BTC to make this transaction")
        getInput()
    elif (float(value) == 0):
        print("You can not send 0 BTC")
        getInput()
    findrange(UTXOs,float(value))
    
  
#get user input for amount of BTC being sent

getInput()
