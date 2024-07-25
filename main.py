import requests
from bs4 import BeautifulSoup
import sys
import os
import random
from dotenv import load_dotenv

load_dotenv()

# def testtings():
#     html_text = requests.get("https://unsplash.com").text
#     soup = BeautifulSoup(html_text, 'lxml')
#     picture_container = soup.find('div', class_="NHQ0m").find_all('div', )
#     print(len(picture_container))
    
def getImagesURL():
    html_text = requests.get("https://unsplash.com").text # Getting the website to scrape
    soup = BeautifulSoup(html_text, 'lxml') # beautiful with soup 
    picture_container = soup.find('div', class_="d95fI") # getting the main div as an object to the children
    
    if not picture_container: # Checks if the main div from unsplash is available
        return print("Picture container was not found (probably they changed the classname)")
    
    anchor_tags = picture_container.find_all('a', class_="Prxeh") # getting all of the available links from the main div
    links = [anchor['href'] for anchor in anchor_tags if 'href' in anchor.attrs] # containing all of the available links
    
    if not links: # Checks if there are any links
        return print("Link was nor found or this is just being a little stupid")
    
    list_amount = len(links) # Counting how many links there are available
    random_image = random.randint(0, list_amount) # getting things randomized from 0 to the amount of available links
    
    print(random_image)
    
    getImage(links[random_image - 1]) # Give it to other function to process we done here
    
def getImage(link):
    html_text = requests.get("https://unsplash.com"+link).text # getting the image's url 
    soup = BeautifulSoup(html_text, 'lxml') # soupy
    imageContainer = soup.find("div", class_="HcSeS") # get the main container to scrape (for image)
    
    getImageSource = imageContainer.find("img", class_="ApbSI z1piP vkrMA")['srcset'] # after that get the image's online link so that we can use
    getCaption = soup.find('h1', class_="vev3s").text
    
    print(getCaption)
    

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
    getImagesURL()
    # sendImages()
    # testtings()
