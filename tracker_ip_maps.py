import requests
import json
import folium

def tracker_ip():    
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print('Não foi possível obter a localização.')
    else:
        ip = json.loads(r.text)
        cidade = json.loads(r.text)
        regiao = json.loads(r.text)
        pais = json.loads(r.text)
        uf = json.loads(r.text)
        continente = json.loads(r.text)
        latitude = json.loads(r.text)
        longitude = json.loads(r.text)
        timezone = json.loads(r.text)

        print('\nSeus dados: ')
        print('IP: ' + ip['geoplugin_request'])
        print('Cidade: ' + cidade['geoplugin_city'])
        print('Região: ' + regiao['geoplugin_region'])
        print('País: ' + pais['geoplugin_countryName'])
        print('UF: ' + uf['geoplugin_region'])
        print('Continente: ' + continente['geoplugin_continentName'])
        print('Latitude: ' + latitude['geoplugin_latitude'])
        print('Longitude: ' + longitude['geoplugin_longitude'])
        print('Timezone: ' + timezone['geoplugin_timezone'])
        print('\n')

        arquivo = open('data.txt','w')
        arquivo.write('IP: ' + ip['geoplugin_request']+"\n")
        arquivo.write('Cidade: ' + cidade['geoplugin_city']+"\n")
        arquivo.write('Região: ' + regiao['geoplugin_region']+"\n")
        arquivo.write('País: ' + pais['geoplugin_countryName']+"\n")
        arquivo.write('UF: ' + uf['geoplugin_region']+"\n")
        arquivo.write('Continente: ' + continente['geoplugin_continentName']+"\n")
        arquivo.write('Latitude: ' + latitude['geoplugin_latitude']+"\n")
        arquivo.write('Longitude: ' + longitude['geoplugin_longitude']+"\n")
        arquivo.write('Timezone: ' + timezone['geoplugin_timezone']+"\n")
        arquivo.close()

def get_map():
    r = requests.get('http://www.geoplugin.net/json.gp')
    latitude = json.loads(r.text)
    longitude = json.loads(r.text)
    mapa = folium.Map(
        location=[latitude['geoplugin_latitude'],longitude['geoplugin_longitude']], 
        zoom_start=15)
    folium.Marker(
        location=[latitude['geoplugin_latitude'], longitude['geoplugin_longitude']], 
        popup='Você está aqui.').add_to(mapa)
    folium.CircleMarker(
        location=[latitude['geoplugin_latitude'], longitude['geoplugin_longitude']],
        radius=50,
        popup='Você está aqui.',
        color='blue',
        fill=True,
        fill_color='blue').add_to(mapa)
    mapa.add_child(folium.LatLngPopup())
    mapa.save('mapa.html')


tracker_ip()
get_map()