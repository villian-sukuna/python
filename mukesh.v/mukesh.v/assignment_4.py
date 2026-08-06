total_patient=0
while True:
    pat_name=input("enter patient name:")
    total_patient +=1
    print("Patient registered successfully")
    next=input("do you need to register another patient: Yes or No:")
    if next=="No" or next =="no":
        break

print ("toatal patiernts:",total_patient)
