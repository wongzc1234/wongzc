temperature=float(input("please enter the value of temperature in celcius:"))
if temperature<=45:
    print("overheating")
elif temperature<30:
    print("cool")
else:
    print("normal")