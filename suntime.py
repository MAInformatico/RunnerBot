import datetime
import ephem #dependecy required. To install it, run 'pip install pyephem'

def read():
    with open("coordinates.txt") as _file:
        values = _file.read()
    return values

coordinates = str(read()).split(',')


def get_sunrise():
    o = ephem.Observer()
    o.lat, o.long, o.date = str(coordinates[0]), str(coordinates[1]), datetime.datetime.utcnow() #Set your own coordinates here
    Sun = ephem.Sun(o)
    return get_time_zone(str(o.next_rising(sun)))

def get_sunset():
    o = ephem.Observer()
    o.lat, o.long, o.date = str(coordinates[0]), str(coordinates[1]), datetime.datetime.utcnow() #Same situation than previous method
    sun = ephem.Sun(o)
    return get_time_zone(str(o.next_setting(sun)))

def get_time_zone(time):
    split_time = time.split(' ')
    hour = datetime.datetime.strptime(split_time[1],'%X')
    hour += datetime.timedelta(hours=2)
    split_hour = str(hour).split(' ')
    timezone = split_time[0] + " " + str(split_hour[1])
    return str(timezone)