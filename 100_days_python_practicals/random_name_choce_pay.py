#import random module
import random as rn
# create a list of random names
name_list = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Gbemi",
             "Fola", "Grace", "Hakeem", "Ife","Benson", "Chidi", "Dami", "Emeka", "Funke"]
# List_name length
list_length = len(name_list)

randm_val = rn.randint(0, list_length - 1)
#person that will pay 
def pay_person():
    person_pay = name_list[randm_val]
    print(f"{person_pay} is going to buy the meal today!")

# main function
def main():
    pay_person()
    
# entry point of the script
if __name__ == "__main__":
    main()
    