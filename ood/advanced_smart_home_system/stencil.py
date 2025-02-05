class SmartDevice:
    '''
    Represents a generic smart device.

    - The device has a name, status (either 'on' or 'off'), and a location in the home.
    - The device is initially off.

    Edge Cases:
    - Ensure the device name and location are non-empty strings. If they are empty, raise a ValueError.
    - The status should only be 'on' or 'off'. If accessed or modified improperly, it should default to 'off'.
    '''
    def __init__(self, device_name: str, location: str) -> None:
        # Initialize the smart device with a name and location, and set the status to 'off'
        pass

    '''
    Turns the device on.

    - The status should be updated to 'on'.

    Edge Cases:
    - If the device is already on, it should remain on without any errors.
    '''
    def turn_on(self) -> None:
        pass

    '''
    Turns the device off.

    - The status should be updated to 'off'.

    Edge Cases:
    - If the device is already off, it should remain off without any errors.
    '''
    def turn_off(self) -> None:
        pass

    '''
    Returns the current status of the device.

    - The status should be either 'on' or 'off'.

    Edge Cases:
    - The status should always be returned as 'on' or 'off'. If any other value is set, it should default to 'off'.
    '''
    def get_status(self) -> str:
        pass

    '''
    Returns a string representation of the device in the format:
    "<device_name> in <location> is <status>."

    Example:
    - "Living Room Light in Living Room is on."
    '''
    def __str__(self) -> str:
        pass


class Light(SmartDevice):
    '''
    Represents a smart light, inheriting from SmartDevice.

    - In addition to the basic device attributes, a Light has brightness and color settings.
    - Brightness is an integer between 0 and 100, and color is a string.

    Edge Cases:
    - Ensure brightness is within the valid range (0 to 100). If out of range, round to the nearest valid value (0 or 100).
    - Handle invalid color inputs by setting a default color (e.g., 'white') if the provided color is not recognized.
    '''
    def __init__(self, device_name: str, location: str) -> None:
        # Initialize the light with default brightness of 100 and color as 'white'
        pass

    '''
    Sets the brightness of the light.

    - Brightness should be an integer between 0 and 100.

    Edge Cases:
    - If brightness is out of range, set it to the nearest valid value (0 or 100).
    '''
    def set_brightness(self, level: int) -> None:
        pass

    '''
    Sets the color of the light.

    - Color should be a valid string representing a color (e.g., 'red', 'blue').

    Edge Cases:
    - If an invalid color is provided, set the color to a default value (e.g., 'white').
    '''
    def set_color(self, color: str) -> None:
        pass

    '''
    Returns a string representation of the light's state in the format:
    "<device_name> in <location> is <status> with brightness <brightness> and color <color>."

    Example:
    - "Living Room Light in Living Room is on with brightness 75 and color warm white."
    '''
    def __str__(self) -> str:
        pass


class Thermostat(SmartDevice):
    '''
    Represents a smart thermostat, inheriting from SmartDevice.

    - In addition to the basic device attributes, a Thermostat has temperature and mode settings.

    Edge Cases:
    - Ensure the temperature is within a reasonable range (e.g., 50 to 85 degrees Fahrenheit). If out of range, set it to the nearest valid value.
    - Handle invalid modes by setting a default mode (e.g., 'off') if the provided mode is not recognized.
    '''
    def __init__(self, device_name: str, location: str) -> None:
        # Initialize the thermostat with default temperature 70.0 and mode 'off'
        pass

    '''
    Sets the temperature of the thermostat.

    - Temperature should be a float within the range of 50 to 85 degrees Fahrenheit.

    Edge Cases:
    - If the temperature is out of range, set it to the nearest valid value.
    '''
    def set_temperature(self, temp: float) -> None:
        pass

    '''
    Sets the operating mode of the thermostat.

    - Mode should be a valid string mode options are 'heat', 'cool', 'off'.

    Edge Cases:
    - If an invalid mode is provided, set the mode to a default value (e.g., 'off').
    '''
    def set_mode(self, mode: str) -> None:
        pass

    '''
    Returns a string representation of the thermostat's state in the format:
    "<device_name> in <location> is set to <temperature> degrees in <mode> mode."

    Example:
    - "Hallway Thermostat in Hallway is set to 72 degrees in heat mode."
    '''
    def __str__(self) -> str:
        pass


