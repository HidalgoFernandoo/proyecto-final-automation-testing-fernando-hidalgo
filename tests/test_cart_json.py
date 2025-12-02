from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

import time
RUTA_JSON = "datos/productos.json"

from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    try:
        logger.info(f"Relizando test de carrito con el producto: {nombre_producto}")
        driver = login_in_driver
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.agregar_producto_por_nombre(nombre_producto)
        logger.info(f"Agregando producto: {nombre_producto}")

        # Abrir el carrito
        logger.info("Abriendo carrito de compras")
        inventory_page.abrir_carrito()

        time.sleep(1)
        logger.info(f"Validando producto en el carrito: {nombre_producto}")
        # Validar el producto
        cartPage = CartPage(driver)

        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto
        

    except Exception as e:
        logger.info("Fallo en el test del carrito")
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()