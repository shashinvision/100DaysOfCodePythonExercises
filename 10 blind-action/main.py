from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo


done = False

list = []

while not done:
    print(logo)
    name = input("Name: ")
    bid_price = int(input("Bid Price: "))

    dict = {
        "name": name,
        "bid_price": bid_price
    }
    
    ask_again = input("Do you want to add another bid? yes/no: ")
    if ask_again != "no":
        done = False
        clear()
    else:
        done = True

    list.append(dict) 
    
# print(list)

bigest = {"name": "", "bid_price":0}
minus = {"name": "", "bid_price":999999999}
for person in list:
    if person['bid_price'] > bigest["bid_price"]:
        bigest["name"] = person['name']
        bigest["bid_price"] = person['bid_price']
    
    if person["bid_price"] < minus['bid_price']  :
        minus["name"] = person['name']
        minus["bid_price"] = person['bid_price']
    
# If only need max or min value 
# max_bid = max(person['bid_price'] for person in list)
# min_bid = min(person['bid_price'] for person in list)

print(f"The Lose is: {minus['name']} with  {minus['bid_price']}")
print(f"The Winner is: {bigest['name']} with  {bigest['bid_price']}")