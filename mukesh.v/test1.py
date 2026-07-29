mobiles = {
    "01": {
        "mob_id": "01",
        "model": "Vivo Y28",
        "ram": "4 GB",
        "category": "Budget",
        "price": 14999,
        "quantity": 10,
        "features": "5000mAh Battery, 50MP Camera",
        "rating": 4.2
    },
    "02": {
        "mob_id": "02",
        "model": "Realme Narzo 70",
        "ram": "8 GB",
        "category": "Mid Range",
        "price": 18999,
        "quantity": 8,
        "features": "120Hz Display, 5000mAh Battery",
        "rating": 4.5
    },
    "03": {
        "mob_id": "03",
        "model": "iQOO Z9",
        "ram": "6 GB",
        "category": "Gaming",
        "price": 19999,
        "quantity": 6,
        "features": "Dimensity 7200, AMOLED Display",
        "rating": 4.6
    },
    "04": {
        "mob_id": "04",
        "model": "Samsung Galaxy M35",
        "ram": "8 GB",
        "category": "Premium",
        "price": 24999,
        "quantity": 5,
        "features": "6000mAh Battery, AMOLED Display",
        "rating": 4.7
    },
    "05": {
        "mob_id": "05",
        "model": "Redmi Note 13",
        "ram": "8 GB",
        "category": "Mid Range",
        "price": 17999,
        "quantity": 12,
        "features": "108MP Camera, AMOLED Display",
        "rating": 4.4
    }
}

def display_mobiles():
    if len(mobiles) == 0:
        print("No Mobiles Available")
    else:
        for mobile in mobiles.values():
            for key, value in mobile.items():
                print(f"{key.capitalize()} : {value}")

def search_mobile():
    mob_id = input("Enter Mobile ID: ")

    if mob_id in mobiles:
        print("\nMobile Found")
        for key, value in mobiles[mob_id].items():
            print(f"{key.capitalize()} : {value}")
    else:
        print("Mobile Not Found")

def update_price():
    mob_id = input("Enter Mobile ID: ")

    if mob_id in mobiles:
        print("Current Price:", mobiles[mob_id]["price"])
        new_price = float(input("Enter New Price: "))
        mobiles[mob_id]["price"] = new_price
        print("Price Updated Successfully")
    else:
        print("Mobile Not Found")
def delete_mobile():
    mob_id = input("Enter Mobile ID: ")

    if mob_id in mobiles:
        del mobiles[mob_id]
        print("Mobile Deleted Successfully")
    else:
        print("Mobile Not Found")

def show_discount():
    mob_id = input("Enter Mobile ID: ")

    if mob_id in mobiles:
        discount = float(input("Enter Discount %: "))
        price = mobiles[mob_id]["price"]

        final_price = price - (price * discount / 100)

        print("Original Price :", price)
        print("Discounted Price :", final_price)
    else:
        print("Mobile Not Found")

def string_operations():
    mob_id = input("Enter Mobile ID: ")

    if mob_id in mobiles:
        model = mobiles[mob_id]["model"]

        print("Original :", model)
        print("Upper    :", model.upper())
        print("Lower    :", model.lower())
        print("Length   :", len(model))
        print("Replace  :", model.replace(" ", "_"))
    else:
        print("Mobile Not Found")

while True:

    choice = int(input("""
========= MOBILE STORE =========

1.Display All Mobiles
2.Search Mobile
3.Update Mobile Price
4.Delete Mobile
5.Show Discount
6.String Operations
7.Exit

Enter Choice: """))

    match choice:

        case 1:
            display_mobiles()

        case 2:
            search_mobile()

        case 3:
            update_price()

        case 4:
            delete_mobile()

        case 5:
            show_discount()

        case 6:
            string_operations()

        case 7:
            print("Thank You...")
            break

        case _:
            print("Invalid Choice")