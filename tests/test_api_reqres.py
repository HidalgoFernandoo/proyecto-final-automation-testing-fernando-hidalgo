import requests
import pytest
from utils.logger import logger

# Obtener usuario
def test_get_user(url_base,header_request):
    logger.info(f"Relizando la solitud GET a {url_base} ")
    response = requests.get(f"{url_base}/2",headers=header_request)

    logger.info(f"Status code: {response.status_code}")
    assert response.status_code == 200

    data = response.json()

    logger.info("Validando el id dentro del usuario")
    assert data["data"]["id"] == 2
# Crear usuario
def test_create_user(url_base,header_request):
    payload={
        "name": "Jose",
        "job": "Profesor"
    }
    response = requests.post(url_base,headers=header_request,json=payload)
    logger.info("Realizando la solicitud POST para crear un usuario")

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == payload["name"]
    logger.info("Usuario creado correctamente")

# Eliminar usuario
def test_delete_user(url_base,header_request):
    logger.info("Realizando la solicitud DELETE para eliminar un usuario")
    response = requests.delete(f"{url_base}/2",headers=header_request)

    assert response.status_code == 204
    logger.info("Usuario eliminado correctamente")
