import pytest
from stencil import *

def test_smart_device():
    device = SmartDevice("Living Room Light", "Living Room")
    assert device.device_name == "Living Room Light"
    assert device.location == "Living Room"
    assert device.get_status() == "off"

    device.turn_on()
    assert device.get_status() == "on"
    device.turn_off()
    assert device.get_status() == "off"

    device.status = "invalid"
    assert device.get_status() == "off"

    assert str(device) == "Living Room Light in Living Room is off."

    with pytest.raises(ValueError):
        SmartDevice("", "Living Room")
    with pytest.raises(ValueError):
        SmartDevice("Living Room Light", "")


def test_light():
    light = Light("Living Room Light", "Living Room")
    assert light.device_name == "Living Room Light"
    assert light.location == "Living Room"
    assert light.get_status() == "off"
    assert light.brightness == 100
    assert light.color == "white"

    light.set_brightness(75)
    assert light.brightness == 75
    light.set_brightness(150)
    assert light.brightness == 100  # Should round down to 100
    light.set_brightness(-10)
    assert light.brightness == 0  # Should round up to 0

    light.set_color("blue")
    assert light.color == "blue"
    light.set_color("unknown color")
    assert light.color == "white"  # Should default to white on invalid color

    # Check the state before turning on
    assert light.brightness == 0  # After all changes, brightness is 0
    assert light.color == "white"  # After all changes, color is white

    light.turn_on()
    assert str(light) == "Living Room Light in Living Room is on with brightness 0 and color white."


def test_thermostat():
    thermostat = Thermostat("Hallway Thermostat", "Hallway")
    assert thermostat.device_name == "Hallway Thermostat"
    assert thermostat.location == "Hallway"
    assert thermostat.get_status() == "off"
    assert thermostat.temperature == 70.0
    assert thermostat.mode == "off"

    thermostat.set_temperature(75.0)
    assert thermostat.temperature == 75.0
    thermostat.set_temperature(90.0)
    assert thermostat.temperature == 85.0  # Should round down to 85
    thermostat.set_temperature(40.0)
    assert thermostat.temperature == 50.0  # Should round up to 50

    thermostat.set_mode("heat")
    assert thermostat.mode == "heat"
    thermostat.set_mode("unknown mode")
    assert thermostat.mode == "off"  # Should default to off on invalid mode

    # Before turning on, check the state
    assert thermostat.temperature == 50.0  # After all changes, temperature is 50.0
    assert thermostat.mode == "off"  # After all changes, mode is off

    thermostat.turn_on()
    assert str(thermostat) == "Hallway Thermostat in Hallway is set to 50.0 degrees in off mode."


def test_smart_lock():
    lock = SmartLock("Front Door Lock", "Entryway")
    assert lock.device_name == "Front Door Lock"
    assert lock.location == "Entryway"
    assert lock.get_status() == "off"
    assert lock.locked_status == "unlocked"

    lock.lock()
    assert lock.locked_status == "locked"
    lock.unlock()
    assert lock.locked_status == "unlocked"

    lock.lock()
    assert str(lock) == "Front Door Lock in Entryway is locked."


def test_smart_home():
    home = SmartHome()
    light = Light("Living Room Light", "Living Room")
    thermostat = Thermostat("Hallway Thermostat", "Hallway")
    lock = SmartLock("Front Door Lock", "Entryway")

    home.add_device(light)
    home.add_device(thermostat)
    home.add_device(lock)
    assert len(home.list_devices()) == 3

    retrieved_device = home.get_device("Living Room Light")
    assert retrieved_device == light

    home.remove_device("Living Room Light")
    assert len(home.list_devices()) == 2

    with pytest.raises(ValueError):
        home.get_device("Living Room Light")

    with pytest.raises(ValueError):
        home.remove_device("Nonexistent Device")

    expected_report = (
        "Hallway Thermostat in Hallway is set to 70.0 degrees in off mode.\n"
        "Front Door Lock in Entryway is unlocked."
    )
    assert home.status_report() == expected_report


def test_room():
    room = Room("Living Room")
    light = Light("Living Room Light", "Living Room")
    thermostat = Thermostat("Hallway Thermostat", "Living Room")

    room.add_device_to_room(light)
    room.add_device_to_room(thermostat)
    assert len(room.list_room_devices()) == 2

    with pytest.raises(ValueError):
        room.add_device_to_room(light)

    room.remove_device_from_room("Living Room Light")
    assert len(room.list_room_devices()) == 1

    with pytest.raises(ValueError):
        room.remove_device_from_room("Nonexistent Device")