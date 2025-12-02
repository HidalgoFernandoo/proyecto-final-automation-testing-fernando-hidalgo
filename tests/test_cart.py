from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger


@pytest.mark.parametrize("usuario,password", [("standard_user", "secret_sauce")])
def test_cart(login_in_driver, usuario, password):

    driver = login_in_driver

    try:
        logger.info("Agregando primer producto al carrito")
        inventory_page = InventoryPage(driver)

        # Agregar primer producto
        inventory_page.agregar_primer_producto()

        # Abrir el carrito
        logger.info("Abriendo carrito de compras")
        inventory_page.abrir_carrito()

        # Validar el producto en carrito
        logger.info("Validando producto en el carrito")
        cartPage = CartPage(driver)
        productos_en_carrito = cartPage.obtener_productos_carrito()

        assert len(productos_en_carrito) == 1, \
            f"Se esperaba 1 producto en el carrito, pero se encontraron {len(productos_en_carrito)}"

    except Exception as e:
        logger.error(f"Error en test_cart: {e}")
        raise

    finally:
        logger.info("Cerrando driver en test_cart")
        driver.quit()
