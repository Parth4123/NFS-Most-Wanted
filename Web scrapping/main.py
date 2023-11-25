from bs4 import BeautifulSoup
import requests
import os

def save_image_links(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')
    
    links_file_path = os.path.join(os.getcwd(), folder, 'image_links.txt')
    
    with open(links_file_path, 'w') as links_file:
        for image in images:
            link = image.get('src') or image.get('data-src')
            if link:
                links_file.write(link + '\n')
                

save_image_links(url, folder)
