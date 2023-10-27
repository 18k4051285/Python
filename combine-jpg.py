import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
from tkinter import messagebox

# Create a function to combine and save the images
def combine_images():
    selected_folder = filedialog.askdirectory(title="Select a folder with JPG images")

    if selected_folder:
        # List all the JPG files in the selected folder
        image_files = [f for f in os.listdir(selected_folder) if f.lower().endswith(".jpg")]

        if not image_files:
            messagebox.showerror("Error", "No JPG images found in the selected folder.")
            return

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

        # Ask the user to choose a destination folder for the combined image
        destination_folder = filedialog.askdirectory(title="Select a destination folder for the combined image")

        if destination_folder:
            # Save the combined image as a single JPG file in the chosen destination folder
            combined_image.save(os.path.join(destination_folder, "combined_image.jpg"))

            # Close the individual images
            for image in images:
                image.close()

            # Display a popup window with the destination
            messagebox.showinfo("Process Completed", f"Combined image saved in:\n{destination_folder}")

# Create a Tkinter GUI window
root = tk.Tk()
root.title("Combine JPG Images")
root.geometry("250x150")
root.minsize(260, 150)
root.maxsize(260, 150)
root['background']='#7cabfc'
# Create a button to trigger the image combining process
combine_button = tk.Button(root, text="Combine Images", command=combine_images)
combine_button.pack()

root.mainloop()


