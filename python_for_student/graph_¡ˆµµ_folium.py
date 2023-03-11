#graph_지도_folium.py
#> pip install folium
import folium
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='Your_API_key') 
places = ['국립현충원','숭실대학교','노들역'] # 관심장소 모음 list
m = folium.Map()
locs = [] # 위 places에 담긴 지점들의 좌표들을 담을 list
for place in places: 
   location = geolocator.geocode(place)
   lat, lon = location.latitude, location.longitude
   locs.append((lat,lon)) 
   folium.Marker([lat,lon], tooltip=place).add_to(m)
# locs list에 담긴 좌표에 표현된 지점을 직선으로 연결한다.
folium.PolyLine(locations=locs).add_to(m) 
# 중앙대학교의 위치를 표시한다. 
loc_CAU = geolocator.geocode('중앙대정문')
lat_CAU, lon_CAU = loc_CAU.latitude, loc_CAU.longitude
folium.Marker([lat_CAU,lon_CAU],
                 tooltip='<b>'+'중앙대학교'+'</b>', # HTML 문자열
                 popup="중앙대정문",              
                 icon=folium.Icon(color='red')).add_to(m)
m.save('map.html')
