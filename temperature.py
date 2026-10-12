pressure=float(input("please enter the value of pressure in bar:"))
temperature=float(input("please enter the value of temperature in celcius:"))

if temperature>50 or pressure>6:
    status="critical"
elif temperature>=40 or pressure<2:
    status="warning"
else:
    status="normal"

print("Temperature:",temperature,"degree C")
print("Pressure:",pressure,"bar")
print("machine Status",status)

