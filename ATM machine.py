#ATM Machine
account={"402590":["user_1",5000,2580],
             "939200":["user_2",2500,9999],
             "965236":["user_3",1500,9000],
             "954238":["user_4",7000,2002],
             "955346":["user_5",6000,9876]}

print("*******************")
print("Welcome to the ATM")
print("*******************")

max_attempts=3
attempt=1
print("Insert the card....")
user_account=input("Enter the account number: ")
while attempt96<+max_attempts:
    user_pin=int(input("Enter the pin"))
    if user_pin==account[user_account][-1]:
        print("Correct Pin.Please proceed with transcation")
        break
    else:
         attempt+=1
         remaining_attempts=max_attempts-attempt

         if remaining_attempts==0:
             print("Account locked. Visit the branch")
             break
    
while True:
    print("Choose an option:\n"\
          "1.Deposit\n"\
          "2.Withdraw\n"\
          "3.Check balance\n"\
          "4.Transaction History\n"\
          "5.Pin change\n"\
          "6.Exit")
    option = int(input("Enter your choice:"))
    if option == 1:
        amount = int(input("Enter the amount you want to deposit:"))
        account[user_account][1] += amount
        transaction_list.append(f"Deposited Rs.{amount}")
    elif option == 2:
        amount = int(input())
        if amount > account[user_account][1]:
            print("Insufficient funds")
        else:
            transaction_pin=int(input("Enter your transcation PIN:"))
            if transacation_pin == accounts[user_account][-1]:
                accounts[user_account][1] -= amount
                transaction_list.append(f"withdraw Rs.{amount}")
            
    elif option == 3:
         print(account[user_account][1])

    elif option == 4:
         if transcation_list:
             n=len(transcation_list)
             if n<3:
                 print(transcation_list)
             else:
                 print("No transcation yet")
     
    elif option == 5:
         current_pin =int(input("please enter your current pin:"))
         if current_pin == account[user_account][-1]:
            new_pin = int(input("Enter new pin::"))
            confirm_pin = int(input("Confirm the pin"))
            if new_pin == confirm_pin:
                accounts[user_account][-1] = new_pin
                print("pin chsnged")
            else:
                print("Incorrect Pin")
    elif option == 6:
         print("Thank you visit again")
         break
else:
    print("Please enter  a valid input")
if uaer_account not in account:
    print("Account doesn't exist")
     
