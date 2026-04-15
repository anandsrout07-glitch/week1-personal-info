#Personal Informaion Manger
#My 1st week task(Anand Sagar Rout)

#Variables for personal information
print("="*40,"\nEnter Your Personal Information\n","="*40)
name=input("\nEnter Your Name: ")
age=int(input("Enter Your Age: "))
city=input("Enter your city name: ")
hobby=input("Enter your hobby: ")

#User input for more information
print("="*40,"\nTell me about your self\n","="*40)
favorite_food=input("What's Your Favorite food: ")
while favorite_food=="":
    print("Please Enter Valid Food!")
    favorite_food=input("What's Your Favorite food: ")

favorite_color=input("What's your favorite color: ")
while favorite_color=="":
    print("Please Enter Valid color: ")
    favorite_color=("What's your favorite color: ")


#Calculating age in months
age_in_months=age*12

#Display Personal INFORMATION
print("="*30,"\nYour Personal Information\n","="*30)

print(f"Name:{name}")
print(f"Age:{age} ({age_in_months}month old)")
print(f"Hobby:{hobby}")
print(f"City:{city}")

print(f"\nFavorite Food:\n{favorite_food}")
print(f"Favorite Color:\n{favorite_color}")
print()

print("="*40,"\nThanks for using this programm\n","="*40)




