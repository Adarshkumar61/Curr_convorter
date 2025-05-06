import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
req = requests.get(url)
rates = req.json()["rates"] 
amount = float(input("Enter the amount in USD: "))
currency = input("enter the cdoe of country (USD, INR..): ").upper()
if currency in rates:
    print(f"{amount}USD = {amount * rates[currency]} {currency}")
else:
    print("not avaliable right now soon....") 