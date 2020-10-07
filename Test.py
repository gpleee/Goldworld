<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/GL/Desktop/chromedriver.exe" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

=======
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "C:/Users/GL/Desktop/chromedriver.exe" # Your Chrome Driver path
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

>>>>>>> 357577a08fd34c0da72908a1c932ff307120a2f4
driver.get("https://www.naver.com/")