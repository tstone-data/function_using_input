
def get_formatted_city(city, state):
    """Takes in input and returns it neatly formatted."""
    formatted_city = f"{city}, {state}"
    return formatted_city.title()

i = 0

while i < 3:
    print("\nPlease enter a destination.")
    print("(Enter 'q' at any point to end program)")
    city_name = input("City: ")
    if city_name == 'q':
        break
    state_name = input("State: ")
    if state_name == 'q':
        break

    destination = get_formatted_city(city_name, state_name)
    print("")
    print(destination)

    i+=1
