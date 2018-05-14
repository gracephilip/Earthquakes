import gmplot
import csv
import random
from gmplot import *
import requests

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

data = []

mymap = GoogleMapPlotter(0, 0, 3, apikey=apikey)  # lat, long, zoom_level, apikey=var

# http://peterbird.name/oldFTP/PB2002/PB2002_plates.dig.txt
# http://www.science20.com/news_articles/morvel_precise_model_tectonicplate_movements




#my_lats = [x/50 for x in range(10)]
#my_longs = [x/50 for x in range(10)]
#mag = [float(x) for x in range(10)]



my_lats = [36.9902, 34.016, 14.4969]
my_longs = [71.3687, -116.77983, 123.9312]
my_mags = [6.2, 4.49, 6.1]
#mymap.polygon(my_lats, my_longs, fc="yellow", ew=5, ec="red") #lats, longs, color, face color, edge width, edge color
#mymap.plot(my_lats, my_longs, "blue")



file = open('techtonic_plates.txt', 'r')

for line in file:
    print(line.strip()



file.close()

plates = []



'''
lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]
size = [random.randrange(1, 500) for x in data]
'''



for i in range(len(my_lats)):
    mymap.circle(my_lats[i], my_longs[i], my_mags[i]*10000, "#FF0000", ew=1) # lat, long, radius(m), web_color, edge_width=int





#for i in range(len(lats)):
    #mymap.circle(lats[i], longs[i], size[i])

#mymap.heatmap(my_lats, my_longs, maxIntensity=7, radius=15, dissipating=False)


mymap.draw('new_mymap.html')