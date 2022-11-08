import io
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox import service as fs
from selenium.webdriver.firefox.options import Options
from PIL import Image
import uuid

def amazonTrackingPrice(amazonURL):
    firefox_servie = fs.Service(executable_path="/code/linux_gecko/geckodriver")
    option = Options()
    option.add_argument('--headless')
    driver = webdriver.Firefox(service=firefox_servie, options=option)
    driver.get(amazonURL)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    imageName = str(uuid.uuid4())[-6:]
    itemName = soup.find(id="productTitle").get_text().strip()
    itemImage = soup.find(id="imgTagWrapperId").find("img", alt=itemName).get("src")
    nowPrice = soup.find("span", class_="a-price-whole").get_text().replace(",","")
    re = requests.get(itemImage)
    img_file = io.BytesIO(re.content)
    img_open = Image.open(img_file)
    img_open.save('templates/static/upload_to/' + imageName + '.png')

    return [itemName, 'templates/static/upload_to/' + imageName + '.png', nowPrice, amazonURL]
