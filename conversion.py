import os
import nibabel as nib
from PIL import Image
import numpy as np

# Function to convert NIfTI to PNG
def convert_nii_to_png(nii_path, output_folder):
    # Load the NIfTI file
    img = nib.load(nii_path)
    
    # Get the image data as a NumPy array
    data = img.get_fdata()
    
    # Normalize the data to the range [0, 255]
    #data = (data - data.min()) / (data.max() - data.min()) * 255
    
    # Convert to uint8
    data = data.astype(np.uint8)
    
    # Save each slice as PNG
    for i in range(data.shape[-1]):
        slice_data = data[:, :, i]
        img_png = Image.fromarray(slice_data)
        img_path = os.path.join(output_folder, f'{os.path.basename(nii_path)[:-7]}_{i}.png')
        img_png.save(img_path)

# Path to the folder containing NIfTI files
dataset_folder = '/home/aranyaa/Project/source_images/ground_truths'

# Path to the folder where PNG images will be saved
images_folder = '/home/aranyaa/Project/source_images/ground_truths_png_not_normalized'

# Loop through all NIfTI files in the dataset folder
for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        if file.endswith('.nii') or file.endswith('.nii.gz'):
            nii_path = os.path.join(root, file)
            convert_nii_to_png(nii_path, images_folder)

print("Conversion complete.")
