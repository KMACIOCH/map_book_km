import requests
import folium
from bs4 import BeautifulSoup

def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["post"]} post')



def add_user(lista:list) ->None:
    user_name = input('Podaj imie:')
    user_surename = input('Podaj nazwisko:')
    user_post = input('Podaj ile postów:')
    lista.append({'name': user_name,'surename': user_surename,'post':user_post})

def search(users: list[dict[str, str]])->None:
    user_name=input('Kogo szukasz?: ')
    for user in users[1:]:
        if user['name']==user_name:
            print(f'znaleziono użytkownika {user}')

def remove_user(users: list[dict[str, str]])->None:
    user_name=input('Kogo usunąć?: ')
    for user in users[1:]:
        if user['name']==user_name:
            print(f'znaleziono użytkownika {user['name']}')
            users.remove(user)
            remove_user(users)
def map_single_users(imie, postow, miasto:str):

    url=(f'https://pl.wikipedia.org/wiki/{miasto}')
    response=requests.get(url)
    response_html=BeautifulSoup(response.text,'html.parser')
    longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    print(longitude,latitude)
    map=folium.Map(location=[latitude,longitude],zoom_start=11)
    folium.Marker(location=[latitude,longitude],popup=f'{imie},postów: {postow},\n{miasto}',
    icon=folium.Icon(color='blue')).add_to(map)
    map.save(f'map_{miasto}.html')
def map_all_users(users, location=None):
    map = folium.Map(location=[52,20], zoom_start=6)
    for user in users:

    url=(f'https://pl.wikipedia.org/wiki/{user['location']}')
    response=requests.get(url)
    response_html=BeautifulSoup(response.text,'html.parser')
    longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    print(longitude,latitude)
    folium.Marker(location=[latitude,longitude],popup=f'{user['name']},postów: {user['location']},\nuser['location']}',
                    icon=folium.Icon(color='blue')).add_to(map)

    map.save(f'map.html')

