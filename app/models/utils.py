from requests import get


def busca_logradouro(cep):
    try:
        response = get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 404: print('CEP não encontrado')
        return response.json()['logradouro']
    except:
        print('Erro ao buscar CEP')
