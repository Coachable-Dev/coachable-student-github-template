from stencil import Car

def test_initialization():
    # Test the initialization of a Car object
    car = Car("Toyota", "Corolla", 2020, 30.5)
    assert car.make == "Toyota"
    assert car.model == "Corolla"
    assert car.year == 2020
    assert car.fuel_efficiency == 30.5

def test_update_make():
    # Test updating the make of the car
    car = Car("Toyota", "Corolla", 2020, 30.5)
    car.update_make("Honda")
    assert car.make == "Honda"

def test_update_model():
    # Test updating the model of the car
    car = Car("Toyota", "Corolla", 2020, 30.5)
    car.update_model("Civic")
    assert car.model == "Civic"

def test_update_year():
    # Test updating the year of the car
    car = Car("Toyota", "Corolla", 2020, 30.5)
    car.update_year(2021)
    assert car.year == 2021

def test_plan_trip():
    # Test planning a trip with the car
    car = Car("Toyota", "Corolla", 2020, 30.5)
    fuel_needed = car.plan_trip(305)
    assert round(fuel_needed, 2) == 10.0

    # Test edge case: Very large distance that exceeds fuel tank capacity
    try:
        car.plan_trip(500)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError for excessive fuel requirement"

    # Test edge case: Non-positive distance
    try:
        car.plan_trip(-100)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError for negative distance"

def test_display_details():
    # Test displaying the car's details
    car = Car("Toyota", "Corolla", 2020, 30.5)
    car.display_details()  # Expect output, but no return value to test