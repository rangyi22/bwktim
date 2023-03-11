#py08p09a_지도.py
import folium
from geopy.geocoders import Nominatim

data = [['Fuqing','Hongyanhe','Ling Ao','Ningde','Qinshan','Tianwan','Yangjiang'],
        [4000,4244,3910,4072,4110,3960,6090]]
print(data) # 중국의 원자력발전소의 위치와 발전출력 규모에 관한 data
geolocator = Nominatim(user_agent='Your_API_key') 
m = folium.Map()
for i in range(len(data[0])):
   place, power = data[0][i], data[1][i]
   location = geolocator.geocode(place)
   lat, lon = location.latitude, location.longitude
   folium.Circle(location = [lat, ???], # 위도, 경도
                 popup = f'{place}: {power: 5.0f}MW' ,
                 radius = power*10,
                 #color='crimson', fill=True, fill_color='crimson'
                ).add_to(m)
m.save('py08p09a.html')
