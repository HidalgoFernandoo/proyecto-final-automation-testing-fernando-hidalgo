import pytest


@pytest.mark.ui
@pytest.mark.xfail(reason="Fallo intencional para validar la captura de pantalla", strict=False)
@pytest.mark.usefixtures("driver")
def test_forces_screenshot_on_failure(driver):
    """Forzar un fallo para comprobar la captura automática de screenshots sin romper la ejecución."""
    driver.get("https://www.saucedemo.com/")
    assert False, "Fallo intencional para validar la captura de pantalla"
