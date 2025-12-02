from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
        inventory_page = InventoryPage(driver)
        logger.info("agregando primer producto al carrito")

        # Agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        # Abrir el carrito
        logger.info("Abriendo carrito de compras")
        inventory_page.abrir_carrito()

        # Validar el producto
        logger.info(f"Validando producto en el carrito")
        cartPage = CartPage(driver)
        
        productos_en_carrito = cartPage.obtener_productos_carrito()
        assert len(productos_en_carrito) == 1

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()