import datetime
import pytz

# Naive date-times: Do not have enough information to determine things like timezones, or daylight savings times. Easier to work with/
# Aware date-times: If we need details to avoid confusion, we use these. 

# Let us begin with Naive and then move to Aware
d = datetime.date(2020, 7, 24)
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday())                       # It starts weekday with 0 (Monday)
print(tday.isoweekday())                    # It starts weekday with 1 (Monday)

tdelta = datetime.timedelta(days=7)
print("Date 1 week after today:", tday + tdelta)
print("Date 1 week before today:", tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2024, 3, 16)

till_bday = bday - datetime.date.today()
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)

dt = datetime.datetime(2020, 7, 26, 12, 30, 45, 100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)

tdelta = datetime.timedelta(days = 7)
print(dt + tdelta)

tdelta = datetime.timedelta(hours = 12)
print(dt + tdelta)

dt_today = datetime.datetime.today()        # Provides date and time according to current timezone. Timezone info is set to none
dt_now = datetime.datetime.now()            # Provides date and time according to the timezone specified
dt_utcnow = datetime.datetime.utcnow()      # Provides date and time according UTC timezone but the timezone info is still set to none

print(dt_today)
print(dt_now)
print(dt_utcnow)

print('-'*30)

# Using pytz
dt = datetime.datetime(2020, 7, 26, 12, 30, 45, tzinfo = pytz.utc)
print(dt)

dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

dt_myloc = dt_utcnow.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_myloc)

print(dt_myloc.isoformat())

# strfttime - Datetime to string
# strptime - String to Datetime
print(dt_myloc.strftime('%B %d, %Y'))

# Converting string to date time
dt_str = 'November 09, 2023'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)