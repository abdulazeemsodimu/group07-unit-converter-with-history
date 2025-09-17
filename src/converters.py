class MassConverter:
    """
    A class to handle conversion between different mass units.
    Supported units: grams (g), kilograms (kg), milligrams (mg).
    """

    # Dictionary to store unit conversion factors relative to grams
    units = {"g": 1, "kg": 1000, "mg": 0.001}

    def convert(self, value, from_unit, to_unit):
        """
        Convert a given mass value from one unit to another.

        Args:
            value (float): The numerical mass value to be converted.
            from_unit (str): The unit of the input value ('g', 'kg', 'mg').
            to_unit (str): The unit to convert the value into ('g', 'kg', 'mg').

        Returns:
            float: Converted value in the target unit.

        Raises:
            ValueError: If either from_unit or to_unit is not supported.
        """
        # Ensure both units are valid
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError("Unit not supported")

        # Convert input to grams first
        in_grams = value * self.units[from_unit]

        # Convert from grams to target unit
        return in_grams / self.units[to_unit]


class TemperatureConverter:
    """
    A class to handle temperature conversions between Celsius, Fahrenheit, and Kelvin.
    """

    def convert(self, value, from_unit, to_unit):
        """
        Convert a given temperature value from one unit to another.

        Args:
            value (float): The numerical temperature value to be converted.
            from_unit (str): The unit of the input value ('C', 'F', 'K').
            to_unit (str): The unit to convert the value into ('C', 'F', 'K').

        Returns:
            float: Converted value in the target unit.

        Raises:
            ValueError: If either from_unit or to_unit is not supported.
        """
        # Step 1: Convert input value to Celsius
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = (value - 32) * 5/9
        elif from_unit == "K":
            celsius = value - 273.15
        else:
            raise ValueError("Unit not supported")

        # Step 2: Convert from Celsius to target unit
        if to_unit == "C":
            return celsius
        elif to_unit == "F":
            return celsius * 9/5 + 32
        elif to_unit == "K":
            return celsius + 273.15
        else:
            raise ValueError("Unit not supported")
