#  Determine if a given year is a leap year

# The Orbital Offset (Rule of 4): The Earth takes approximately 365.2425 days to orbit the Sun, but our standard calendar only has 365 days. To account for the remaining fraction of a day (roughly 0.25 days or 6 hours each year), we add one extra day every four years (4 * 0.25 hr = 1 day) to prevent the calendar from drifting out of sync with the solar seasons.

# The Centenary Overcorrection (Rule of 100): Adding a leap day every four years assumes the solar year is exactly 365.25 days long. Because it is actually slightly shorter (365.2425 days), this rule overcorrects by about 11 minutes per year, which adds up to a full extra day every 100 years. To compensate for this buildup, century years (years ending in 00) are stripped of their leap year status.

# The Final Alignment (Rule of 400): Skipping a leap year every 100 years reduces the calendar's average year length just a bit too much, creating a tiny undercorrection. To achieve near-perfect mathematical alignment with the Earth's true 365.2425-day orbit, the calendar adds a leap day back in once every 400 years, making years like 1600 and 2000 exceptional leap years

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap

while True:
    try:
        year = int(input("Enter the year : "))
        print(f"{year} is a Leap year : {leap_year(year)}")
    except ValueError:
        print("Year must be an INTEGER")
        continue

    query = input("Do you want to continue ? (y/n) ").strip().lower()
    if query == 'n':
        break