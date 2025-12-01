from collections import deque

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()

    def arrive(self, car_id):
        if len(self.queue) < self.capacity:
            self.queue.append(car_id)
            print(f"🚗 Car {car_id} arrived.")
        else:
            print(f"❌ Parking lot is full. Car {car_id} cannot enter.")

    def depart(self):
        if self.queue:
            car_id = self.queue.popleft()
            print(f"🚙 Car {car_id} departed.")
        else:
            print("⚠️ Parking lot is empty.")

    def status(self):
        print("📊 Current parking lot status:")
        if self.queue:
            for i, car in enumerate(self.queue, start=1):
                print(f"{i}. Car {car}")
        else:
            print("No cars in the parking lot.")

def main():
    print("\n🚘 Parking Queue Simulator")
    try:
        capacity = int(input("Enter parking lot capacity: "))
    except ValueError:
        print("❌ Invalid input. Capacity must be an integer.")
        return

    parking = ParkingLot(capacity)

    while True:
        print("\nMenu:")
        print("1. Car arrival")
        print("2. Car departure")
        print("3. Show parking status")
        print("4. Exit program")
        choice = input("Your choice: ")

        if choice == "1":
            car_id = input("Enter car ID: ")
            parking.arrive(car_id)
        elif choice == "2":
            parking.depart()
        elif choice == "3":
            parking.status()
        elif choice == "4":
            print("👋 Exiting Parking Queue Simulator.")
            break
        else:
            print("❌ Invalid option. Please try again.")
