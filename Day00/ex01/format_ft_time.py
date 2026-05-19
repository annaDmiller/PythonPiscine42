from datetime import datetime as dt

now_date = dt.now() #returns the NOW date/time value
old_date = dt(1970, 1, 1) #returns the date/time value but as time not specified, it is set to 0 by default
diff = now_date - old_date #returns timedelta value, but in days/years
diff_seconds = diff.total_seconds() #to convert timedelta value into seconds
format_diff_sec = f"{diff_seconds:,.4f}" #formatting seconds: ',' means to separate the thousands by comma; '.4f' means that it will display 4 digits after .
sci_not_diff_sec = f"{diff_seconds:.2e}" #formatting seconds into scientific notation: '.2' means to display 2 digits after .; 'e' - for scientific notation

print("Seconds since January 1, 1970:", format_diff_sec, "or", sci_not_diff_sec, "in scientific notation")
print(now_date.strftime("%b %d %Y"))  # '%b' - for short name of a month; '%d' for days in a month; '%Y' - for long format of the year
