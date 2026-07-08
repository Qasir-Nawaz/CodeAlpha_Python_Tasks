# Simple Parking System
parking_slots = {}  # Dictionary to store slot:car_number
total_income = 0
fee = 50

while True:
    print("\n1: Add Park car")
    print("2: View Parking")
    print("3: Remove Parking")
    print("4: Total income")
    print("5: Exit")
    
    choice = input("Select an option: ")

    if choice == '1':
        slot = input("Enter Slot Number: ")
        car = input("Enter Car Number: ")
        parking_slots[slot] = car
        print("Car added successfully!")

    elif choice == '2':
        print("\nParking List:", parking_slots)

    elif choice == '3':
        slot = input("Enter Slot Number to remove: ")
        if slot in parking_slots:
            del parking_slots[slot]
            total_income += fee
            print("Car removed. Fee collected.")
        else:
            print("Slot is empty!")

    elif choice == '4':
        print("Total Income:", total_income)

    elif choice == '5':
        break