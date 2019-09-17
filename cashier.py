items_list = []
dic = {}
total_price = 0
enter_item = input('Item (enter "done" when finished): ')
while enter_item.lower() != 'done':
  price = input("Price: ")
  quantity = input("Quantity: ")
  items_list.append({'name': enter_item, 'price': price, 'quantity': quantity})
  enter_item = input('Item (enter "done" when finished): ')
print(items_list)
print("\n-------------------\nreceipt\n-------------------")
for dictionary in items_list:
  total_price += int(dictionary['quantity'])*float(dictionary['price'])
  print("{} {} {}KD".format(dictionary['quantity'], dictionary['name'], int(dictionary['quantity'])*float(dictionary['price'])))
print("-------------------\nTotal Price: {}".format(total_price))


