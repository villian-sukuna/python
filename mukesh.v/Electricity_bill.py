print("Welcome To Smart Electricity Bill Management System")
customer_list = []
while True:
    customer_name=input("Enter the Customer name:")
    customer_list.append(customer_name)
    customer_id=int(input("Enter the customer id:"))
    customer_type=int(input("choose the custer type:\n1.Domestic\n2.Commercial\n3.Industrial\n"))
    current_mtr_red=float(input("enter the current meter reading:"))
    previous_mtr_red=float(input("enter the previous meter reading:"))

    unit_cons= current_mtr_red - previous_mtr_red

    if current_mtr_red < previous_mtr_red or unit_cons < 0:
        print("INVALID READING")
        break

    bill=0

    if 0<=unit_cons<=100:
        bill=unit_cons*2
    elif 100<unit_cons<=300:
        bill=unit_cons*3.5
    elif 300<unit_cons:
        bill=unit_cons*5

    match customer_type:
        case 1:
            print("the customer type is domestic")
        case 2:
            print("the customer type is commercial")
        case 3:
            print("the customer type is Industrial")
        case _:
            print("INVALID CUSTOMER TYPE choose the correct customer type")

    discount=0
    if bill>=1000:
        discount=bill*(10/100)
        print("Discount applied for 10%=",discount)
    else:
        print ("no discount")
    ch = input("Do you want add a another customer (yes or no): ")
    if ch =="no":
        print("Thanks you for your cooporation Here is your bill")
        break

for i in customer_list:
    print("Customer name:",i)