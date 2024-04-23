users: list[dict[str, str]]= [
    {'name':'Staś','surename':'Grzymski','post':1},
    {'name':'Kacper','surename':'Macioch','post':2},
    {'name':'Michał','surename':'Krzywiński','post':3},
    {'name':'Tymon','surename':'Leszczyc','post':2},
    {'name':'Michał','surename':'Lębryk','post':2},
]
print(f'witaj {users[0]["name"]}')

def read(users: list[dict[str, str]])->None:
    for user in users[1:]:
        print(f'twój znajomy {user["name"]} opublikował {user["post"]} post')

read(users)

