#py08p09b_지도.py
import folium
import pandas as pd

# https://github.com/python-visualization/folium/tree/master 
# /examples/data에서 다음 두 개의 data file을 내려받는다
#geo_USA = "us-states.json"
URL = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
#URL="https://github.com/python-visualization/folium/tree/master/examples/data"
#state_geo = f"{URL}/us-states.json"
geo_USA = URL +"/us-states.json"
fcsv_name = "US_Unemployment_Oct2012.csv" 
data_USA = pd.read_csv(fcsv_name) # 저장할 때 utf-8 형식으로  
m = folium.Map(location=[48, -102], zoom_start=3) 
folium.Choropleth(geo_data=geo_USA, data=data_USA,
                  #name="choropleth",
                  key_on='feature.id', columns=['State', 'Unemployment'],
                  fill_color='YlGn',
                  fill_opacity=0.8, line_opacity=1,
                  legend_name='Unemployment Rate[%]'
                 ).add_to(m) 
m.save('py08p09b.html')
