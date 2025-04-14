from PIL import Image
import os

folder_path = "/workspaces/python-projects/image_manipulation_with_pill/images"

new_path_of_resized_images = "/workspaces/python-projects/image_manipulation_with_pill/resized_images/"

for item in os.listdir():
    full_path = os.path.join(folder_path, item)
   
    img = Image.open(full_path).convert('RGB').rotate(90).resize((128,128))
   # print(new_path_of_resized_images+item+".jpeg")
    img.save(new_path_of_resized_images+item+".jpeg")
    



    