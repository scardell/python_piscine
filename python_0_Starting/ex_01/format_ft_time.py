import datetime

current_time = datetime.datetime.now()
formated_current_time = current_time.strftime("%B %d, %Y %H:%M:%S")

current_date = datetime.date.today()

print(f"seconds since January 1, 1970: {formated_current_time} or {current_time:.2e} in specific notation")
print(f"{current_date}")
print(f"{current_date.strftime('%B')} {current_date.day} {current_date.year}")
print(f"{current_date.strftime('%b %d %Y')}")