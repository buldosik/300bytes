import folium # library for maps
import time
import csv

arr = []
rows = []

#instead of csv we had to use sql databases
with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        arr.append(row)

larr = len(arr) + 1

while True:

    #send request to database
    #arr=database

    if len(arr) == larr:
        # if nothing has chached, map is not generated again
        larr=len(arr)
        time.sleep(60)
        continue
    
     
    #Map generate
    m = folium.Map(location=[51.107883, 17.038538], zoom_start=10) #wroclaw location
    
    
    for i in range(1, len(arr)):
        if arr[i][1] == "Sport":
            folium.Marker(
                [arr[i][2], arr[i][3]],
                popup= arr[i][0],
                icon=folium.Icon(color="blue", icon="heart")).add_to(m)
        elif arr[i][1] == "Restaurant":
            folium.Marker(
                [arr[i][2], arr[i][3]],
                popup= arr[i][0],
                icon=folium.Icon(color="red", icon="cutlery")).add_to(m)
        elif arr[i][1] == "Museum":
            folium.Marker(
                [arr[i][2], arr[i][3]],
                popup= arr[i][0],
                icon=folium.Icon(color="green", icon="book")).add_to(m)
    
    m.save("EF_map.html")
    larr = len(arr)
    time.sleep(5)