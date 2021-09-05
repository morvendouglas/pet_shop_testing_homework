# WRITE YOUR FUNCTIONS HERE


# NUMBER 1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

# NUMBER 2 
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# NUMBER 3 failed
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash
    
# NUMBER 4 failed
def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] -= cash

# NUMBER 5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# NUMBER 6
def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num
     
# NUMBER 7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#  NUMBER 8 failed
def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

# NUMBER 9
def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
        return pet_list
    return 0

#   NUMBER 10
def get_pets_by_name(pet_shop, name):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_list.append(pet)
    return pet_list

#  NUMBER 11
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

# NUMBER 12 error
def remove_pet_by_name(pet_shop, name):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_list.pop(pet)
    return pet_list

# NUMBER 13
def add_pet_to_stock(pet_shop, pet_added):
    pet_shop["pets"].append(pet_added)

#  NUMBER 14
def get_customer_cash(customers):
        return customers["cash"]

# NUMBER 15
def remove_customer_cash(customers, cash):
        customers["cash"] -= cash

# NUMBER 16
def get_customer_pet_count(customers):
        return len(customers["pets"])

# NUMBER 17
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)


#  Extention

# NUMBER 18 failed
def customer_can_afford_pet(pet_shop, customers):
    for pet in pet_shop["pets"]:
        if pet["price"] <= customers["cash"]:
            return True

# NUMBER 19 failed
def customer_can_afford_pet(pet_shop, customers):
    for pet in pet_shop["pets"]:
        if pet["price"] >= customers["cash"]:
            return False

#  NUMBER 20 failed
def customer_can_afford_pet(pet_shop, customers):
    for pet in pet_shop["pets"]:
        if pet["price"] == customers["cash"]:
            return True

    


        



            


    



