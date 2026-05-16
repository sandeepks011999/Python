shopping_list=["Watch","Laptop","Shoes","Pen","Clothes"]
shopping_list.append("Football")
print(shopping_list[0])
print(shopping_list[-1])
print(shopping_list)
print(shopping_list[1:3])
shopping_list[3]="Notebook"
del(shopping_list[4])
print(shopping_list)


Dictionary

album_sales_dict={"The Bodyguard":50,"Back in Black":50,"Thriller":65}
album_sales_dict["Thriller"]
album_sales_dict.keys()
album_sales_dict.values()


Inventory Store

inventory={}
product_name="mobile phone"
product_quantity=5
product_price=20000
product_release_year=2020
inventory["product_name"]=product_name
inventory["product_quantity"]=product_quantity
inventory["product_price"]=product_price
inventory["product_release_year"]=product_release_year
product_name1="Laptop"
product_quantity1=10
product_price1=50000
product_release_year1=2023
inventory["product_name1"]=product_name1
inventory["product_quantity1"]=product_quantity1
inventory["product_price1"]=product_price1
inventory["product_release_year1"]=product_release_year1
print(inventory)
print("product_release_year" in inventory)
print("product_release_year1" in inventory)

conditioning and branching

player_name="Lionel Messi"
sport="soccer"
achievements=7
if achievements>10:
    print(f"{player_name} plays {sport} and has {achievements} achivements.")
else:
    print(f"{player_name} does not have more than 10 achievements.")
player_name="Roger Federer"
sport="Tennis"
achievements=20
if sport=="Tennis" or achievements==20:
    print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria")
player_name="Ussain bolt"
sport="Athletics"
achievements=8
if achievements<10 and sport!="scoccer":
    print(f"{player_name} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player_name} does not meet the criteria.")
