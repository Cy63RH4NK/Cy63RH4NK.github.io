
def travel_budget():
    print("Welcome to the Travel Budget Calculator!")

    # Input for initial budget
    initial_budget = float(input("Enter your initial budget: "))
    
    # Input for destination and its distance
    destination = input("Enter your destination: ")
    distance = float(input(f"Enter the distance to {destination} (in miles): "))
    
    # Input for gas costs
    miles_per_gallon = float(input("Enter your vehicle's miles per gallon: "))
    gas_price = float(input("Enter the current gas price per gallon: "))
    total_gas_cost = (distance / miles_per_gallon) * gas_price
    
    # Input for food costs
    daily_food_cost = float(input("Enter your estimated daily food cost: "))
    trip_length = int(input("Enter the number of days of your trip: "))
    total_food_cost = daily_food_cost * trip_length
    
    # Input for accommodation costs
    nightly_accommodation_cost = float(input("Enter your estimated nightly accommodation cost: "))
    total_accommodation_cost = nightly_accommodation_cost * trip_length
    
    # Total budget calculation
    total_budget = total_gas_cost + total_food_cost + total_accommodation_cost
    remaining_budget = initial_budget - total_budget
    
    # Output results
    print("\n--- Travel Budget Summary ---")
    print(f"Destination: {destination}")
    print(f"Total Gas Cost: ${total_gas_cost:.2f}")
    print(f"Total Food Cost: ${total_food_cost:.2f}")
    print(f"Total Accommodation Cost: ${total_accommodation_cost:.2f}")
    print(f"Total Estimated Expenses: ${total_budget:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")

# Run the travel budget calculator
travel_budget()

