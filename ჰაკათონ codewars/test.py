# arr = [2, 2, 1, 2, 1]

# def list(arr):
#     arr.remove(min(arr))
#     return arr

# print(list(arr))



# -------------------- 2

# def multy(a, b):
#     return a * b

# print(multy(97, 120))


# -------------------- 3

# string = "lets talk about javascript the best language"

# def length(string):
#     arr_str = string.split(" ")

#     result = []

#     for i in arr_str:
#         result.append(len(i))

#     return min(result)
# print(length(string))


# -------------------- 4

# arr = [9, 10, 19, 13, 19, 13]

# def remove(arr):
#     counter = []
#     for i in arr:
#         if arr.count(i) == 1:
#             counter.append(i)
#     return sum(counter)

# print(remove(arr))

# -------------------- 5

# ამოცანა 5.

# შექმენით ფუნქცია, რომელიც სტრინგში ამოიღებს 
# მაქსიმალურ და მინიმალურ რიცხვებს.

# test case -- ("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
# test case -- ("1 2 3"), "3 1")
    
# def sentence(str_arr):
#     result = str_arr.split()

#     f_result = []

#     for i in result:
#         f_result.append(int(i))


#     return f"{max(f_result)} - {min(f_result)}"


# print(sentence("1 2 3"))

# -------------------- 6
# ამოცანა 6.
# დაწერეთ ფუნქცია, რომელიც იღებს ორ პარამეტრს (integer, limit) 
# და უნდა გამოიტანოთ ყველა რიცხვი იქნება ყველა რიცხვი 
# integer-დან limit-მდე. თითოეული რიცხვი გაიზრდება integer-ით
# ანუ თუ (2, 8) იქნება პარამეტრები, მაშინ გამოიტანეთ [2, 4, 6, 8].

# test case -- (5, 25), [5, 10, 15, 20, 25]
# test case -- (1, 2), [1, 2])

# def ranged(integer, limit):

#     result = []

#     for i in range(integer, limit+1, integer):
#         result.append(i)
    
#     return result

# print(ranged(5, 25))
# # -------------------- 7


# ამოცანა 7.
# დაწერეთ ფუნქცია (Hashtag Generator) სადაც ცვლადის პირველი ელემენტი
# იქნება '#', შემდეგ მიუწერთ სტრინგის ყოველ სიტყვას ოღონდ 
# (Capitalize - ანუ პირველი ასო დიდი) ფორმაში.
# გამოიტანეთ False თუ სტრინგი ცარიელია.

# test case -- " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# test case -- 'c i n' => '#CIN'
# test case -- '' => False


# text = "c"
# def case_str(text):
#     text = text.split(" ")

#     result = ["#"]

#     for i in text:
#         result.append(i.capitalize())

#     return "".join(result)

# print(case_str(text))

# -------------------- 8
# ამოცანა 8.
# შექმენით ფუნქცია, რომლის საშუალებითაც გადაიტანთ
#  0-ებს მასივის ბოლო ინდექსებზე.
# მაგალითად --- ([1, 0, 1, 2, 0, 1, 3]) => [1, 1, 2, 1, 3, 0, 0]

# test case -- [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),  [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
# test case -- [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




# ამოცანა 9.
# საჩუქრად ❤️ 
# გადაიყვანეთ ამერიკული დოლარი, ჩინურ იენში.
# (ამ შემთხვევაში 6.75 ჩინური იენი => 1 ამერიკული დოლარის)
# აუცილებელია რომ წერტილის შემდეგ მეასედი იყოს ანუ (2 ციფრი)

# test case - 15  -> '101.25 Chinese Yuan'
# test case - 465 -> '3138.75 Chinese Yuan'
# test case - 178674 -> '1206049.50 Chinese Yuan'

# x = 178674
# def valute(x):
#     return x * 6.75
# print(valute(x))






acc = {
    "name": "",
    "balance": ""
}
name = input("enter name: ")

person = input(f"{name} What do you want - 'input' or 'output'? ")
balance = 1000

if person == 'input':
    amount1 = int(input("what is  amount of money: "))
    balance += amount1
    print(f"your balance {balance}$")
if person == 'output':
    amount2 = int(input("what is  amount of money: "))
    if balance < amount2:
        print("there is not enough money")
        print(f"your balance {balance}$: difference is {amount2 - balance}$")
    if balance >= amount2:
        balance -= amount2
        print(f"your balance {balance}$")



acc["name"] = name
acc["balance"] = balance


print(acc)








