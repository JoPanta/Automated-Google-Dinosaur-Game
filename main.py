from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import ImageGrab, ImageOps
from time import sleep


# to keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# setting up
driver = webdriver.Chrome(options=chrome_options)
# full page
driver.maximize_window()
driver.get('https://chromedino.com/')

dino = (649, 303, 700, 350)
box = (780, 298, 820, 345)

cookies = driver.find_element(By.XPATH, value="/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]")
cookies.click()


def take_print():
    sleep(0.02)
    bbox = (box[0], box[1], box[2], box[3])
    image = ImageGrab.grab(bbox)
    gray = ImageOps.grayscale(image)
    # image.save("box.png")
    # color = gray.getcolors()
    total = sum(map(sum, gray.getcolors()))
    return total

print(take_print())

def jump():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.SPACE)


def main():
    jump()
    while True:
        take_print()
        if take_print() < 2100 or take_print() > 2200:
            jump()


if __name__ == "__main__":
    main()

print(take_print())
