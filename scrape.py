from selenium import webdriver
import json

driver = webdriver.Chrome()

def check_page(url, driver) -> bool:
    try:
        driver.get(url)
        element = driver.find_element_by_tag_name('h1')
        if configData['desired_game_name'] in element.text:
            return True
        else:
            return False
    except:
        print('Correct HTML tag not found on page. The page is probably not the right one')
        return False

def update_id_in_config(new_property, property_name: str):
    # Read in config file
    with open('config.json', 'r') as data:
        original = json.load(data)
    
    # Update specified field here
    original[property_name] = new_property
    # close file, then open again with write permissions
    with open('config.json', 'w') as data:
        json.dump(original, data)
    print('fin')

with open('data.json') as data:
    configData = json.load(data)
    
    
    desired_title = configData['const_slug'] + ' ' + configData['current_year'] + ' ' + configData['desired_game_name']
    # set test id to previous id + 1
    uid: int = (int)(configData['previous_uid']) + 1
    original_uid = uid # use this to prevent runaway program, configurable search time in config
    found: bool = False
    
    while not found:
        found = check_page(configData['website_base'] + (str)(uid), driver)
        if not found:
            uid += 1
        else:
            print(f'Success, found %d as valid UID for game %s' % (uid, configData['desired_game_name']))
            update_id_in_config(uid, 'uid') 
        
        if uid >= original_uid + ((int)(configData['max_loops'])):
            break

