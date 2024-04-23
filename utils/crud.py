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

