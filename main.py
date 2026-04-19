# Railway Reservation System

total_seats = 5
bookings = {}

def check_availability():
    print(f"Available seats: {total_seats - len(bookings)}")

def book_ticket():
    if len(bookings) >= total_seats:
        print("No seats available!")
        return

    name = input("Enter name: ")
    age = input("Enter age: ")

    booking_id = len(bookings) + 1
    seat_number = booking_id

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    print(f"Ticket booked! Booking ID: {booking_id}, Seat: {seat_number}")

def view_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        print("Booking Details:", bookings[bid])
    else:
        print("Booking not found!")

def cancel_ticket():
    bid = int(input("Enter booking ID: "))
    if bid in bookings:
        del bookings[bid]
        print("Ticket cancelled!")
    else:
        print("Invalid ID!")

while True:
    print("\n1.Check Availability\n2.Book Ticket\n3.View Ticket\n4.Cancel Ticket\n5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
