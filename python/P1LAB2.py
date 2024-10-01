# CTI 110
# P1lAB2 - Receipt
#CYBER HANK
# 10/1/24

print("P1LAB2")
# For today, let's do a resturaunt
# that only sells burgers and fries

# declare our variables
num_burgers = 0
num_fries = 0
burger_cost = 4.99
fry_cost = 0.99

#if the custy doesn't just want burgers and fries

answer = input("Can I take your oder? (yes/no)")

if answer == "yes":
    print("only burgers and fries")
if answer=="no":
    print("Then have a nice day! exit()")



# we have to convert their input to an int
num_burgers = int(input("How many burgers?"))

print("You ordered", num_burgers, "burgers")

num_fries = int(input("How many fries?"))
print("Ok,that's", num_fries,"french fries.")

#Add up all the totals
burger_total = num_burgers * burger_cost
fry_total = num_fries * fry_cost
meal_total = burger_total + fry_total

# print the receipt
print("_" * 20)
print(num_burgers,"\t$", burger_total)
print(num_fries,"fry\t\t$",fry_total)
print("Total\t\t$", meal_total)