class SmartLock(SmartDevice):
    '''
    Represents a smart lock, inheriting from SmartDevice.

    - In addition to the basic device attributes, a SmartLock has a locked status.

    Edge Cases:
    - Handle cases where the locked status is accessed or modified incorrectly by ensuring it defaults to 'unlocked'.
    '''
    def __init__(self, device_name: str, location: str) -> None:
        # Initialize the smart lock with default locked status 'unlocked'
        pass

    '''
    Locks the smart lock.

    - The locked status should be updated to 'locked'.

    Edge Cases:
    - If the lock is already locked, it should remain locked without any errors.
    '''
    def lock(self) -> None:
        pass

    '''
    Unlocks the smart lock.

    - The locked status should be updated to 'unlocked'.

    Edge Cases:
    - If the lock is already unlocked, it should remain unlocked without any errors.
    '''
    def unlock(self) -> None:
        pass

    '''
    Returns a string representation of the lock's state in the format:
    "<device_name> in <location> is <locked_status>."

    Example:
    - "Front Door Lock in Entryway is locked."
    '''
    def __str__(self) -> str:
        pass


class SmartHome:
    '''
    Manages all the smart devices in the home.

    - Allows adding, removing, listing, and getting status reports of devices.
    
    Edge Cases:
    - When removing or retrieving a device by name, handle the case where the device does not exist by raising a ValueError.
    '''

    def __init__(self) -> None:
        # Initialize an empty list to store devices
        pass

    '''
    Adds a device to the smart home.

    - The device should be an instance of SmartDevice or its subclasses.
    '''
    def add_device(self, device: SmartDevice) -> None:
        pass

    '''
    Removes a device from the smart home by name.

    - The device should be removed from the list of devices.

    Edge Cases:
    - If the device does not exist, raise a ValueError with the message "Device not found."
    '''
    def remove_device(self, device_name: str) -> None:
        pass

    '''
    Returns a list of string representations of all devices in the smart home.

    - The list should include the string representation of each device.
    '''
    def list_devices(self) -> list:
        pass

    '''
    Returns a report of the status of all devices in the smart home.

    - The report should be a string with each device's status on a new line.
    '''
    def status_report(self) -> str:
        pass

    '''
    Retrieves a device by its name.

    - If the device is not found, raise a ValueError with the message "Device not found."

    Returns:
    - The SmartDevice object with the matching name.
    '''
    def get_device(self, device_name: str) -> SmartDevice:
        pass


class Room:
    '''
    Represents a room in the smart home.

    - The room contains multiple smart devices.

    Edge Cases:
    - Handle cases where a device being added already exists in the room by raising an appropriate error.
    - Ensure that devices cannot be added to multiple rooms at the same time.
    '''
    def __init__(self, room_name: str) -> None:
        # Initialize the room with a name and an empty list of devices
        pass

    '''
    Adds a device to the room.

    - The device should be an instance of SmartDevice or its subclasses.

    Edge Cases:
    - If a device with the same name already exists in the room, do not add it and raise an error.
    '''
    def add_device_to_room(self, device: SmartDevice) -> None:
        pass

    '''
    Removes a device from the room by name.

    - The device is removed from the list of devices.

    Edge Cases:
    - If the device does not exist in the room, raise an appropriate error.
    '''
    def remove_device_from_room(self, device_name: str) -> None:
        pass

    '''
    Returns a list of all devices in the room.

    - The list should include the name, status, and specific attributes of each device.
    '''
    def list_room_devices(self) -> list:
        pass