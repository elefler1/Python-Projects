def validate_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def final_shutoff_volume(actual_tank_capacity):
    """
    Calculate the final shutoff volume of a tank.

    Parameters:
    actual_tank_capacity (float): The actual capacity of the tank.

    Returns:
    float: The final shutoff volume, which is 95% of the actual tank capacity.

    Requirements:
    Once the final shutoff volume is deteremined, the user must reference their tank chart to find the corresponding height for the final shutoff volume.
    """
    final_shutoff_volume = 0.95 * actual_tank_capacity
    print(f"Final Shutoff Volume: {final_shutoff_volume} units")
    return final_shutoff_volume


def calculate_upper_drop_tube_length(final_shutoff_height, seat_surface_to_bottom):
    """
    Calculate the upper drop tube length.

    Parameters:
    seat_surface_to_bottom (float): The drop tube seat surface to bottom of tank.
    final_shutoff_height (float): The final shutoff volume height.

    Returns:
    float: The length of the upper drop tube.
    """
    upper_drop_tube_length = (seat_surface_to_bottom - final_shutoff_height) - 2
    print(f"Upper Drop Tube Length: {upper_drop_tube_length} inches")
    return upper_drop_tube_length

def calculate_lower_drop_tube_length(final_shutoff_height):
    """
    Calculate the lower drop tube length.

    Parameters:
    final_shutoff_height (float): The final shutoff volume height.

    Returns:
    float: The length of the lower drop tube.
    """
    lower_drop_tube_length = (final_shutoff_height - 15.75) - 6
    print(f"Lower Drop Tube Length: {lower_drop_tube_length} inches")
    return lower_drop_tube_length

def main():
    print("\nCalculating Final Shutoff Volume...")
    actual_tank_capacity = validate_float_input("Enter the actual tank capacity: ")
    final_shutoff_volume(actual_tank_capacity)
    final_shutoff_height = validate_float_input("Enter the final shutoff height gathered from your tank chart: ")
    seat_surface_to_bottom = validate_float_input("Enter the drop tube seat surface to bottom of tank measurement: ")

    print("\nCalculating Upper Drop Tube Length...")
    calculate_upper_drop_tube_length(final_shutoff_height, seat_surface_to_bottom)

    print("\nCalculating Lower Drop Tube Length...")
    calculate_lower_drop_tube_length(final_shutoff_height)

main()