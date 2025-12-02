# Automatización de pruebas para SauceDemo

Este proyecto automatiza pruebas funcionales de UI y API para el sitio **SauceDemo**, aplicando el modelo Page Object, manejo de datos externos, captura de imagenes, generación de reportes HTML y logs.

## Tecnologías utilizadas
- Python 3.x
- Pytest
- Selenium WebDriver
- Requests
- Faker
- Manejo de datos en CSV y JSON
- Logging estándar de Python

## Estructura del proyecto
- `pages/`: Page Objects con los flujos de navegación y acciones sobre la UI.
- `tests/`: Casos de prueba de UI y API.
- `datos/`: Datos de prueba en formatos CSV y JSON.
- `utils/`: Utilidades como la configuración de logging.
- `assets/`: Recursos auxiliares (por ejemplo, capturas o archivos estáticos).
- `run_tests.py`: Lanzador principal que ejecuta el conjunto de pruebas y genera el reporte HTML.
- `logs/`: Carpeta donde se persiste el archivo `suite.log` con el detalle de ejecución.
- `report.html`: Reporte HTML generado tras la última ejecución de pruebas.

## Instalación de dependencias
1. Clona el repositorio y entra al proyecto.
   ```bash
   git clone <url-del-repositorio>
   cd entrega-final-automation
   ```
2. (Opcional) Crea y activa un entorno virtual.
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
   ```
3. Instala las dependencias.
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de pruebas
Ejecuta todas las pruebas y genera un reporte HTML autocontenido en la raíz del proyecto:
```bash
python run_tests.py
```

## ¿Cómo interpretar los reportes generados?
- **Reporte HTML (`report.html`)**: muestra el detalle de cada prueba (estado, duración y trazas). Se puede abrir en cualquier navegador y queda en la raíz del proyecto tras la ejecución.
- **Logs (`logs/suite.log`)**: registra la cronología y mensajes de las pruebas; útil para depurar.
- **Evidencias**: las capturas u otros artefactos se almacenan en `assets/` cuando los tests las producen.

## Control de Versiones y Documentación
- **Repositorio en GitHub**: sube el proyecto a GitHub y mantén un historial de commits que describa claramente cada avance.
- **Ramas de trabajo**: desarrolla nuevas funcionalidades en ramas específicas y fusiónalas con la rama principal mediante pull requests.
- **README.md**: conserva este archivo actualizado con el propósito, tecnologías, estructura, instrucciones de instalación, ejecución de pruebas e interpretación de reportes.

## Alcance de las pruebas incluidas
- Autenticación (casos exitosos y fallidos, incluidos datos generados con Faker).
- Flujo de inventario y carrito de compras.
- Pruebas de API contra el servicio ReqRes (GET, POST, DELETE y validaciones de códigos de estado y estructura JSON).

## Datos de prueba
- `datos/data_login.csv`: credenciales válidas e inválidas para los casos de login.
- `datos/productos.json`: información de productos utilizada en validaciones.

## Notas
- El reporte y los logs se sobreescriben con cada ejecución; respáldalos si necesitas conservar ejecuciones anteriores.

##
- Actualizado por Fernando Hidalgo 02/12/2025