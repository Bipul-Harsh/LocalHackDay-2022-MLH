from geopy.geocoders import Nominatim
from geopy.distance import great_circle

geolocator = Nominatim(user_agent="MLH_Task")

def get_geolocation(PIN):
    '''
    Return the geolocation of the given PIN

    Arguments:
        PIN {str} -- PIN code of the location
    
    Returns:
        tuple -- tuple of latitude, longitude and address.
    '''
    location = geolocator.geocode(PIN)
    if not location:
        print("Invalid PIN")
    return (location.latitude, location.longitude, location.address)

def find_distance(source_geolocation, dest_geolocation):
    '''
    Return the distance between two locations
    
    Arguments:
        source_geolocation {tuple} -- tuple of latitude, longitude and address
        dest_geolocation {tuple} -- tuple of latitude, longitude and address
    
    Returns:
        float -- distance between two locations in kms.
    '''
    dist = great_circle(source_geolocation[:2], dest_geolocation[:2]).km
    return round(dist, 2)

if __name__ == "__main__":
    try:
        source = int(input("Enter source city PIN Code : "))
        destination = int(input("Enter destination city PIN Code: "))
    except ValueError:
        print("Please enter valid PIN Code")

    source_geolocation = get_geolocation(source)
    destination_geolocation = get_geolocation(destination)
    
    print(f'\nSource Location : {source_geolocation[2]}')
    print(f'Destination Location : {destination_geolocation[2]}')
    print(f'\nDistance between source and destination is {find_distance(source_geolocation, destination_geolocation)} Km')