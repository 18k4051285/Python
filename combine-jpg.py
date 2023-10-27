import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from PIL import Image

# Create a Tkinter root window (it won't be displayed)
root = Tk()
root.withdraw()

# Ask the user to select a folder containing JPG images
selected_folder = askdirectory(title="Select a folder with JPG images")

# Check if the user selected a folder
if selected_folder:
    # List all the JPG files in the selected folder
    image_files = [f for f in os.listdir(selected_folder) if f.lower().endswith(".jpg")]

    if not image_files:
        print("No JPG images found in the selected folder.")
    else:
        # Sort the files alphabetically (you can change the sorting order if needed)
        image_files.sort()

        # Open the images and store them in a list
        images = [Image.open(os.path.join(selected_folder, image)) for image in image_files]

        # Calculate the total width and height of the combined image
        max_width = max(image.width for image in images)
        total_height = sum(image.height for image in images)

        # Create a new blank image with the calculated dimensions
        combined_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))  # White background

        # Paste the individual images into the combined image
        y_offset = 0
        for image in images:
            combined_image.paste(image, (0, y_offset))
            y_offset += image.height

        # Save the combined image as a single JPG file in the same folder
        combined_image.save(os.path.join(selected_folder, "combined_image.jpg"))

        # Close the individual images
        for image in images:
            image.close()

        print(f"Combined image saved as 'combined_image.jpg' in the selected folder.")
else:
    print("No folder selected. Please select a folder to proceed.")
