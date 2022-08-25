import webdriver as wdc
import constants as c
import episodeService as esc

driver = wdc.initializeWebDriver()
driver.get(c.get_black_clover_url(10))
print(esc.get_watching_servers(driver)[0].get_attribute('onclick'))



