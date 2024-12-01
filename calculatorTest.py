from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Crear una función para manejar las capturas donde (name = nombre de la foto)  y (extension = extension de archivo sin el punto "."):
def makeScreenshot(name, extension):
    file_path = f"./capturas/{name}.{extension}"

    # Eliminar el archivo si ya existe
    if os.path.exists(file_path):
        os.remove(file_path)

    # Tomar la captura de pantalla
    driver.get_screenshot_as_file(file_path)

# Comprueba que existe la carpeta para capturas:
if not os.path.exists("capturas"):
    os.makedirs("capturas")

html_report = ""  # Variable global para el contenido principal

def start_html_report():
    global html_report
    # Agregar el contenido inicial del HTML
    html_report = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scientific_Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                background-color: #f9f9f9;
            }
            .test-result {
                background-color: #e0e0e0;
                border-radius: 8px;
                padding: 10px;
                margin: 10px 0;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            .test-result p {
                margin: 5px 0;
                font-size: 14px;
            }
            .test-result img {
                width: 100%;
                max-width: 500px;
                margin: 10px 0;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            .test-result img.before {
                border: 2px solid #4CAF50;
            }
            .test-result img.after {
                border: 2px solid #FF5722;
            }
        </style>
    </head>
    <body>
        <h1>Reporte de Pruebas - Calculadora Científica</h1>
    """
    # Crear o sobrescribir el archivo con el contenido inicial
    with open("reporte_pruebas.html", "w") as file:
        file.write(html_report)

def add_test_to_report(test_name, before_img, after_img):
    # Agregar solo el contenido de la prueba actual al archivo
    test_html = f"""
    <div class="test-result">
        <p><strong>{test_name}</strong></p>
        <p>Antes del resultado:</p>
        <img src="capturas/{before_img}.png" class="before">
        <p>Después del resultado:</p>
        <img src="capturas/{after_img}.png" class="after">
    </div>
    """
    # Añadir la nueva prueba al archivo existente sin reescribir el contenido previo
    with open("reporte_pruebas.html", "a") as file:
        file.write(test_html)

def finish_html_report():
    # Agregar el cierre del HTML
    closing_html = """
    </body>
    </html>
    """
    # Escribir el cierre al final del archivo
    with open("reporte_pruebas.html", "a") as file:
        file.write(closing_html)

# Empezamos el reporte HTML:
start_html_report()

# Configurar el WebDriver de Chrome:
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# Abrir pagina:
driver.get("https://warenjsm29.github.io/Scientific_Caculator_v2/")

# Esperamos que cargue bien la pagina:
waitForCalculatorPage = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "display")))
waitForCalculatorPage.clear()
makeScreenshot("00-DisplayTest", "png")

# Prueba de Suma: --------------------------------------------------------------------------------
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberNine = driver.find_element(By.CSS_SELECTOR, "input[value='9']").click()
operatorPlus = driver.find_element(By.CSS_SELECTOR, "input[value='+']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("01-SumTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("02-SumTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion de Suma:", "01-SumTestBeforeEqual", "02-SumTestAfterEqual")

# Prueba de Resta: --------------------------------------------------------------------------------
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberNine = driver.find_element(By.CSS_SELECTOR, "input[value='9']").click()
operatorMinus = driver.find_element(By.CSS_SELECTOR, "input[value='-']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("03-ResTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("04-ResTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion de Resta:", "03-ResTestBeforeEqual", "04-ResTestAfterEqual")

# Prueba de Multiplicación: --------------------------------------------------------------------------------
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
operatorMulti = driver.find_element(By.CSS_SELECTOR, "input[value='x']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("05-MultiTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("06-MultiTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion de Multiplicacion:", "05-MultiTestBeforeEqual", "06-MultiTestAfterEqual")

# Prueba de Division: --------------------------------------------------------------------------------
numberTwo = driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
operatorDiv = driver.find_element(By.CSS_SELECTOR, "input[value='÷']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("07-DivTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("08-DivTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion de Division:", "07-DivTestBeforeEqual", "08-DivTestAfterEqual")

# Prueba de Division por Zero: --------------------------------------------------------------------------------
numberTwo = driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
operatorDiv = driver.find_element(By.CSS_SELECTOR, "input[value='÷']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("09-DivZeroTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("10-DivZeroTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion de Division por Zero:", "09-DivZeroTestBeforeEqual", "10-DivZeroTestAfterEqual")

# Prueba de Operación Compleja: --------------------------------------------------------------------------------
numberTwo = driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
operatorPlus = driver.find_element(By.CSS_SELECTOR, "input[value='+']").click()
numberSix = driver.find_element(By.CSS_SELECTOR, "input[value='6']").click()
operatorDiv = driver.find_element(By.CSS_SELECTOR, "input[value='÷']").click()
numberThree = driver.find_element(By.CSS_SELECTOR, "input[value='3']").click()
operatorMulti = driver.find_element(By.CSS_SELECTOR, "input[value='x']").click()
numberTwo = driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
time.sleep(5)
makeScreenshot("11-OperationTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("12-OperationTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Operacion Combinada:", "11-OperationTestBeforeEqual", "12-OperationTestAfterEqual")

# Prueba de Raíz Cuadrada de 16: --------------------------------------------------------------------------------
sqrt = driver.find_element(By.CSS_SELECTOR, "input[value='√']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberSix = driver.find_element(By.CSS_SELECTOR, "input[value='6']").click()
time.sleep(5)
makeScreenshot("13-SqrtTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("14-SqrtTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Raiz cuadrada de 16:", "13-SqrtTestBeforeEqual", "14-SqrtTestAfterEqual")

# Prueba del Seno: --------------------------------------------------------------------------------
sinButton = driver.find_element(By.CSS_SELECTOR, "input[value='sin']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberThree = driver.find_element(By.CSS_SELECTOR, "input[value='3']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("15-SinTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("16-SinTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calcular el Seno de 30:", "15-SinTestBeforeEqual", "16-SinTestAfterEqual")

# Prueba del Coseno: --------------------------------------------------------------------------------
cosButton = driver.find_element(By.CSS_SELECTOR, "input[value='cos']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberThree = driver.find_element(By.CSS_SELECTOR, "input[value='3']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("17-CosTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("18-CosTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calcular el Coseno de 30:", "17-CosTestBeforeEqual", "18-CosTestAfterEqual")

# Prueba del Tangente: --------------------------------------------------------------------------------
tanButton = driver.find_element(By.CSS_SELECTOR, "input[value='tan']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberThree = driver.find_element(By.CSS_SELECTOR, "input[value='3']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("19-TanTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("20-TanTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calcular la Tangente de 30:", "19-TanTestBeforeEqual", "20-TanTestAfterEqual")

# Prueba del Pi: --------------------------------------------------------------------------------
piButton = driver.find_element(By.CSS_SELECTOR, "input[value='π']").click()
time.sleep(5)
makeScreenshot("21-PiTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("22-PiTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Valor de PI:", "21-PiTestBeforeEqual", "22-PiTestAfterEqual")

# Prueba del Logaritmo: --------------------------------------------------------------------------------
logButton = driver.find_element(By.CSS_SELECTOR, "input[value='log']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("23-LogTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("24-LogTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calcular Logaritmo de 10:", "23-LogTestBeforeEqual", "24-LogTestAfterEqual")

# Prueba del Logaritmo Natural: --------------------------------------------------------------------------------
lnButton = driver.find_element(By.CSS_SELECTOR, "input[value='ln']").click()
dirLeft = driver.find_element(By.CSS_SELECTOR, "input[value='←']").click()
numberOne = driver.find_element(By.CSS_SELECTOR, "input[value='1']").click()
numberZero = driver.find_element(By.CSS_SELECTOR, "input[value='0']").click()
time.sleep(5)
makeScreenshot("25-LnTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("26-LnTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calcular el Logaritmo Natural de 10:", "25-LnTestBeforeEqual", "26-LnTestAfterEqual")

# Prueba de Potencias: --------------------------------------------------------------------------------
numberFive = driver.find_element(By.CSS_SELECTOR, "input[value='5']").click()
powButton = driver.find_element(By.CSS_SELECTOR, "input[value='^']").click()
numberTwo = driver.find_element(By.CSS_SELECTOR, "input[value='2']").click()
time.sleep(5)
makeScreenshot("27-PowTestBeforeEqual", "png")
operatorEqual = driver.find_element(By.CSS_SELECTOR, "input[value='=']").click()
makeScreenshot("28-PowTestAfterEqual", "png")
time.sleep(5)

# Borramos la pantalla de la calculadora:
buttonAC = driver.find_element(By.CSS_SELECTOR, "input[value='AC']").click()

# Hacemos el reporte al HTML:
add_test_to_report("Calculamos 5 elevado al cuadrado:", "27-PowTestBeforeEqual", "28-PowTestAfterEqual")

# Terminamos las pruebas y cerramos el driver: --------------------------------------------------------------------------------

# Termino el reporte HTML:
finish_html_report()

# Terminar la prueba automatizada:
input("Pulsa Enter para terminar la prueba...")
driver.quit()
