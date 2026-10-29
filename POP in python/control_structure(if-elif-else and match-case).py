#learn about control structure in python!
print("___________ E-mail _____________")
username = input("Enter username: ")
passwords = input("Enter the passwords: ")

if(username == "Tha Sothea" and passwords == "Thea123"):
    print("Login Success.")
elif(username != "Tha Sothea" and passwords == "Thea123"):
    print("Login Fail.")
elif(username == "Tha Sothea" and passwords != "Thea123"):
    print("Login Fail.")
else:
    print("Login Fail.") 
    
day = "Saturday" or "Sunday"
age = 10
ticket_price = 0

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        if age < 12:
            ticket_price = 6
        else:
            ticket_price = 10
            
    case "Saturday" | "Sunday":
        ticket_price = 12
        
    case _:
        print("it's not true")

print(f"Ticket Price: ${ticket_price}")

age1 = 20
has_license = True
drunk = True

if(age1 >= 18 and has_license and not drunk):
    print("They can drive.")
else:
    print("They cannot drive!")
    
total_amount = 60       # ចំនួនទឹកប្រាក់ទិញអីវ៉ាន់
is_vip = False          # ស្ថានភាពសមាជិក VIP
day = "Sunday"          # ថ្ងៃទិញអីវ៉ាន់

# ចូរបំពេញលក្ខខណ្ឌក្នុង if ខាងក្រោមនេះ៖
if(total_amount >= 50 and (is_vip == True or day == "Saturday" or day == "Sunday")):
    print("They will discount for you 15%!")
else:
    print("They won't discount for you!.")
    
    
age2 = int(input("How old are you?: "))
has_license = input("Do you have license?(Yes, i do. or No): ")
atm_bank = input("Have you created the card ATM Bank yet?(I'm already created): ")

if(age2 >= 18 and has_license == "Yes, i do." and atm_bank == "I'm already created"):
    print("You can go to trip.")
else:
    print("You cannot join!.")

print("---< Control structure: match-case >---")
day2 = int(input("Choose the day that you're free time: "))
answer2 = "=> I'm free time on"
match day2:
    case 1:
        print(f"{answer2} Monday")
    case 2:
        print(f"{answer2} Tuesday")
    case 3:
        print(f"{answer2} Wednesday")
    case 4:
        print(f"{answer2} Thursday")
    case 5:
        print(f"{answer2} Friday")
    case 6:
        print(f"{answer2} Saturday")
    case 7:
        print(f"{answer2} Sunday")

day3 = str(input("choose the day that you wanna come here: "))
age3 = int(input("How old are you?: "))
ticket_price3 = 0
match day3:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        if(age3 <= 12):
            ticket_price3 = 6
        else:
            ticket_price3 = 12
    case "Saturday" | "Sunday":
        ticket_price3 = 12
print(f"You're {age3}. You wanna come here on {day3}. So the price of ticket is ${ticket_price3}")