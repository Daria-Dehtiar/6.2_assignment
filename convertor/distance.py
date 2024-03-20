def convert_feets_to_meters(distance:str) -> str:
    if "ft" in distance:
        feets = float(distance.replace("ft", "").strip())
        meters = round((feets * 0.3048), 2)
        return f"{meters}m"
    else: return distance

def convert_meters_to_feets(distance:str) -> str:
    if "m" in distance:
        meters = float(distance.replace("m", "").strip())
        feets = round((meters / 0.3048), 2)
        return f"{feets}ft"
    else: return distance



