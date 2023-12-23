class Item:
    pass
item1 = Item()

#attributes of instances of the class
# .instance this is how we create attributes

item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# if I print the attributes it is proove that they belong to the class:
print(type(item1)) #item
print(type(item1.name)) # str
print(type(item1.price)) # int
print(type(item1.quantity)) # int
