# With this file we will be scraping from the US Geological survey
# written by Zoë starting on May 11


def get_data(intensity, time):

    '''
    this function gathers the data necessary for plotting based on the criteria
    given by the user
    :return:
    latitude, longitude and depth for the given earthquakes
    '''

    import requests
    import csv

    # this portion of the code gets the data based on the time specifications of the user
    if time == 30:
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
    elif time == 7:
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.csv'
    elif time == 1:
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
    else:
        url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv'

    response = requests.get(url)
    reader = csv.reader(response.text.strip().split('\n'))
    data = list(reader)

    # setting up the data so it can be used
    data.pop(0)
    data.sort(key=lambda x: float(x[4]))


    # forming the lists that will be passed
    latitudes_for_plotting = []
    longitudes_for_plotting = []
    magnitudes_for_plotting = []

    # filling the lists with the data
    for i in range(len(data)):
        if float(data[i][4]) >= intensity:
            latitudes_for_plotting.append(float(data[i][1]))
            longitudes_for_plotting.append(float(data[i][2]))
            magnitudes_for_plotting.append(float(data[i][4]))

    return longitudes_for_plotting, latitudes_for_plotting, magnitudes_for_plotting




