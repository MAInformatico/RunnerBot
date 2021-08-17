import datetime
import ephem #dependecy required. To install it, run 'pip install pyephem'

def getSunrise():
    o = ephem.Observer()
    o.lat, o.long, o.date = '37:10', '-3:36', datetime.datetime.utcnow() #Set your own coordinates here
    Sun = ephem.Sun(o)
    return str(o.next_rising(Sun))

def getSunset():
    o = ephem.Observer()
    o.lat, o.long, o.date = '37:10', '-3:36', datetime.datetime.utcnow() #Same situation than previous method
    Sun = ephem.Sun(o)
    return str(o.next_setting(Sun))

