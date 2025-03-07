import threading
import time

class TicketBooking:
    def __init__(self, available_tickets):
        self.available_tickets = available_tickets
        self.lock = threading.Lock()  # Lock to prevent race conditions

    def book_ticket(self, name):
        with self.lock:  # Ensure only one thread can access at a time
            if self.available_tickets > 0:
                print(f"{name} is booking a ticket...")
                time.sleep(2)  # Simulating ticket processing delay
                self.available_tickets -= 1
                print(f"Ticket successfully booked for {name}. Remaining tickets: {self.available_tickets}")
            else:
                print(f"Sorry {name}, no tickets available.")

# Initialize TicketBooking system with 1 ticket
booking_system = TicketBooking(1)

# Create threads for multiple users
threads = []
users = ["Alice", "Bob"]
for user in users:
    t = threading.Thread(target=booking_system.book_ticket, args=(user,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("Ticket booking process completed.")
