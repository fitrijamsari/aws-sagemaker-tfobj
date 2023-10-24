import json
import os
import shutil
from pathlib import Path

import xmltodict

# Define the paths to your dataset and the new directory structure
dataset_path = "dataset"
output_directory = "input_directory"

# Create the new directory structure
os.makedirs(os.path.join(output_directory, "images"), exist_ok=True)

# Initialize the data structures for images, annotations, and categories
images = []
annotations = []
categories = {}


# Helper function to add a category to the categories dictionary
def add_category(category_name):
    if category_name not in categories:
        category_id = len(categories) + 1
        categories[category_name] = category_id
    return categories[category_name]


# Recursively process the dataset directory and its subdirectories
for xml_file in Path(dataset_path).rglob("*.xml"):
    with open(xml_file, "r") as xml:
        xml_dict = xmltodict.parse(xml.read())

    image_info = xml_dict["annotation"]["filename"]
    image_path = os.path.join(os.path.dirname(xml_file), image_info)

    # Copy the image to the "images" folder
    destination_image_path = os.path.join(
        output_directory, "images", image_info
    )
    os.makedirs(
        os.path.dirname(destination_image_path), exist_ok=True
    )
    shutil.copy(image_path, destination_image_path)

    # Process image information
    image_id = len(images) + 1
    image_width = xml_dict["annotation"]["size"]["width"]
    image_height = xml_dict["annotation"]["size"]["height"]
    images.append(
        {
            "file_name": image_info,
            "width": image_width,
            "height": image_height,
            "id": image_id,
        }
    )

    # Process object annotations
    objects = xml_dict["annotation"]["object"]
    if not isinstance(objects, list):
        objects = [objects]

    for obj in objects:
        category_name = obj["name"]
        category_id = add_category(category_name)
        bbox = [
            int(obj["bndbox"]["xmin"]),
            int(obj["bndbox"]["ymin"]),
            int(obj["bndbox"]["xmax"]) - int(obj["bndbox"]["xmin"]),
            int(obj["bndbox"]["ymax"]) - int(obj["bndbox"]["ymin"]),
        ]

        annotations.append(
            {
                # "id": len(annotations) + 1,
                "image_id": image_id,
                "bbox": bbox,
                # "category_id": category_id,
                "category_id": category_name,
            }
        )

# Create the annotations dictionary
annotations_dict = {
    "images": images,
    "annotations": annotations,
    # "categories": [
    #     {"id": category_id, "name": category_name}
    #     for category_name, category_id in categories.items()
    # ],
}

# Save the annotations as a JSON file
with open(
    os.path.join(output_directory, "annotations.json"), "w"
) as json_file:
    json.dump(annotations_dict, json_file, indent=4)

print(
    "Dataset restructuring and conversion to annotations.json"
    " completed"
)
