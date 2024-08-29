Erick Torres Cohort 12 - Sprint 07
# Proyecto de Pruebas Urban Routes
> Urban Routes es una aplicación web automatizada que simula el proceso de pedir un taxi, desde la configuración de la ruta hasta la confirmación del conductor. El proyecto incluye pruebas automatizadas en `pytest`que cubren el flujo completo de la aplicación, asegurando que cada paso funcione correctamente. Estas pruebas son fundamentales para garantizar la calidad del software y una experiencia de usuario fluida.

## Contenido

1. [Estructura](#)
2. [Tecnologías y Técnicas Utilizadas](#)
3. [Comando para ejecurtar las pruebas](#)
4. [Como funciona cada prueba](#)

## 1. Estructura
- ### Archivo `data.py`
> A) Este archivo contiene datos que se utilizan en las pruebas automatizadas. Los datos están almacenados como variables globales que incluyen la URL de la aplicación web, direcciones de origen y destino, número de teléfono, detalles de la tarjeta de crédito y un mensaje para el conductor.
> 
> B) Variables importantes:
>  - `urban_routes_url`: URL de la aplicación.
>  - `address_from`: Dirección de origen.
>  - `address_to`: Dirección de destino.
>  - `phone_number`: Número de teléfono.
>  - `card_number, card_code`: Datos de la tarjeta de crédito.
>  - `message_for_driver`: Mensaje que se enviará al conductor.

- ### Archivo `UrbanRoutesPage.py`
> A) Este archivo sigue el patrón de diseño Page Object Model (POM), que organiza la estructura del código de manera que cada página web tenga su propia clase en la que se definen los elementos interactivos (localizadores) y los métodos para interactuar con ellos.
> 
> B) Localizadores: Cada elemento interactivo de la página (como botones, campos de texto, etc.) tiene un localizador definido utilizando selectores de Selenium como:
> - By.ID
> - By.CLASS_NAME
> - By.CSS_SELECTOR
> - etc
>
> C) Métodos: Se definen métodos que realizan acciones específicas en la página, como llenar formularios, hacer clic en botones, etc. Por ejemplo:
> - `set_from(self, from_address)`: Llena el campo "de" con la dirección proporcionada.
> - `click_taxi_button(self)`: Hace clic en el botón para seleccionar un taxi.
> - `insert_route(self, from_address, to_address)`: Combinación de métodos para llenar los campos de dirección y hacer clic en el botón de selección de taxi.

- ### Archivo `Helpers.py`
> A) Este archivo contiene funciones auxiliares que se utilizan durante las pruebas. En este caso, solo contiene una función:
> - `retrieve_phone_code(driver)`: Esta función intercepta y devuelve el código de confirmación del teléfono necesario para agregar un numero de telefono. Usa los registros de rendimiento de Selenium para obtener el código de confirmación desde la respuesta del servidor.

- ### Archivo `main.py`
> A) Este archivo contiene las pruebas automatizadas que verifican las diferentes funcionalidades de la aplicación Urban Routes. Las pruebas están organizadas en la clase `TestUrbanRoutes`, que sigue el patrón de `pytest` de Python.
>
> B) Métodos `setup_class` y `teardown_class`:
> - `setup_class(cls)`: Se ejecuta antes de que las pruebas comiencen. Configura el entorno de prueba, abre el navegador Chrome, lo maximiza y establece un tiempo de espera implícito.
> - `teardown_class(cls)`: Se ejecuta después de que todas las pruebas se han completado. Cierra el navegador.

## 2. Tecnologías y Técnicas Utilizadas

> - **Python 3.x**: Lenguaje de programación principal para escribir las pruebas automatizadas.
>
> 
> - **Selenium WebDriver**: Biblioteca para automatizar la interacción con la interfaz de usuario web.
> 
> 
> - **ChromeDriver**: Controlador para automatizar las pruebas en el navegador Google Chrome.
> 
> 
> - **Page Object Model (POM)**: Patrón de diseño utilizado para estructurar el código, facilitando la mantenibilidad y la reutilización de los componentes de la página web.
> 
> 
> - **Pytest**: Es un marco de pruebas en Python que permite escribir y ejecutar pruebas de manera simple y flexible, facilitando la verificación de la funcionalidad del código.

## 3. Comando para ejecurtar las pruebas

> Para ejecutar las pruebas se debe utilizar el comando: `pytest main.py`

## 4. Como funciona cada Método de prueba en `main.py`

### Método `test_insert_route(self)`
> A) Descripción: Esta prueba verifica que la funcionalidad de configurar la ruta funcione correctamente.
> 
> B) Funcionamiento:
> 
> - Navega a la URL de la aplicación.
> - Instancia un objeto de la clase `UrbanRoutesPage`.
> - Usa el método `insert_route` para ingresar la dirección de origen y destino.
> - Verifica que las direcciones ingresadas coincidan con las esperadas utilizando `assert`.

### Método `test_comfort_tariff(self)`
> A) Descripción: Verifica que la opción de seleccionar la tarifa Comfort funcione correctamente.
> 
> B) Funcionamiento:
> 
> - Llama al método `insert_comfort_tariff` para seleccionar la tarifa Comfort.
> - Verifica que el texto "Requisitos del pedido" esté presente para confirmar que la tarifa se ha seleccionado correctamente.

### Método `test_phone_number(self)`
> A) Descripción: Prueba la funcionalidad de ingresar un número de teléfono y confirmar el código recibido.
> 
> B) Funcionamiento:
> 
> - Llama al método `insert_phone_number` para ingresar el número de teléfono y confirmar el código.
> - Verifica que el número de teléfono ingresado coincida con el esperado.

### Método `test_payment_method(self)`
> A) Descripción: Verifica que la funcionalidad de agregar una tarjeta de crédito funcione correctamente.
> 
> B) Funcionamiento:
> - Llama al método `insert_payment_method` para ingresar los datos de la tarjeta y agregarla como método de pago.
> - Verifica que los datos de la tarjeta ingresados coincidan con los esperados.

### Método `test_message_for_driver(self)`
> A) Descripción: Prueba la funcionalidad de enviar un mensaje al conductor.
> 
> B) Funcionamiento:
> - Llama al método `set_message_for_driver` para ingresar un mensaje para el conductor.
> - Verifica que el mensaje ingresado coincida con el esperado.



### Método `test_blanket_on(self)`
> A) Descripción: Verifica que la opción de seleccionar manta y pañuelos funcione correctamente.
> 
> B) Funcionamiento:
> - Llama al método `click_blanket_slider` para activar la opción.
> - Verifica que el slider esté activado (valor True).

### Método `test_ice_cream_quantity(self)`
> A) Descripción: Prueba la funcionalidad de agregar helados al pedido.
> 
> B) Funcionamiento:
> - Llama al método `click_add_ice_cream` dos veces para agregar dos helados.
> - Verifica que la cantidad de helados agregados sea 2.

### Método `test_search_taxi_modal(self)`
> A) Descripción:  Verifica que el modal para buscar un taxi se muestre correctamente.
> 
> B) Funcionamiento:
> - Llama al método `click_search_taxi` para activar la búsqueda de un taxi.
> - Verifica que el modal de búsqueda esté visible.

### Método `test_payment_method(self)`
> A) Descripción: Prueba la funcionalidad de esperar y mostrar la información del conductor en el modal.
> 
> B) Funcionamiento:
> - Llama al método `get_info_taxi_modal` para esperar y verificar que la información del conductor se muestre en el modal.
> - Verifica que la información se haya mostrado correctamente.

















