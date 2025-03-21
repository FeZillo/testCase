import requests

# Variáveis
url = "https://two025-1a-t13-es05-api2.onrender.com/api/v1/institutions"
bearer_token = "g6-4b0f41f4314f91b5061681049da58c9454"
id_correto = "587"
id_inexistente = "99999"

headers = {
    "Authorization": f"Bearer {bearer_token}"
}

# Função para fazer GET
def send_get_request(endpoint):
    response = requests.get(endpoint, headers=headers)
    return response.status_code, response.json()

# Testes
def run_tests():
    # Requisição 1: GET com ID correto
    print("Requisição 1: GET com ID correto")
    status_code, data = send_get_request(f"{url}/{id_correto}/students/")
    if status_code == 200:
        print("Resultado esperado: Todos os alunos daquela unidade")
    else:
        print(f"Erro: {status_code} - {data}")

    # Requisição 2: GET com ID inexistente
    print("\nRequisição 2: GET com ID inexistente")
    status_code, data = send_get_request(f"{url}/{id_inexistente}/students/")
    if status_code == 404:
        print("Resultado esperado: Erro devido a ID inexistente")
    else:
        print(f"Erro: {status_code} - {data}")

    # Requisição 3: GET sem ID
    print("\nRequisição 3: GET sem ID")
    status_code, data = send_get_request(f"{url}/students/")
    if status_code == 400:
        print("Resultado esperado: Erro devido a ID não recebido")
    else:
        print(f"Erro: {status_code} - {data}")


if __name__ == "__main__":
    run_tests()
