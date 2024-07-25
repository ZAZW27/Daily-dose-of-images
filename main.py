import requests
from bs4 import BeautifulSoup
import sys
import random



def testtings():
    html_text = requests.get("https://unsplash.com").text
    soup = BeautifulSoup(html_text, 'lxml')
    picture_container = soup.find('div', class_="NHQ0m").find_all('div', )
    print(len(picture_container))
    
def getImagesURL():
    html_text = requests.get("https://unsplash.com").text
    soup = BeautifulSoup(html_text, 'lxml')
    picture_container = soup.find('div', class_="d95fI")
    
    if not picture_container: # Checks if the main div from unsplash is available
        return print("Picture container was not found (probably they replaced it :())")
    
    anchor_tags = picture_container.find_all('a', class_="Prxeh")
    links = [anchor['href'] for anchor in anchor_tags if 'href' in anchor.attrs]
    
    if not links: # Checks if there are any links
        return print("Link was nor found or this is just being a little stupid")
    
    list_amount = len(links)
    random_image = random.randint(0, list_amount)
    
    print(random_image)
    
    getImage(links[random_image - 1])
    # with open('output.html', 'w', encoding='utf-8') as file: 
    #     file.write(str(picture_container))
    
def getImage(link):
    html_text = requests.get("https://unsplash.com"+link).text
    soup = BeautifulSoup(html_text, 'lxml')
    imageContainer = soup.find("div", class_="HcSeS")
    getImageSource = imageContainer.find("img", class_="ApbSI z1piP vkrMA")['srcset']
    print(getImageSource)
    
    with open('output.html', 'w', encoding='utf-8') as file: 
        file.write(str(getImageSource))
    

def sendImages(): 
    base_url = ""
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
