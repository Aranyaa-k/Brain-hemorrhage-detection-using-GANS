import os
import cv2
import numpy as np

def calculate_iou(pred_mask, true_mask):
    intersection = np.logical_and(pred_mask, true_mask)
    union = np.logical_or(pred_mask, true_mask)
    iou_score = np.sum(intersection) / (np.sum(union) + 1e-10)
    return iou_score

pred_folder = "/home/aranyaa/Project/Results/pred/"
gt_folder = "/home/aranyaa/Project/Results/gt/"

iou_scores = []

# Iterate through the images in the pred folder
for pred_file in os.listdir(pred_folder):
    if pred_file.endswith(".png"):  # Assuming the images are in PNG format
        pred_path = os.path.join(pred_folder, pred_file)
        gt_path = os.path.join(gt_folder, pred_file)
        
        # Load the predicted and ground truth masks
        pred_mask = cv2.imread(pred_path, cv2.IMREAD_GRAYSCALE)
        true_mask = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)
        
        # Convert images to binary masks if needed
        # Convert images to binary masks (if needed)
        # For example, apply a threshold to convert grayscale images to binary
        pred_mask = cv2.threshold(pred_mask, 70, 255, cv2.THRESH_BINARY)[1]
        true_mask = cv2.threshold(true_mask, 70, 255, cv2.THRESH_BINARY)[1]
        
        # Calculate IoU
        iou = calculate_iou(pred_mask, true_mask)
        iou_scores.append(iou)

# Calculate average IoU
average_iou = np.mean(iou_scores)

print("Average IoU:", average_iou)
