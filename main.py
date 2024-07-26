import requests
from bs4 import BeautifulSoup
import sys
import os
import random
from dotenv import load_dotenv
import re

load_dotenv()

def testtings():
    html_text = requests.get("https://unsplash.com/photos/a-camper-van-parked-in-a-field-with-the-sun-setting-in-the-background-0HPzoJ1sAwM").text
    soup = BeautifulSoup(html_text, 'lxml')
    container = soup.find('button', {"aria-label": "Zoom in on this image"}).find('div').find_all('img')
    # print(len(container))
    with open('output.html', 'w', encoding='utf-8') as file: 
        file.write(str(container[1]))

# FUNCTION TO GET IMAGE's URL 
def getImagesURL():
    html_text = requests.get("https://unsplash.com/").text # Getting the website to scrape
    soup = BeautifulSoup(html_text, "lxml") # Make a soup 

    photo_containers = soup.find('div', {'data-test': 'masonry-grid-count-three'}) # get the main container to scrape
    
    if not photo_containers: # checks if it exists
        return print('either the data-test attribute is replaced or something else happen idk')
    
    photo_grids = photo_containers.find_all('div', style=lambda value: value and '--row-gutter:24px' in value)
    
    if not photo_grids: # checks if it exists
        return print('either the style for --row-gutter:24px is replaced or something else happened idk')
    
    choose_random_grid = random.randint(0, 2) #choose 1 of 3 containers to have more random image
    chosen_grid = photo_grids[choose_random_grid] # getting the chosen grid
    
    get_anchors = chosen_grid.find_all('a', {'itemprop': 'contentUrl'}) # Getting all of the available links from the chosen grid
    if not get_anchors: # checks if it exists
        return print("probably they changed the anchor's attribute name (previously was itemprop) or they changed the value of itemprop")
    
    links = [anchor['href'] for anchor in get_anchors if 'href' in anchor.attrs] # get their links individually
    if not links: # checks if it exists
        return print("Link was not found!")
    
    links_count = len(links) # counting links (could've just put it directly inside the bottom var but for a better reading this is best... i think)
    
    choose_random_link = random.randint(0, links_count - 1) # getting random number 0 to whatever the links_count is
    chosen_link = links[choose_random_link] # choosing the image by random
    
    print("grid yang dipilih: " + str(choose_random_grid + 1)) # EXPLANATION!!!!!!!!!
    print("Link yang dipilih: " +  f"({str(choose_random_link)}) https://unsplash.com" + str(links[choose_random_link]) ) # EXPLANATION !!!!!!!!!!!!!!!!!!!!
    
    getImage(chosen_link) # getting ready to get the image by the chosen link

# FUNCTION TO GET THE ACTUAL IMAGE THE PAINTING THE ARTFUL THE PORTRAITS 
def getImage(link):
    html_text = requests.get("https://unsplash.com"+link).text # getting the image's url 
    soup = BeautifulSoup(html_text, 'lxml') # soupy
    
    photo_container = soup.find('button', {"aria-label": "Zoom in on this image"}) # getting the main container for the iamge
    if not photo_container:
        return print('the container button was not found they probably changed the aria-label or somethinge lse... damn...')
    
    find_image = photo_container.find('div').find_all('img') # first after we got to the child div we will be searching for all images to get (the parent is photo_contaienr btw)
    
    

# Send message
def sendImages(): 
    base_url = os.getenv('baseurl')
    parameters = {
        "chat_id" : "5757385822", 
        "photo" : "https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=415&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 415w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 715w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=830&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 830w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=1015&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 1015w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=1315&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 1315w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=1430&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 1430w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=1615&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 1615w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=1915&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 1915w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=2030&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 2030w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=2215&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 2215w, https://images.unsplash.com/photo-1721807578532-dc1756624727?q=80&w=2500&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D 2500w",
        "caption" : "This is what you would look like if you were a picture"
    }

    action = "sendPhoto"

    req = requests.get(base_url + action, data = parameters)

    response = req.json()
    print(response)

if __name__ == "__main__":
    # getImagesURL()
    # sendImages()
    testtings()
