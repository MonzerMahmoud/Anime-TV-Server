def get_watching_servers(driver):
    return driver.find_element_by_xpath('//*[@id="mCSB_1_container"]').find_elements_by_tag_name('li')
        
def get_4shared_url(driver):
    for server in get_watching_servers(driver):
        if server.get_attribute('onclick') == "getPlayerByName('4shared','multiple_servers2')":
            server.click()
            driver.switch_to_window(driver.window_handles[0])
            return driver.find_element_by_xpath('//*[@id="homePage"]/div[5]/div/div/div[3]/div/span/iframe').get_attribute('src')
            break

