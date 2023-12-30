class FlightBookingSystem:
    def __init__(self):
        # Initialize data (replace this with actual data retrieval logic)
        self.available_flights = [
            {"flight_id": 1, "destination": "Nairobi", "departure_time": "10:00 AM", "seats_available": 50},
            {"flight_id": 2, "destination": "Mombasa", "departure_time": "12:30 PM", "seats_available": 30},
            # Add more flights as needed
        ]

        self.selected_flight = None
        self.selected_seat = None

    def display_flights(self):
        print("Available Flights:")
        for flight in self.available_flights:
            print(f"ID: {flight['flight_id']}, Destination: {flight['destination']}, Departure Time: {flight['departure_time']}, Seats Available: {flight['seats_available']}")

    def select_flight(self, flight_id):
        for flight in self.available_flights:
            if flight['flight_id'] == flight_id:
                self.selected_flight = flight
                break

    def select_seat(self, seat_number):
        if seat_number <= self.selected_flight['seats_available']:
            self.selected_seat = seat_number
            self.selected_flight['seats_available'] -= 1
            return True
        else:
            print("Sorry, the selected seat is not available. Please choose another seat.")
            return False

    def book_flight(self):
        print(f"Booking Confirmation - Flight to {self.selected_flight['destination']}")
        print(f"Departure Time: {self.selected_flight['departure_time']}")
        print(f"Seat Number: {self.selected_seat}")
        print("Booking successful! Enjoy your flight.")

def main():
    booking_system = FlightBookingSystem()

    # Main menu
    while True:
        print("\nMain Menu:")
        print("1. View Available Flights")
        print("2. Book a Flight")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            booking_system.display_flights()
        elif choice == '2':
            flight_id = int(input("Enter the ID of the flight you want to book: "))
            booking_system.select_flight(flight_id)

            if booking_system.selected_flight:
                seat_number = int(input("Enter your desired seat number: "))
                if booking_system.select_seat(seat_number):
                    booking_system.book_flight()
        elif choice == '3':
            print("Thank you for using the Flight Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
