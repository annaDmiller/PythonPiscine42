from datetime import datetime as dt

now_date = dt.now()
old_date = dt(1970, 1, 1)
diff_sec = (now_date - old_date).total_seconds()

print(f"Seconds since January 1, 1970: {diff_sec:,.4f} or {diff_sec:.2e} in scientific notation")
print(now_date.strftime("%b %d %Y"))  # '%b' - short name of a month; '%d' - day; '%Y' - long format of the year
