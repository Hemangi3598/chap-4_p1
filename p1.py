# amount > 250 --> 10 % , amount > 150 ---> 5 % else no discount
actual_amount = int(input("enter your amount "))

if actual_amount <= 0:
	print(" invalid amount")
elif actual_amount > 250:
	final_amount = actual_amount * 0.90
	print(" final_amount = ", final_amount)
elif actual_amount > 100:
	final_amount = actual_amount * 0.95
	print(" final_amount = ", final_amount)
else:
	print("final amount = ", actual_amount)

