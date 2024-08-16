
def feet_and_inches_to_cm(feet, inches=0):
    total_inches = feet * 12 + inches
    centimeters = total_inches * 2.54
    return centimeters

try:
    # Take height input in feet
    feet = float(input("Enter your height (feet): "))
    # Convert the height to centimeters
    height_cm = feet_and_inches_to_cm(feet)
    print(f"Your height in centimeters is: {height_cm:.2f} cm")
    
    # Convert height from centimeters to meters for BMI calculation
    height_m = height_cm / 100

    # Take weight input in kilograms
    weight = float(input("Enter your weight in kg: "))
    
    # Calculate BMI
    BMI = weight / (height_m ** 2)
    print(f"Your Body Mass Index is: {BMI:.2f}")

    # Determine BMI category
    if BMI > 0:
        if BMI <= 16:
            print("You are severely underweight")
        elif BMI <= 18:
            print("You are underweight")
        elif BMI <= 25:
            print("You are healthy")
        elif BMI <= 30:
            print("You are overweight")
        else:
            print("You are severely overweight")
    else:
        print("Please enter correct values")

except ValueError:
    print("Please enter valid numbers for feet and weight.")
