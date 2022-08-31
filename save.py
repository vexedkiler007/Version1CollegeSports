import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import codecs
from deffinistion_football_ import average_dif_oppenents
import time
def save_html(html,index):
    with open(f"{index}.html", "w") as file:
        file.write(html)


