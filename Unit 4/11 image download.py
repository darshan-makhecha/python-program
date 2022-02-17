from bs4 import *
import requests
import os

def folder(img):
    try:
        foler = input("Enter folder name :-")
        os.mkdir(folder)
    except:
        print("Folder Exists with that name !")
        folder()

def download(img,folder):
    count = 0
    print(f"Total {len(img)} Image Found !")

    if len(img)!=0:
        for i,img in enumerate(img):
            try:
                img_link = img["data-srcset"]
            except:
                try:
                    img_link = img["data-src"]
                except:
                    try:
                        img_link = img["data-fallback-src"]
                    except:
                        try:
                            img_link = img["src"]
                        except:
                            pass
                try:
                    r = requests.get(img_link).content
                    try:
                        r = str(r,'utf-8')
                    except unicode:
                        with open(f"{folder}/img{i+1}.jpg", "wb+") as f:
                            f.write(r)
                    count +=1
                except:
                    pass
        if count == len(img):
            print("All img download")
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")

def main(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    img = soup.findAll('img')
    folder(img)

url = input("entern URL : ")
main(url)

                    
                    




















                    
                    







                    
