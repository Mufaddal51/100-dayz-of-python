print("Welcome to tip caculator")
bill=float(input("what was the total bill"))
tip=int(input("How much tip would you like to give 10, 12 or 15"))
num=int(input("How many peoples to split the bill "))
total=bill*(tip/100)+bill
total_num=total/num
totalbill=float(round(total_num,2))
print("Each person should pay :"+str(totalbill))
