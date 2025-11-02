import random as rn

#Capture integer input from user
val =int(input("Enter an integer value: "))

# Function to generate random value and check condition
def ran_val_check(val):
    ran_val = rn.randint(1, 1000)
    ran_final = ran_val + val
    print(f"final val is : {ran_final}")
    print(f"random value predicted is : {ran_val}")
    print(f"User value entered is : {val}")
    if ran_final > 500:
        print("The final value is greater than 500.")
    else:
        print("The final value is 500 or less.")
# Main function to call the check function
def main():
    ran_val_check(val)

# Entry point of the script
if __name__ == "__main__":
	main()