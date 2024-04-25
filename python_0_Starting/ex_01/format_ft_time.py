import datetime  # Importing the datetime module to work with dates and times
import time      # Importing the time module to work with time-related functions

# Getting the current time in seconds since the epoch (January 1, 1970)
current_time = time.time()

# Getting the current date
current_date = datetime.date.today()

# Formatting the current time to display with comma separation and 4 decimal places
formatted_seconds = f"{current_time:,.4f}"

# Formatting the current time to display in scientific notation with 2 decimal places
scientific_notation = f"{current_time:.2e}"

# Printing the formatted current time in both formats
print(f"Seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in scientific notation")

# Printing the current date in the format: Month Day Year
print(f"{current_date.strftime('%b %d %Y')}")