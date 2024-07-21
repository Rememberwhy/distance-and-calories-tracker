### This application is created by Sandro Zakaidze ###
### It prompts users to enter the name of the person and the distance they walked. ###
### The application then calculates the number of steps taken and the calories burned. ###
### Upon completing all the steps application will save logs in walking_log.txt ### 

import datetime

# Function to validate input
def get_valid_km():
    while True:
        try:
            km = float(input("Please enter how many km you walked today: "))
            if km < 0:
                print("Distance can't be negative. Please enter a valid number.")
            else:
                return km
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate steps
def calculate_steps(km):
    return 1000 * km

# Function to estimate calories burned (approximation)
def calculate_calories(steps):
    return steps * 0.04  # Roughly 0.04 calories per step

# Function to process a single person's data
def process_person(name):
    km = get_valid_km()
    steps = calculate_steps(km)
    calories_burned = calculate_calories(steps)
    
    # Get current date
    today = datetime.date.today()
    
    # Display results
    print("\n" + "="*50)
    print(f"Date: {today}")
    print(f"Name: {name}")
    print(f"Distance walked: {km:.2f} km")
    print(f"Steps taken: {steps:,}")
    print(f"Calories burned: {calories_burned:.2f} calories")
    print("="*50 + "\n")

    # Log the data
    with open("walking_log.txt", "a") as log:
        log.write(f"{today}: {name} walked {km} km, {steps} steps, {calories_burned:.2f} calories burned\n")

# Main function
def main():
    print("Welcome to the Walking Tracker App!")
    while True:
        name = input("Enter the name of the person (or type 'done' to exit): ")
        if name.lower() == "done":
            print("You exited from the application. Have a good day!")
            break
        else:
            process_person(name)

# Run the program
if __name__ == "__main__":
    main()
