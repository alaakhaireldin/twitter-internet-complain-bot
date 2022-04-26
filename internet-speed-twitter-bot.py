import main
import time
from selenium.webdriver.common.keys import Keys

print(main.username)
print(type(main.username))

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = main.webdriver.Chrome(executable_path=driver_path)
        self.upload = 0
        self.download = 0
    def Get_internet_speed(self):
        self.driver.get(main.test_speed)

        time.sleep(5)

        consent = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]').click()
        go_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        time.sleep(60)

        self.download = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.upload = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


    def tweet_at_provider(self):
        self.driver.get(main.twitter_link)

        time.sleep(4)

        self.email_or_username = self.driver.find_element_by_name('text')
        self.email_or_username.send_keys(main.username)
        self.email_or_username.send_keys(Keys.ENTER)

        time.sleep(2)

        self.password = self.driver.find_element_by_name('password')
        self.password.send_keys(str(main.password))
        self.password.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet_compose = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey Internet Provider, why is my internet speed {self.download}down/{self.upload}up when I pay for {main.PROMISED_DOWN}down/{main.PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()
        

bot = InternetSpeedTwitterBot(main.chrome_driver_path)
bot.Get_internet_speed()
bot.tweet_at_provider()


# print("download: ",bot.download)
# print("uplaod: ", bot.upload)