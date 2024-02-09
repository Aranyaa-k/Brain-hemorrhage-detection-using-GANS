import os
import random
import shutil

# Set the paths
train_folder = '/home/aranyaa/Project/dataset/train'
train2_folder = '/home/aranyaa/Project/dataset/train2'

# Create the 'train2' folder if it doesn't exist
os.makedirs(train2_folder, exist_ok=True)
os.makedirs(os.path.join(train2_folder, 'ground_truths'), exist_ok=True)
os.makedirs(os.path.join(train2_folder, 'images'), exist_ok=True)

# Get the list of filenames from both folders
gt_filenames = os.listdir(os.path.join(train_folder, 'ground_truths'))
img_filenames = os.listdir(os.path.join(train_folder, 'images'))

# Select 2000 random filenames from each list
selected_gt_filenames = random.sample(gt_filenames, 2000)
#selected_img_filenames = random.sample(img_filenames, 2000)

# Copy the selected files to the 'train2' folder
for filename in selected_gt_filenames:
    shutil.copy(os.path.join(train_folder, 'ground_truths', filename),
                os.path.join(train2_folder, 'ground_truths', filename))

for filename in selected_gt_filenames:
    shutil.copy(os.path.join(train_folder, 'images', filename),
                os.path.join(train2_folder, 'images', filename))

print("Images copied to train2 folder.")
