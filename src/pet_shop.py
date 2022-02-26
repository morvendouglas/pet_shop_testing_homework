
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
        return pet_list
    return 0

def get_pets_by_name(pet_shop, name):
    pet_list = []
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_list.append(pet)
    return pet_list

def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

def add_pet_to_stock(pet_shop, pet_added):
    pet_shop["pets"].append(pet_added)

def get_customer_cash(customers):
        return customers["cash"]

def remove_customer_cash(customers, cash):
        customers["cash"] -= cash

def get_customer_pet_count(customers):
        return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
