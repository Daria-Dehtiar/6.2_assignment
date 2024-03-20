def convert_celsius_to_fahrenheit(temperature: float, unit: str) -> float:
    if unit == "C":
        fahrenheit = round(((temperature * 9/5) + 32), 2)
        return fahrenheit
    elif unit == "F":
        return temperature

def convert_fahrenheit_to_celsius(temperature: float, unit: str) -> float:
    if unit == "F":
        celsius = round((5/9 * (temperature - 32)), 2)
        return celsius
    elif unit == "C":
        return temperature


