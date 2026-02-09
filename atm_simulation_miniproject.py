user_details={1:{ "acc_no":4568,"name":"John","acc_type":"Savings Account","balance":5000,"pin":1234,"transactions":[]},
               2: {"acc_no":3568,"name":"Ram","acc_type":"Current Account","balance":1500,"pin":1001,"transactions":[]}
            }
def check_balance(user):
    print("Your balance is", user["balance"])

def mini(user):
    print("Your last transactions,")
    if not user["transactions"]:
        print("No transactions yet.")
    else:
        for txn in user["transactions"]:
            print(txn)

def withdrawal(user):
        try:
            with_amt = int(input("Enter the amount: "))
            if with_amt <= 0:
                print("Amount must be greater than zero ❌")
            elif with_amt <= user["balance"]:
                user["balance"] -= with_amt
                user["transactions"].append(f"Withdraw amount: {with_amt} | Balance: {user['balance']}")

                print("Transaction Successful ✅")
                print("Remaining balance is ₹", user["balance"])

            else:
                print("Insufficient balance ❌")
        except ValueError:
            print("Amount should be integer")

def deposit(user):
    try:
        dep_choice = int(input("Options:\n1. 500\n2. 1000\n3. 2000\nEnter your choice: "))
        if dep_choice == 1:
            user["balance"] += 500
            amount=500
            print("₹500 deposited successfully")
        elif dep_choice == 2:
            user["balance"] += 1000
            amount=1000
            print("₹1000 deposited successfully")
        elif dep_choice == 3:
            user["balance"] += 2000
            amount=2000
            print("₹2000 deposited successfully")
        else:
            print("Please enter a valid option")
            return
        #user["balance"] += with_amt
        print("Deposit successful ✅")
        print("Updated balance is ₹", user["balance"])
        user["transactions"].append(f"Deposit amount: {amount} | Balance: {user['balance']}")
        print("Deposit successful ✅")

    except ValueError:
        print("Amount value should be integer")

print("Welcome the the XYZ Atm!!")
print("Please enter your card...")

logged_user = None
attempt=0
#pin authentication
while logged_user is None and attempt < 3:
    try:
     pin = int(input("Enter your 4 digit pin:"))
     for user in user_details.values():
      if user ["pin"]==pin:
       logged_user = user
       print("Welcome",user["name"],"!!")
       print("Login Successful ✅")
       break
     else:
        attempt += 1
        print("Invalid Pin ❌")
    except ValueError:
        print("Pin should be integer!!")

if logged_user is None:
    print("Transaction attempt exceeded")
    print("Please try after 24 hours...")
    print("Please collect your card!")

else:
    while True:
        print("Menu")
        print("1.Check Balance")
        print("2.Cash Withdrawal")
        print("3.Cash Deposit")
        print("4.Mini Statement")
        print("5.Exit")
        try:
         choice = int(input("Enter your choice:"))

         if choice == 1:
              check_balance(logged_user)
         elif choice == 2:
              withdrawal(logged_user)
         elif choice == 3:
              deposit(logged_user)
         elif choice==4:
             mini(logged_user)
         elif choice == 5:
              print("Please collect your card!")
              print("Thanks for using XYZ Atm 🙏!")
              break
         else:
              print("Please enter a valid choice")
        except ValueError:
            print("Please enter integer only")

