import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open("/Users/liaohaofan/Downloads/资料/可视化案例数据/地图数据/疫情.txt","r",encoding="UTF-8")
data = f.read()
f.close()
data_dict = json.loads(data)
henan_data = data_dict["areaTree"][0]["children"][3]["children"]
data_list = []
for city in henan_data:
    city_name = city["name"]+"市"
    city_confirm = city["total"]["confirm"]
    data_list.append((city_name,city_confirm))

data_list.append({"济源市",5})

# print(data_list)
map = Map()
map.add("COVID-19 Cases in Henan Province",data_list,"河南")
map.set_global_opts(
    title_opts=TitleOpts(title="Henan Province COVID-19 Map"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=(
            {"min":1,"max":99,"label":"1-99 cases","color":"#CCFFFF"},
            {"min":100,"max":199,"label":"100-199 cases","color":"#FFFF99"},
            {"min":200,"max":299,"label":"200-299 cases","color":"#FF9966"},
            {"min":300,"max":399,"label":"300-399 cases","color":"#CC3333"},
            {"min":400,"max":499,"label":"400-499 cases","color":"#990033"}

        )
    )
)

map.rend