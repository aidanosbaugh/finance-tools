capital = float(input("Starting Amount"))
return_rate = float(input("Yearly Return"))
years = int(input("How many years?"))
future_value = capital * (1 + return_rate/100) ** years
print(f"Your investment becomes {future_value:.2f}")