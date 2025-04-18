from astropy.coordinates import EarthLocation, AltAz, get_sun
from astropy.time import Time
from datetime import datetime
import pytz
import astropy.units as u
import math

def calculate_rising_sign(latitude, longitude, birth_date, birth_time, timezone="UTC"):
    """
    Calculate the rising sign based on birth details.

    Args:
    - latitude (float): Latitude of the birth location in decimal degrees.
    - longitude (float): Longitude of the birth location in decimal degrees.
    - birth_date (str): Birth date in the format 'YYYY-MM-DD'.
    - birth_time (str): Birth time in the format 'HH:MM' (24-hour format).
    - timezone (str): Timezone of the birth location (default is 'UTC').

    Returns:
    - str: The Rising Sign.
    """
    # Define Zodiac signs
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Calculate birth datetime in local timezone
    local_tz = pytz.timezone(timezone)
    birth_dt = datetime.strptime(f"{birth_date} {birth_time}", "%Y-%m-%d %H:%M")
    birth_dt = local_tz.localize(birth_dt)

    # Convert to UTC and AstroPy Time object
    utc_dt = birth_dt.astimezone(pytz.utc)
    time = Time(utc_dt.strftime("%Y-%m-%dT%H:%M:%S"))  # Format without timezone offset

    # Calculate Local Sidereal Time (LST)
    lst = time.sidereal_time('mean', longitude * u.deg)

    # Calculate Ascendant (Rising Degree)
    ascendant = (lst.deg + longitude) % 360

    # Determine Zodiac Sign
    sign_index = int(ascendant // 30)

    return zodiac_signs[sign_index]

# Example Usage
latitude = 6.9271  # Latitude for Sri Lanka
longitude = 79.8612  # Longitude for Sri Lanka
# birth_date = "1998-10-09"
# birth_time = "01:00"
# timezone = "Asia/Colombo"

birth_date = "1995-04-08"
birth_time = "15:00"
timezone = "Asia/Colombo"

rising_sign = calculate_rising_sign(latitude, longitude, birth_date, birth_time, timezone)
print(f"Your Rising Sign is {rising_sign}.")
