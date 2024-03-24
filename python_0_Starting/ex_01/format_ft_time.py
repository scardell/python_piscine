import datetime
import time

current_time = time.time()
current_date = datetime.date.today()

formatted_seconds = f"{current_time:,.4f}"
scientific_notation = f"{current_time:.2e}"

print(f"seconds since January 1, 1970: {formatted_seconds} or {scientific_notation} in specific notation")
print(f"{current_date.strftime('%b %d %Y')}")