

balance = 1000
acc = {}
name = input("enter name: ")

i = 2
while i > 1:
    person = input(f"{name} What do you want - 'in' or 'out'? ")
    if person == 'in':
        amount1 = int(input("what is  amount of money: "))
        balance += amount1
        print(f"your balance {balance}$")
    if person == 'out':
        amount2 = int(input("what is  amount of money: "))
        if balance < amount2:
            print("there is not enough money")
            print(f"your balance {balance}$: difference is {amount2 - balance}$")
        if balance >= amount2:
            balance -= amount2
            print(f"your balance {balance}$")

    upgrade = input("do you want continue: ")
    if upgrade == 'yes':
        i -= 0
    if upgrade == 'no':
        i -= 1

    acc = dict(name = name, balance = balance) 
    print(acc)













