from datetime import datetime, timedelta

# Predefined vaccination schedule
vaccination_schedule = {
    'BCG': 0,        # At birth
    'Hepatitis B': 1, # 1 month
    'Polio': 2,       # 2 months
    'DPT': 6,         # 6 months
    'Measles': 9,     # 9 months
}

# Parent class
class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Child class
class Child:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        self.appointments = {}

    def get_vaccination_schedule(self):
        print(f"\nVaccination schedule for {self.name}:")
        for vaccine, months in vaccination_schedule.items():
            due_date = self.birthdate + timedelta(days=months*30)
            print(f"{vaccine}: Due on {due_date.strftime('%Y-%m-%d')}")

    def book_appointment(self, vaccine):
        if vaccine in vaccination_schedule:
            due_date = self.birthdate + timedelta(days=vaccination_schedule[vaccine]*30)
            appointment_date = input(f"Enter appointment date for {vaccine} (YYYY-MM-DD): ")
            self.appointments[vaccine] = appointment_date
            print(f"Appointment for {vaccine} booked on {appointment_date} for {self.name}.")
        else:
            print(f"Invalid vaccine: {vaccine}")

    def view_reminders(self):
        print(f"\nReminders for {self.name}:")
        for vaccine, date in self.appointments.items():
            print(f"{vaccine} appointment on {date}")

# Main system
def main():
    parent = Parent(input("Enter parent's name: "))
    
    while True:
        print("\nOptions:")
        print("1. Register a Child")
        print("2. View Vaccination Schedule")
        print("3. Book Vaccination Appointment")
        print("4. View Reminders")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            child_name = input("Enter child's name: ")
            birthdate = input("Enter child's birthdate (YYYY-MM-DD): ")
            child = Child(child_name, birthdate)
            parent.add_child(child)
            print(f"Child {child_name} added.")
        
        elif choice == "2":
            for child in parent.children:
                child.get_vaccination_schedule()

        elif choice == "3":
            child_name = input("Enter child's name to book appointment: ")
            vaccine = input("Enter vaccine name to book appointment for: ")
            for child in parent.children:
                if child.name == child_name:
                    child.book_appointment(vaccine)
                    break

        elif choice == "4":
            for child in parent.children:
                child.view_reminders()

        elif choice == "5":
            print("Exiting system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
