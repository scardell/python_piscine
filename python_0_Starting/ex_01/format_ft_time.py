import time
import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

current_time = time.time()
formated_current_time = \
    locale.format_string("%.4f", current_time, grouping=True)

current_date = datetime.date.today()

print(f"seconds since January 1, 1970: {formated_current_time} or {current_time:.2e} in specific notation")
print(f"{current_date}")
print(f"{current_date.strftime('%B')} {current_date.day} {current_date.year}")
print(f"{current_date.strftime('%b %d %Y')}")