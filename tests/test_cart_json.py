from selenium import webdriver
import pytest
import time

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos
from utils.logger import logger

RUTA_JSON = "datos/productos.json"


@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])
@pytest.mark.parametrize("nombre_producto", leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver, usuario, password, nombre_producto):
    driver = login_in_driver

    try:
        logger.info(f"Realizando test de carrito con el producto: {nombre_producto}")

        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        logger.info(f"Agregando producto: {nombre_producto}")
        inventory_page.agregar_producto_por_nombre(nombre_producto)

        # Abrir el carrito
        logger.info("Abriendo carrito de compras")
        inventory_page.abrir_carrito()

        time.sleep(1)

        # Validar el producto
        logger.info(f"Validando producto en el carrito: {nombre_producto}")
        cartPage = CartPage(driver)

        assert cartPage.obtener_nombre_producto_carrito() == nombre_producto, \
            f"El producto en el carrito no coincide: se esperaba '{nombre_producto}'"

    except Exception as e:
        logger.error(f"Fallo en test_cart_json con producto '{nombre_producto}': {e}")
        raise

    finally:
        logger.info("Cerrando driver en test_cart_json")
        driver.quit()
