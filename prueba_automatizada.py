import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select


class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\driver_chrome\chromedriver.exe" ) 
        

    def test_automatizado(self):
        driver = self.driver        
        driver.get("https://www.choucairtesting.com/")
        driver.maximize_window()
        time.sleep(2)

        contactenos = driver.find_element_by_xpath("//*[@id='menu-item-282']/a")	
        contactenos.click()
        time.sleep(2)


        driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='0100fdf3-ff82-446d-8be0-063723163749']"))
        tema_de_interes=Select(driver.find_element_by_id("d5a52985-66b2-ea11-a812-000d3ac166cd"))
        tema_de_interes.select_by_value("704240000")

        nombre = driver.find_element_by_xpath("//*[@id='3f746946-34b4-442c-a677-e232cdd2bc40']")
        nombre.send_keys("YEISSON CLAROS")

        apellido=driver.find_element_by_xpath("//*[@id='e1dfc514-f301-4cb2-855a-4c8fa8331207']")
        apellido.send_keys("CLAROS GRANDETT")

        correo_electronico=driver.find_element_by_xpath("//*[@id='7f685ebb-7c54-4cff-a1bc-772562d25c38']")
        correo_electronico.send_keys("clarosyeisson@gmail.com")

        ciudad=driver.find_element_by_xpath("//*[@id='a70f881b-ef95-ea11-a812-000d3ac166cd']")
        ciudad.send_keys("Neiva")
        ciudad.send_keys(Keys.ARROW_DOWN)
        ciudad.click()

        time.sleep(3)

        empresa=driver.find_element_by_xpath("//*[@id='ac9ddb60-616f-4f12-b4e2-9202f688ed2f']")
        empresa.send_keys("choucair")

        celular=driver.find_element_by_xpath("//*[@id='08362b8f-b4ff-4d47-bc08-9b25a7e81e95']")
        celular.send_keys("3182298162")

        mensaje=driver.find_element_by_xpath("//*[@id='2048d706-a094-ea11-a812-000d3ac166cd']")
        mensaje.send_keys("haciendo prueba qa")

        aceptar_politica= driver.find_element_by_xpath("/html/body/div[1]/div/form/div/div[5]/div/div[2]/div/div/div/input")	
        aceptar_politica.click()

        enviar = driver.find_element_by_name("submit")
        time.sleep(10)
        enviar.click()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
	unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultado de mi test, con TestRunner'))