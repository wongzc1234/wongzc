temperature=float(input("please enter the value of temperature in celcius:"))
pressure=float(input("please enter the value of pressure in bar:"))
if temperature>=50 and pressure>6:
    print("alarm active")
else:
    print("alarm off")