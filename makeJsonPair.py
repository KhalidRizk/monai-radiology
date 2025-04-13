import os
import random
import json

# Define the base directories
img_dir = '/teamspace/studios/this_studio/monai-radiology/images/val'
lbl_dir = '/teamspace/studios/this_studio/monai-radiology/images/labels/final/val'

# Function to get image-label pairs from a directory
def get_image_label_pairs(img_dir, lbl_dir):
    img_files = [f for f in os.listdir(img_dir) if f.endswith('.nii.gz')]
    lbl_files = [f for f in os.listdir(lbl_dir) if f.endswith('.nii.gz')]
    pairs = []
    for img in img_files:
        lbl = img.replace('_ct.nii.gz', '.nii.gz')
        if lbl in lbl_files:
            pairs.append((img, lbl))
    return pairs

pairs = get_image_label_pairs(img_dir, lbl_dir)

# Shuffle the data if needed
random.shuffle(pairs)

# Create the JSON structure
data = [
    {
        'image': os.path.join(img_dir, img),
        'label': os.path.join(lbl_dir, lbl)
    }
    for img, lbl in pairs
]

# Write the data to a JSON file
json_file_path = '/teamspace/studios/this_studio/validation.json'
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"JSON file created at {json_file_path}")
