#py08p09c_지도.py
import folium, json
import pandas as pd

# https://github.com/PinkWink/DataScience/tree/master/data
fgeo_json = "seoul_municipalities_geo.json" # 한글을 포함한 json
geo_Korea = json.load(open(fgeo_json, encoding='utf-8-sig'))
fcsv_name = "서울구별인구.csv"
서울구별인구 = pd.read_csv(fcsv_name) # 저장할 때 utf-8 형식으로  
#지도 중앙의 초기치로 서울시의 위도/경도를 넣고 각구별경계선이 그려지도록
m = folium.Map(location=[37.5502, 126.982], zoom_start=11,    
               tiles='Stamen Toner') #tiles='Mapbox Bright')
folium.Choropleth(geo_data=geo_Korea, data = 서울구별인구, 
                  key_on='feature.properties.SIG_KOR_NM',
                  columns = ['구별', '인구수'],
                  fill_opacity=0.7, line_opacity=0.5,
                  legend_name='서울의 구별 인구수[명]'
                 ).add_to(m)
folium.LayerControl().add_to(m)
m.save('py08p09c.html')
