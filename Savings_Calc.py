print("Savings Calculator")
from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def sav(x):
	return x
savs = interact(sav, x=1000000)
#print("Savings Calculator")
Amount_of_Savings = input("What is The Savings Amount? \n {savs}")

def rat(y):
	return y
rats = interact(rat, y=50)

Rate_of_Inv = input("What is the Rate of Return on the Investment (P.A) ? \n {rats}")
month_rate_of_Inv = (Rate_of_Inv/100)/12
Duration_of_Inv = float(input("What is the Duration of the Investment? \n"))
month_duration_of_Inv = Duration_of_Inv * 12
monthly_EMI = (Amount_of_Savings * month_duration_of_Inv *(( 1 + month_duration_of_Inv)**12))/(( 1 + month_duration_of_Inv)**12 - 1)
print(f"The Amount to Save and Invest each Month to achieve your Desired Goal is {monthly_EMI}")