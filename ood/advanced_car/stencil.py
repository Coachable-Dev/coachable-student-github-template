class Car:
    '''
    Initializes a Car object with the given make, model, year, and fuel efficiency.

    Edge Cases:
    - Ensure 'year' is a positive integer.
    - Ensure 'fuel_efficiency' is a positive float.
    - Make sure 'make' and 'model' are non-empty strings.
    '''
    def __init__(self, make: str, model: str, year: int, fuel_efficiency: float) -> None:
        # Your code here
        pass

    '''
    Updates the make of the car.

    Edge Cases:
    - Ensure 'new_make' is a non-empty string.
    '''
    def update_make(self, new_make: str) -> None:
        # Your code here
        pass

    '''
    Updates the model of the car.

    Edge Cases:
    - Ensure 'new_model' is a non-empty string.
    '''
    def update_model(self, new_model: str) -> None:
        # Your code here
        pass

    '''
    Updates the year of the car.

    Edge Cases:
    - Ensure 'new_year' is a positive integer.
    '''
    def update_year(self, new_year: int) -> None:
        # Your code here
        pass

    '''
    Calculates the amount of fuel needed for a given trip distance.

    Rounds the fuel needed to 2 decimal places.

    Edge Cases:
    - Ensure 'distance' is a positive float. Raise a ValueError if not.
    - Assume the car has a maximum fuel tank capacity of 15 gallons. 
      If the trip distance requires more fuel than the tank can hold, raise a ValueError.
    '''
    def plan_trip(self, distance: float) -> float:
        # Your code here
        pass

    '''
    Displays the car's details including make, model, year, and fuel efficiency.
    '''
    def display_details(self) -> None:
        # Your code here
        pass