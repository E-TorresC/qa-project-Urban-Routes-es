from selenium.webdriver.common.by import By
import data
import Helpers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:
    # Selectores de Interaccion 1 : colocar direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    select_taxi_button = (By.CLASS_NAME, 'button.round')

    # Selectores de Interaccion 2: Seleccionar tarifa comfort
    comfort_tariff_icon = (By.CSS_SELECTOR, "div.tcard:nth-child(5)>div:nth-child(3)")
    to_test_comfort_tariff = (By.CLASS_NAME, 'r-sw-label')

    # Selectores de Interaccion 3: Colocar numero de telefono
    phone_field = (By.CLASS_NAME, 'np-button')
    input_phone_number = (By.ID, 'phone')
    select_phone_number_send_button = (By.CLASS_NAME, "button.full")
    input_phone_code = (By.ID, 'code')
    select_confirm_code_button = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    to_test_phone_number = (By.CLASS_NAME, 'np-text')

    # Selectores de Interaccion 4: Agregar numero tarjeta
    payment_method_field = (By.CLASS_NAME, 'pp-value')
    select_payment_method = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled > div.pp-title')
    input_card_number = (By.CLASS_NAME, 'card-input')
    input_card_code = (By.CSS_SELECTOR, '#code.card-input') #CAMBIO SEGUN LA SUGERENCIA
    blank_space = (By.CLASS_NAME, 'pp-buttons')
    select_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    select_payment_method_close_button = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
    to_test_payment_text = (By.CLASS_NAME, 'pp-value-text') #CAMBIO SEGUN LA SUGERENCIA
    to_test_card_code = (By.CSS_SELECTOR, '#code.card-input') #CAMBIO SEGUN LA SUGERENCIA

    # Selectores de Interaccion 5: Mensaje al conductor
    input_comment_driver = (By.ID, 'comment')

    # Selectores de Interaccion 6: Seleccionar Manta Pañuelos
    select_blanket_slider = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div')
    to_test_blanket_slider_on = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')

    # Selectores de Interaccion 7: Agreagr Helados
    select_ice_cream_add_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    to_test_ice_cream_quantity = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')

    # Selectores de Interaccion 8: Buscar Taxi-Modal
    select_search_taxi_button = (By.CLASS_NAME, 'smart-button')
    to_test_search_taxi_modal = (By.CLASS_NAME, 'order-buttons')

    # Selectores de Interaccion 9: Esperar informacion del taxi
    to_test_detail_taxi = (By.CLASS_NAME, 'order-btn-rating')


    def __init__(self, driver):
        self.driver = driver

    # Interaccion 1: Configurar la dirección
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_taxi_button(self):
        self.driver.find_element(*self.select_taxi_button).click()

    def insert_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_taxi_button()

    # Interaccion 2: Seleccionar tarifa comfort
    def click_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff_icon).click()

    def get_comfort_tariff(self):
        return self.driver.find_element(*self.to_test_comfort_tariff).text

    def insert_comfort_tariff(self):
        self.click_comfort_tariff()

    # Interaccion 3: Colocar numero de telefono
    def click_phone_field(self):
        self.driver.find_element(*self.phone_field).click()

    def set_phone_number(self):
        self.driver.find_element(*self.input_phone_number).send_keys(data.phone_number)

    def click_phone_number_send_button(self):
        self.driver.find_element(*self.select_phone_number_send_button).click()

    def set_phone_code(self):
        self.driver.find_element(*self.input_phone_code).send_keys(Helpers.retrieve_phone_code(self.driver))

    def click_confirm_code_button(self):
        self.driver.find_element(*self.select_confirm_code_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.to_test_phone_number).text

    def insert_phone_number(self):
        self.click_phone_field()
        self.set_phone_number()
        self.click_phone_number_send_button()
        self.set_phone_code()
        self.click_confirm_code_button()

    # Interaccion 4: Agregar numero tarjeta
    def click_payment_method_field(self):
        self.driver.find_element(*self.payment_method_field).click()

    def click_add_payment_method(self):
        self.driver.find_element(*self.select_payment_method).click()

    def set_card_number(self):
        self.driver.find_element(*self.input_card_number).send_keys(data.card_number)

    def set_car_code(self):
        self.driver.find_element(*self.input_card_code).send_keys(data.card_code)

    def click_outside(self):
        self.driver.find_element(*self.blank_space).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.select_card_button).click()

    def click_close_payment_method(self):
        self.driver.find_element(*self.select_payment_method_close_button).click()

    def get_for_test_payment_text(self):
        return self.driver.find_element(*self.to_test_payment_text).text

    def get_for_test_card_code(self):
        return self.driver.find_element(*self.to_test_card_code).get_property('value')

    def insert_payment_method(self):
        self.click_payment_method_field()
        self.click_add_payment_method()
        self.set_card_number()
        self.set_car_code()
        self.click_outside()
        self.click_add_card_button()
        self.click_close_payment_method()

    # Interaccion 5: Mensaje al conductor
    def set_message_for_driver(self):
        self.driver.find_element(*self.input_comment_driver).send_keys(data.message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.input_comment_driver).get_property('value')

    # Interaccion 6: Seleccionar Manta Pañuelos
    def click_blanket_slider(self):
        self.driver.find_element(*self.select_blanket_slider).click()

    def get_blanket_slider(self):
        return self.driver.find_element(*self.to_test_blanket_slider_on).is_selected()

    # Interaccion 7: Agreagr Helados
    def click_add_ice_cream(self):
        self.driver.find_element(*self.select_ice_cream_add_button).click()
        self.driver.find_element(*self.select_ice_cream_add_button).click()

    def get_ice_cream_quantity(self):
        return self.driver.find_element(*self.to_test_ice_cream_quantity).text

    # Interaccion 8: Buscar Taxi-Modal
    def click_search_taxi(self):
        self.driver.find_element(*self.select_search_taxi_button).click()

    def get_search_taxi_modal(self):
        return self.driver.find_element(*self.to_test_search_taxi_modal).is_displayed()

    # Interaccion 9: Esperar informacion del taxi
    def get_info_taxi_modal(self):
        WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(self.to_test_detail_taxi))
        return self.driver.find_element(*self.to_test_detail_taxi).is_displayed()