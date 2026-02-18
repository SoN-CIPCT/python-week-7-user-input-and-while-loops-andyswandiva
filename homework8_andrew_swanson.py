pizza_orders = ['stephens salami','pauls pepperoni','chriss combo','pattys pasta','sammys special']
finished_pizzas = []
while pizza_orders:
    current_pizza = pizza_orders.pop()
    print(f"\n{current_pizza.title()}, your order is finished!")
    finished_pizzas.append(current_pizza)
print(f"\nThe following pizza orders have been completed:")
for pizza in finished_pizzas:
    print(f"The following pizza order: {pizza.title()}, has been made.")
