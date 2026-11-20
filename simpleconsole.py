TOTAL_SLOTS = 5
parking_slots = []
FEE_PER_HOUR = 20
while True:
    print("\n===== PARKING MANAGEMENT SYSTEM =====")
    print("1. Park Vehicle")
    print("2. View Parked Vehicles")
    print("3. Remove Vehicle")
    print("4. Search Vehicle")
    print("5. Available Slots")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        if len(parking_slots) < TOTAL_SLOTS:
            vehicle = input("Enter vehicle number: ")

            if vehicle in parking_slots:
                print("Vehicle already parked")
            else:
                parking_slots.append(vehicle)
                print("Vehicle parked successfully")

        else:
            print("Parking is full!")

    elif choice == "2":

        if len(parking_slots) == 0:
            print("No vehicles parked.")
        else:
            print("Parked Vehicles:")
            for vehicle in parking_slots:
                print(vehicle)

    elif choice == "3":

        vehicle = input("Enter vehicle number: ")

        if vehicle in parking_slots:
            parking_slots.remove(vehicle)
            print("Vehicle removed successfully")

            hours = int(input("Enter parking hours: "))
            fee = hours * FEE_PER_HOUR

            print("Parking Fee: Rs.", fee)
        else:
            print("Vehicle not found")

    elif choice == "4":

        vehicle = input("Enter vehicle number: ")

        if vehicle in parking_slots:
            print("Vehicle is parked.")
        else:
            print("Vehicle not found!")

    elif choice == "5":

        available = TOTAL_SLOTS - len(parking_slots)

        print("Total Slots:", TOTAL_SLOTS)
        print("Occupied Slots:", len(parking_slots))
        print("Available Slots:", available)

    elif choice == "6":
        print("Thank you for using Parking Management System")
        break

    else:
        print("Invalid choice! Try again.")