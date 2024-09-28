import math 

def CalculateE(roundVal):

		someE = round(math.e,roundVal);
		e = str(someE)
		someList = list(e)
		return someE
	
while True:
    roundTo = input('Enter the number of digits you want after the decimal for e: ')
    try:
        roundint = int(roundTo)
        print(CalculateE(roundint))
        
        break
    
    except:
        print("You did not enter an integer")
        
        continue


