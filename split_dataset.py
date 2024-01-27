import os
import shutil
from sklearn.model_selection import train_test_split

# Set the path to your original folders
original_images_folder = '/home/aranyaa/Project/Brain_Hemorrhage_Segmentation_Dataset/source_images/images_png'
original_ground_truths_folder = '/home/aranyaa/Project/Brain_Hemorrhage_Segmentation_Dataset/source_images/ground_truth_png'

# Set the path to the new folders for train, val, and test
output_folder = '/home/aranyaa/Project/Brain_Hemorrhage_Segmentation_Dataset/dataset'
train_folder = os.path.join(output_folder, 'train')
val_folder = os.path.join(output_folder, 'val')
test_folder = os.path.join(output_folder, 'test')

# Create the output folders if they don't exist
for folder in [train_folder, val_folder, test_folder]:
    os.makedirs(os.path.join(folder, 'images'), exist_ok=True)
    os.makedirs(os.path.join(folder, 'ground_truths'), exist_ok=True)

# Get the list of image filenames
image_filenames = os.listdir(original_images_folder)

# Split the dataset into train, val, and test sets
train_images, test_images = train_test_split(image_filenames, test_size=0.2, random_state=42)
train_images, val_images = train_test_split(train_images, test_size=0.1, random_state=42)

# Copy images and corresponding ground truths to the appropriate folders
def copy_images_and_ground_truths(images, source_folder, dest_folder):
    for image_filename in images:
        # Copy image
        shutil.copy(os.path.join(original_images_folder, image_filename),
                    os.path.join(dest_folder, 'images', image_filename))
        
        # Corresponding ground truth filename
        # gt_filename = image_filename.replace('.png', '_gt.png')
        
        # Copy ground truth
        shutil.copy(os.path.join(original_ground_truths_folder, image_filename),
                    os.path.join(dest_folder, 'ground_truths', image_filename))

# Copy for train set
copy_images_and_ground_truths(train_images, original_images_folder, train_folder)

# Copy for val set
copy_images_and_ground_truths(val_images, original_images_folder, val_folder)

# Copy for test set
copy_images_and_ground_truths(test_images, original_images_folder, test_folder)
