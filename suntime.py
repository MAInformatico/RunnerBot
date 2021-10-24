import datetime
import ephem #dependecy required. To install it, run 'pip install pyephem'

def read():
    with open("coordinates.txt") as _file:
        values = _file.read()
    return values

coordinates = str(read()).split(',')


def getSunrise(coordinates):
    o = ephem.Observer()
    o.lat, o.long, o.date = str(coordinates[0]), str(coordinates[1]), datetime.datetime.utcnow() #Set your own coordinates here
    Sun = ephem.Sun(o)
    return getTimezone(str(o.next_rising(Sun)))

def getSunset():
    o = ephem.Observer(coordinates)
    o.lat, o.long, o.date = str(coordinates[0]), str(coordinates[1]), datetime.datetime.utcnow() #Same situation than previous method
    Sun = ephem.Sun(o)
    return getTimezone(str(o.next_setting(Sun)))

def getTimezone(time):
    splitTime = time.split(' ')
    hour = datetime.datetime.strptime(splitTime[1],'%X')
    hour += datetime.timedelta(hours=2)
    splitHour = str(hour).split(' ')
    timezone = splitTime[0] + " " + str(splitHour[1])
    return str(timezone)