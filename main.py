from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO

# to keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# setting up
driver = webdriver.Chrome(options=chrome_options)
# full page
driver.maximize_window()
driver.get('https://chromedino.com/')
# wait for elements to appear, if necessary
driver.implicitly_wait(4)

cookies = driver.find_element(By.XPATH, value='//*[@id="t"]/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]')
cookies.click()
#
screen = driver.find_element(By.XPATH, value='//*[@id="main-frame-error"]')
# location = screen.location
# size = screen.size
left = 810
top = 330
right = left + 10
bottom = top + 10

# pressing space
actions = ActionChains(driver)
actions.send_keys(Keys.SPACE).perform()


while True:
    # saves screenshot of entire page
    png = driver.get_screenshot_as_png()
    # uses PIL library to open image in memory
    im = Image.open(BytesIO(png))
    # defines crop points
    im = im.crop((left, top, right, bottom))
    im.save('screenshot1.png') # saves new cropped image

    if not im.getbbox():
        im.save('screenshot2.png') # saves new cropped image