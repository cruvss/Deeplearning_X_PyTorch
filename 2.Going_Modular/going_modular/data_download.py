import os 
import requests
import zipfile
from pathlib import Path


#set the path to the data directory

data_path = Path('data/')
image_path = data_path / 'pizza_steak_sushi'

# if the image folder doesn't exist, create it

if image_path.is_dir():
    print(f"{image_path} exists.")
else:
    print(f"Did not find {image_path}. Creating {image_path}....")
    image_path.mkdir(parents=True, exist_ok=True)
    
# download the data from github repo

with open(data_path/ "pizza_steak_sushi.zip", "wb") as f:
    request =  requests.get("https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip")
    print(" Downloading the data . . .")
    f.write(request.content)
    print( " Sucessfully downloaded the data ")
    
#unzip the data

with zipfile.ZipFile(data_path/"pizza_steak_sushi.zip", "r") as zip_ref:
    print("Unzipping the downloaded data. . .")
    zip_ref.extractall(image_path)
    
os.remove(data_path / "pizza_steak_sushi.zip")