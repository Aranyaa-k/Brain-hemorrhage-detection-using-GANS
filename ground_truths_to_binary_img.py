import os
import cv2

# Path to the folder containing images
folder_path = "/home/aranyaa/Project/dataset_not_normalized/train2/ground_truths"

# Output folder for binary images
output_folder = "/home/aranyaa/Project/dataset_not_normalized/temp/ground_truths"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        # Read the image
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # Convert pixels above 0 to 1 (binary)
        binary_image = (image > 0).astype(int)

        # Save the binary image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, binary_image)

        print(f"Converted {filename} to binary and saved as {output_path}")
