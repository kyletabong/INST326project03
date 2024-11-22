class PayReport:
    # The PayReport class generates a report of weekly pay for a list of caregivers.
    def __init__(self, caregivers):
        # Validate that the provided caregivers argument is a list.
        if not isinstance(caregivers, list):
            raise ValueError("Caregivers must be a list of caregiver objects.")
        self.caregivers = caregivers  # Store the list of caregiver objects.

    def generate_report(self):
        # Method to calculate and print the weekly pay report.
        total_weekly_pay = 0  # Initialize the total weekly pay to zero.

        print("Weekly Pay Report:")  # Print the report heading.
        print("------------------")  # Print a separator.

        # Iterate through the list of caregivers.
        for caregiver in self.caregivers:
            # Ensure each caregiver has the required attributes and method.
            if not hasattr(caregiver, 'name') or not hasattr(caregiver, 'calculate_weekly_pay'):
                raise AttributeError(
                    "Each caregiver must have a 'name' attribute and a 'calculate_weekly_pay()' method."
                )

            try:
                # Calculate the weekly pay using the caregiver's method.
                weekly_pay = caregiver.calculate_weekly_pay()

                # Check that the weekly pay is a valid numeric value.
                if not isinstance(weekly_pay, (int, float)):
                    raise ValueError(f"Invalid pay calculated for {caregiver.name}. Must be a number.")

                # Add the weekly pay to the total pay.
                total_weekly_pay += weekly_pay

                # Print the individual caregiver's name and their weekly pay.
                print(f"{caregiver.name}: ${weekly_pay:.2f}")
            except Exception as e:
                # Handle errors that occur while processing a caregiver and print an error message.
                print(f"Error processing caregiver {caregiver.name}: {e}")

        print("------------------")
        print(f"Total Weekly Pay: ${total_weekly_pay:.2f}")

class Caregiver:
    # The Caregiver class represents an individual caregiver with pay information.
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name  # Store the caregiver's name.
        self.hourly_rate = hourly_rate  # Store the hourly pay rate.
        self.hours_worked = hours_worked  # Store the number of hours worked in a week.

    def calculate_weekly_pay(self):
        # Calculate the weekly pay as the product of hourly rate and hours worked.
        return self.hourly_rate * self.hours_worked

# Example of Usage
caregivers = [
    Caregiver("Lisa", 19, 40),  # Lisa works 40 hours at $19/hour.
    Caregiver("Miles", 20, 28),  # Miles works 28 hours at $20/hour.
    Caregiver("Jerry", 15.5, 30),  # Jerry works 30 hours at $15.50/hour.
]

# Create an instance of PayReport with the caregivers list.
report = PayReport(caregivers)

# Generate and print the weekly pay report.
report.generate_report()
