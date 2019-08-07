# libraries required
# pip install python-geoip
# pip install python-geoip-geolite2


from geoip import geolite2

match = geolite2.lookup('34.216.171.68');

# print(match.country);
#
# for key in match:
#     print (key, match[key])
import maxminddb

reader = maxminddb.open_database('GeoLite2-City.mmdb')

details = reader.get('34.216.171.68')
print(details);
# {'country': ... }

reader.close()
