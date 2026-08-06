products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Keyboard"]
categories = ("Computers", "Mobiles", "Audio", "Wearables", "Accessories")
product_price = {
    "Laptop": 65000,
    "Smartphone": 25000,
    "Headphones": 3000,
    "Smartwatch": 7000,
    "Keyboard": 1500
}
brands = {"Dell", "Samsung", "Sony", "Boat", "Logitech"}
product_category = {
    "Laptop": "Computers",
    "Smartphone": "Mobiles",
    "Headphones": "Audio",
    "Smartwatch": "Wearables",
    "Keyboard": "Accessories"
}
product_brand = {
    "Laptop": "Dell",
    "Smartphone": "Samsung",
    "Headphones": "Sony",
    "Smartwatch": "Boat",
    "Keyboard": "Logitech"
}
def get_product(product):
    if product in product_price:
        return product, product_price[product]
    else:
        return None, None
discount = lambda price: price - (price *10/100)
print("all product name:",products)
user_product = input("Enter Product Name:")
product, price = get_product(user_product)

if product == user_product:
    print("\n===== PRODUCT DETAILS =====")
    print("Product Name   :", product)
    print("Category       :", product_category[product])
    print("Original Price : ₹", price)
    print("Discount Price : ₹", discount(price))
    print("Brand          :", product_brand[product])
else:
    print("Product not found!")