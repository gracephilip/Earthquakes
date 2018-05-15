import gmplot
import csv
import random
from gmplot import *
import requests
import os
import time

import webbrowser


def plotting_function(my_lats, my_longs, my_mags ):
    apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

    data = []

    mymap = GoogleMapPlotter(0, 0, 3, apikey=apikey)  # lat, long, zoom_level, apikey=var


    # http://peterbird.name/oldFTP/PB2002/PB2002_plates.dig.txt
    # http://www.science20.com/news_articles/morvel_precise_model_tectonicplate_movements

    file = open('techtonic_plates.txt', 'r')

    for line in file:
        print(line.strip())

    file.close()

    plates = []


    for i in range(len(my_lats)):
        mymap.circle(my_lats[i], my_longs[i], my_mags[i]*10000, "#FF0000", ew=1) # lat, long, radius(m), web_color, edge_width=int


    mymap.draw('earthquakes_map.html')
    time.sleep(3)
    path = os.path.abspath("earthquakes_map.html")
    print(path)
    webbrowser.get("safari").open_new(path)


if __name__ == "__main__":
    '''main program goes here'''
    my_lats = [36.9902, 34.016, 14.4969]
    my_longs = [71.3687, -116.77983, 123.9312]
    my_mags = [6.2, 4.49, 6.1]
    plotting_function(my_lats, my_longs, my_mags)

