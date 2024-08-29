from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from UrbanRoutesPage import UrbanRoutesPage
import data

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)

    # Prueba 1: Configurar la dirección (test: 'from'  'to')
    def test_insert_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.insert_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Prueba 2: Seleccionar tarifa comfort (Test: 'reqs-head')
    def test_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.insert_comfort_tariff()
        assert routes_page.get_comfort_tariff() == 'Requisitos del pedido'

    # Prueba 3: Insertar numero de telefono ( Test: Phone number )
    def test_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.insert_phone_number()
        assert routes_page.get_phone_number() == data.phone_number

    # Prueba 4: Agregar numero tarjeta ( Test: card Number / card code)
    def test_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.insert_payment_method()
        assert  routes_page.get_for_test_card_number() == data.card_number
        assert routes_page.get_for_test_card_code() == data.card_code

    # Prueba 5: Mensaje al conductor ( Test: message for driver de data.py)
    def test_message_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver()
        assert routes_page.get_message_for_driver() == data.message_for_driver

    # Prueba 6: Seleccionar Manta Pañuelos ( Test: icono este ON )
    def test_blanket_on(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_slider()
        assert routes_page.get_blanket_slider() == True

    # Prueba 7: Agreagr Helados ( Test: Cantidad de helados es 2)
    def test_ice_cream_quantity(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_ice_cream()
        assert routes_page.get_ice_cream_quantity() == '2'

    # Interaccion 8: Buscar Taxi-Modal ( Test: Se muestra el modal
    def test_search_taxi_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_search_taxi()
        assert routes_page.get_search_taxi_modal() == True
        WebDriverWait(self.driver,5)

    # Interaccion 9: Esperar informacion del taxi ( Test: Verificar info del taxista - rating )
    def test_info_taxi_modal(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.get_info_taxi_modal() == True
        WebDriverWait(self.driver,5)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
