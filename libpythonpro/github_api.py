import requests

def buscar_avatar(usuario):
    """
    Buscar o avatar de um usuário no Github
    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url) # Requisição de URL na variável url.
    return resp.json()['avatar_url'] #Chave contendo a ulr "https://avatars.githubusercontent.com/u/61337568?v=4"

#Confirmando a requisição.
#Usando a propriedade __name__ devido importação de módulos:
if __name__ == '__main__':
    print(buscar_avatar('jeferson777')) #Usuário github