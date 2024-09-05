firstPriceDollars = 0.07633
secondPriceDollars = 0.09259

#Asking for the hours used
hoursUsed=int(input("Enter an integer greater than zero representing the kilowatt hours used: "))

#If conditional to difference between the ones that are > or < 1000
if(hoursUsed < 1000):
    hoursUsed = (hoursUsed * firstPriceDollars)

elif(hoursUsed > 1000):
    limitHours = 1000 * firstPriceDollars
    extraHours= (hoursUsed - 1000) * secondPriceDollars
    hoursUsed = limitHours + extraHours

print("Amount owed is", "$", "%.2f" % hoursUsed)
