import torch
from torchvision import transforms
import requests
from io import BytesIO
from PIL import Image
#from ImageCaption import net

def Result(url):
    response = requests.get(url)
    trans = transforms.ToTensor()
    img = trans(Image.open(BytesIO(response.content)))
    return "Work in Progress" #net(img)