import datetime
import googlemaps
from datetime import datetime

# Jesse's code

gmaps = googlemaps.Client(key='AIzaSyDjSlPa90L1Rq_flnd4nmjQg0E1Pi3BYZA', retry_over_query_limit=False) # Python Client for Google Maps Services 3.0.2 documentation » https://googlemaps.github.io/google-maps-services-python/docs/index.html
#print statements in functions will need to be changed to return statements for gui

#get start and end location
def location(start, destination, errDisplay, e1, e2):
    try:
        global directions_result
        now = datetime.now()
        directions_result = gmaps.directions(start, destination, mode="driving", departure_time=now)
        errDisplay.config(text="")
    except googlemaps.exceptions.HTTPError as _:
        errDisplay.config(text="Error: Please Enter an Address!")
    except googlemaps.exceptions.ApiError as _:
        errDisplay.config(text="Error: Invalid Address!")
    global temp1
    global temp2
    temp1 = e1.get()
    temp2 = e2.get()
    e1.delete(0, 1000)
    e2.delete(0, 1000)


#get distance to destination
def timeanddistance_to_destination(distToDest, timeToDest):
    distToDest.set('Distance: ' + directions_result[0]['legs'][0]['distance']['text'])
    timeToDest.set('Travel Time: ' + directions_result[0]['legs'][0]['duration']['text'])

def location2(distToDest, timeToDest, errDisplay, mapDisplay, e1, e2, start, destination):
    try:
        location(start, destination, errDisplay, e1, e2)
        timeanddistance_to_destination(distToDest, timeToDest)
        mapDisplay.set_address(temp2)
    except NameError as _:
        errDisplay.config(text="Error: Please enter an address!")


def clearField(e1, e2):
    e1.delete(0, 250)
    e2.delete(0, 250)
    e1.config(fg="gray")
    e2.config(fg="gray")
    e1.insert(text="Start Location")
    e2.insert(text="End Destination")

#get directions
def directions():
    print('Directions:')
    # print('Travle Time:', directions_result[0]['legs'][0]['steps'][0]['html_instructions'])
    # print(directions_result)
    i = 0
    num_directions = len(directions_result[0]['legs'][0]['steps'])
    import re
    while i < num_directions:
        direction = directions_result[0]['legs'][0]['steps'][i]['html_instructions']

        # REMOVE HTML FORMATTING
        if 'style' in direction:
            direction = direction.replace('</b>', ' </b>')

        clean = re.compile('<.*?>')
        direction = re.sub(clean, '', direction)
        direction = direction.replace('Restricted usage road', '')
        direction = direction.replace('Toll road', 'Toll road ')
        direction = direction.replace('Entering', ' Entering')
        direction = direction.replace('  ', ' ')  # removes double spaces from doing replace('</b>', ' </b>')
        print('>', direction)
        i += 1


#get location
def geolocate():
    location = gmaps.geolocate()#returns coordinates
    x = location['location']['lat']
    z = location['location']['lng']
    cord = [x, z]
    loc = gmaps.reverse_geocode(cord)
    ('Your Location:', loc[0]['formatted_address'])


#adds a new favorite location
def add_fav_location(e3):
    with open('favorite_location', 'a') as file:
        new_location = e3.get()
        new_location = new_location + '\n'
        file.write(new_location)


#removes a new favorite location
def remove_fav_location():
    with open('favorite_location', 'r') as file:
        lines = file.readlines();
        for i in lines:
            print(i.replace("\n", " | ",), end='')
        print()
    with open('favorite_location', 'w') as file:
        remove = input('Location to remove: ')
        remove += '\n'
        for i in lines:
            if i != remove:
                file.write(i)
            else:
                print('removed:', remove)



#lists favorite locations
def fav_locations():
    print('Favorite Locations:')
    with open('favorite_location', 'r') as file:
        lines = file.readlines();
        for i in lines:
            print('>', i, end='')

