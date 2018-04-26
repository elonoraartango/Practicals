
item_count = 0
total_items = item_count + 1

total_items = int(input("Number of items"))
if total_items < 0:
    print("Invalid number of items")
for i in range(total_items):
    item_price = float(input("Price of item {}:".format(i+1)))
if total_items >= 100:
    print("Total price for", total_items, "items is ${:.2f}".format(item_price-item_price * .09))
else:
    print("Total price for", total_items, "items is ${:.2f}".format(item_price+total_items))
