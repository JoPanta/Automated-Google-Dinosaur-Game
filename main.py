from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# to keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# setting up
driver = webdriver.Chrome(options=chrome_options)
# full page
driver.maximize_window()
driver.get('https://chromedino.com/')


# wait for elements to appear, if necessary
cookies = (WebDriverWait(driver, 10).until
           (EC.element_to_be_clickable((By.XPATH, '//*[@id="t"]/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]'))))
cookies.click()

canvas = driver.find_element(By.XPATH, value='//*[@id="main-frame-error"]/div[2]/canvas')
print(canvas.location, canvas.size)

# pressing space

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)


def is_color_present(image, target_color):
    # open image

    im = Image.open(BytesIO(image))

    # crop image
    cropped_img = im.crop((840, 180, 870, 220))

    # iterate through each pixel

    for x in range(cropped_img.width):
        for y in range(cropped_img.height):
            # Get the RGB values of the current pixel
            pixel_color = cropped_img.getpixel((x, y))

            if pixel_color == target_color:
                return True

    # If the target color is not found in the cropped image
    return False


target_color = (83, 83, 83, 255)

image = driver.get_screenshot_as_png()



while True:
    # saves screenshot of entire page
    image = driver.get_screenshot_as_png()

    result = is_color_present(image, target_color)
    if result:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)
    else:
        pass
