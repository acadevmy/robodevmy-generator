from PIL import Image 
from IPython.display import display 
import random
import json
import os

# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

face = ["White"] 
face_weights = [100]

eyes = ["eye1", "eye2", "eye3", "eye4", "eye5", "eye6", "eye7", "eye8", "eye9", "eye10"] 
eyes_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

hair = ['hair1', 'hair2', 'hair3', 'hair4', 'hair5', 'hair6', 'hair7', 'hair8', 'hair9', 'hair10']
hair_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

mouth = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10']
mouth_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

# Dictionary variable for each trait. 
# Eech trait corresponds to its file name

face_files = {
    "White": "face1"
}

eyes_files = {
    "eye1": "eye1",
    "eye2": "eye2",
    "eye3": "eye3",
    "eye4": "eye4",
    "eye5": "eye5",
    "eye6": "eye6",
    "eye7": "eye7",
    "eye8": "eye8",
    "eye9": "eye9",
    "eye10": "eye10"      
}

hair_files = {
    "hair1": "hair1",
    "hair2": "hair2",
    "hair3": "hair3",
    "hair4": "hair4",
    "hair5": "hair5",
    "hair6": "hair6",
    "hair7": "hair7",
    "hair8": "hair8",
    "hair9": "hair9",
    "hair10": "hair10"
}

mouth_files = {
    "m1": "m1",
    "m2": "m2",
    "m3": "m3",
    "m4": "m4",
    "m5": "m5",
    "m6": "m6",
    "m7": "m7",
    "m8": "m8",
    "m9": "m9",
    "m10": "m10"
}

## Generate Traits

TOTAL_IMAGES = 100 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():   
    new_image = {} #
    # For each trait category, select a random trait based on the weightings 
    new_image ["Face"] = random.choices(face, face_weights)[0]
    new_image ["Eyes"] = random.choices(eyes, eyes_weights)[0]
    new_image ["Hair"] = random.choices(hair, hair_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]   
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)

# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
print(all_images)

# Get Trait Counts

face_count = {}
for item in face:
    face_count[item] = 0

eyes_count = {}
for item in eyes:
    eyes_count[item] = 0
    
hair_count = {}
for item in hair:
    hair_count[item] = 0
    
mouth_count = {}
for item in mouth:
    mouth_count[item] = 0
    
for image in all_images:
    face_count[image["Face"]] += 1
    eyes_count[image["Eyes"]] += 1
    hair_count[image["Hair"]] += 1
    mouth_count[image["Mouth"]] += 1
    
print(face_count)
print(eyes_count)
print(hair_count)
print(mouth_count)

#### Generate Images

os.makedirs("./images/")

for item in all_images:

    im1 = Image.open(f'./face_parts/face/{face_files[item["Face"]]}.png').convert('RGBA')
    im2 = Image.open(f'./face_parts/eyes/{eyes_files[item["Eyes"]]}.png').convert('RGBA')
    im2 = im2.resize(im1.size)
    im3 = Image.open(f'./face_parts/hair/{hair_files[item["Hair"]]}.png').convert('RGBA')
    im3 = im3.resize(im1.size)
    im4 = Image.open(f'./face_parts/mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    im4 = im4.resize(im1.size)

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)

    #Convert to RGB
    rgb_im = com3.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)