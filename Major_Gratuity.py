#Welcome Algorithm
print("Welcome To The Gratuity Calculator!")

#To Ask the User for Input

superannuation = (input("Are You Eligible for Superannuation? Enter Yes or No \n"))

#To check for superannuation eligibility

if superannuation == "No":
	print("Sorry,You are Not Eligible for Gratuity")

elif superannuation == "Yes":	
	retired = (input("Have You Retired? Enter Yes or No \n"))

#To check for retirement 

	if retired == "Yes":
		print("You are Eligible for Gratuity")
		#Calculator Logic
 
		Gratuity_act =input("Is your Employer Covered Under the Gratuity Act? Enter Yes or No \n")
		if Gratuity_act == "Yes":
			tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
#Check for working Years
			if tenure_of_working >=5:
				my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
				dear_allowance = float(input("How much was Dear Allowance? \n"))
				Basic = my_last_drawn_salary + dear_allowance
				Gratuity = (tenure_of_working * Basic * 15)/26

				if Gratuity <= 2000000:
					print(f"Your Gratuity is {Gratuity}")
				elif Gratuity > 2000000:
					print(f"Your Gratuity is {Gratuity}")
					Exgratia = Gratuity - 2000000
					print(f"And Your Ex-gratia is {Exgratia}")
		
				else:
					print("Please Enter a Number")

			elif tenure_of_working < 5:
				print("Sorry,You are not Eligible for Gratuity!")

			else:
				print("Please Enter a Valid Option, Yes or No")

		elif Gratuity_act == "No":
			tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
			if tenure_of_working < 5:

				print("Sorry,You are not Eligible for Gratuity")
			elif tenure_of_working >=5:
				my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
				dear_allowance = float(input("How much was Dear Allowance? \n"))
				Basic = my_last_drawn_salary + dear_allowance
				Gratuity = (tenure_of_working * Basic * 15)/30
				if Gratuity <= 2000000:
					print(f"Your Gratuity is {Gratuity}")
				elif Gratuity > 2000000:
					print(f"Your Gratuity is {Gratuity}")
					Exgratia = Gratuity - 2000000
					print(f"And Your Ex-gratia is {Exgratia}")
				else:
					print("Please Enter a Number")

			else:
				print("Please Enter a Valid Option,a Number!")


		else:
			print("Please Enter a Valid Option, Yes or No")


	elif retired == "No":
		resigned = (input("Have You Resigned? Enter Yes or No \n"))

#To check for resignation

		if resigned == "Yes":
			tenure_of_working =round(float(input("How many Years did you spend with the Company before your resignation? \n")))
#You must Input a Number here

			if tenure_of_working >= 5:
				print("You are Eligible for Gratuity")
				#Calculator Logic
 
				Gratuity_act =input("Is your Employer Covered Under the Gratuity Act? Enter Yes or No \n")
				if Gratuity_act == "Yes":
					tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
#Check for working Years

					if tenure_of_working >=5:
						my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
						dear_allowance = float(input("How much was Dear Allowance? \n"))
						Basic = my_last_drawn_salary + dear_allowance
						Gratuity = (tenure_of_working * Basic * 15)/26

						if Gratuity <= 2000000:
							print(f"Your Gratuity is {Gratuity}")
						elif Gratuity > 2000000:
							print(f"Your Gratuity is {Gratuity}")
							Exgratia = Gratuity - 2000000
							print(f"And Your Ex-gratia is {Exgratia}")
		
						else:
							print("Please Enter a Number")

					elif tenure_of_working < 5:
						print("Sorry,You are not Eligible for Gratuity!")

					else:
						print("Please Enter a Valid Option, Yes or No")

				elif Gratuity_act == "No":
					tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
					if tenure_of_working < 5:

						print("Sorry,You are not Eligible for Gratuity")
					elif tenure_of_working >=5:
						my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
						dear_allowance = float(input("How much was Dear Allowance? \n"))
						Basic = my_last_drawn_salary + dear_allowance
						Gratuity = (tenure_of_working * Basic * 15)/30
						if Gratuity <= 2000000:
							print(f"Your Gratuity is {Gratuity}")
						elif Gratuity > 2000000:
							print(f"Your Gratuity is {Gratuity}")
							Exgratia = Gratuity - 2000000
							print(f"And Your Ex-gratia is {Exgratia}")
						else:
							print("Please Enter a Number")

					else:
						print("Please Enter a Valid Option,a Number!")


				else:
					print("Please Enter a Valid Option, Yes or No")


			else:
				casualty = (input("Are You Suffering from any casualty hindering your work? Enter Yes or No \n"))
#To check for casualty

				if casualty == "Yes":
					print("You are Eligible for Gratuity")

					#Calculator Logic
 
					Gratuity_act =input("Is your Employer Covered Under the Gratuity Act? Enter Yes or No \n")
					if Gratuity_act == "Yes":
						tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
#Check for working Years

						my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
						dear_allowance = float(input("How much was Dear Allowance? \n"))
						Basic = my_last_drawn_salary + dear_allowance
						Gratuity = (tenure_of_working * Basic * 15)/26

						if Gratuity <= 2000000:
							print(f"Your Gratuity is {Gratuity}")
						elif Gratuity > 2000000:
							print(f"Your Gratuity is {Gratuity}")
							Exgratia = Gratuity - 2000000
							print(f"And Your Ex-gratia is {Exgratia}")
		
						else:
							print("Please Enter a Number")


					elif Gratuity_act == "No":
						tenure_of_working = round(float(input("How many years did you work for Your Employer? \n")))
	
	
						my_last_drawn_salary = float(input("How much was Your last Basic Salary? \n"))
						dear_allowance = float(input("How much was Dear Allowance? \n"))
						Basic = my_last_drawn_salary + dear_allowance
						Gratuity = (tenure_of_working * Basic * 15)/30
						if Gratuity <= 2000000:
							print(f"Your Gratuity is {Gratuity}")
						elif Gratuity > 2000000:
							print(f"Your Gratuity is {Gratuity}")
							Exgratia = Gratuity - 2000000
							print(f"And Your Ex-gratia is {Exgratia}")
						else:
							print("Please Enter a Number")

					else:
						print("Please Enter a Valid Option, Yes or No")



				elif casualty == "No":
					print("Sorry,You are Not Eligible for Gratuity")

				else:
					print("Please Enter a Valid Option, Yes or No")


		elif resigned == "No":
			print("Sorry,You are Not Eligible for Gratuity")

		else:
			print("Please Enter a Valid Option, Yes or No")

	else:
		print("Please Enter a Valid Option, Yes or No")
else:
	print("Please Enter a Valid Option, Yes or No")
##	print("Sorry,You are Not Eligible for Gratuity")


