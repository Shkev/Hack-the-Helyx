"""Takes in the following as input:
* Price of charger provider's electricity per $/kWh
* Power output of provider in kW
* Time that the user wants to charge for

Outputs:
* Price to charge the customer for charging car
"""

prov_price = 0
power = 0
time = 0

power_used = power * time

#the price the provider will have to pay
init_price = power_used * prov_price

#the price the user will pay
user_price = round(init_price * 1.2, 2)

print("Price :: %.2f" % user_price)
