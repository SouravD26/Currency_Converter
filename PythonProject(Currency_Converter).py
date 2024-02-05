#-------------------------------------------------------------------------------
# Name:       Sourav Dutta
# Purpose:    Project
#
# Author:      DELL PC
#
# Created:     24-01-2024
# Copyright:   (c) DELL PC 2023
#------------------------------------------------------------------------------
import requests

# User input
amount = float(input("Enter The Amount --  "))
currency = input("Enter The Currency to Convert to -- ")

# Currency Exchange
exchange_market = requests.get("https://api.exchangerate-api.com/v4/latest/INR")
exchange_rate = exchange_market.json()["rates"]
convert_amount = amount * exchange_rate[currency]

# Print the converted Amount
print(f"{amount} is convert to {convert_amount} {currency}")

