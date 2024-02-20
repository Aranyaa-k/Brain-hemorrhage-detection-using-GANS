"""import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the noisy image (replace 'sample_denoise_input.jpg' with your actual filename)
image = cv2.imread('/home/aranyaa/Project/dataset_not_normalized/train/images/ID_0b10cbee_ID_f91d6a7_17.png')

# Apply the median filter
denoised_image = cv2.medianBlur(image, 5)  # Adjust the kernel size (e.g., 5x5) as needed

# Display the original and denoised images
row, col = 1, 2
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')

axs[1].imshow(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Denoised Image (Median Filter)')

plt.show()"""

"""import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the noisy image (replace 'sample_denoise_input.jpg' with your actual filename)
image = cv2.imread('/home/aranyaa/Project/dataset_not_normalized/train/images/ID_0b10cbee_ID_f91d6a7_17.png')

# Apply the median filter for noise removal
denoised_image = cv2.medianBlur(image, 5)  # Adjust the kernel size (e.g., 5x5) as needed

# Apply histogram equalization
equalized_image = cv2.equalizeHist(denoised_image)

# Display the original, denoised, and equalized images
row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')

axs[1].imshow(cv2.cvtColor(denoised_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Denoised Image')

axs[2].imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
axs[2].set_title('Equalized Image')

plt.show()"""


'''import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the noisy image (replace 'sample_denoise_input.jpg' with your actual filename)
image = cv2.imread('/home/aranyaa/Project/dataset_not_normalized/train/images/ID_ed6dfff7_ID_f54a5fd_4.png')

denoised_image = cv2.medianBlur(image, 3)

# Convert the image to grayscale (if not already)
gray_image = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display the original, denoised, and equalized images
row, col = 1, 3
fig, axs = plt.subplots(row, col, figsize=(15, 10))
fig.tight_layout()

axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')

axs[1].imshow(gray_image, cmap='gray')
axs[1].set_title('Denoised Grayscale Image')

axs[2].imshow(equalized_image, cmap='gray')
axs[2].set_title('Equalized Image')

plt.show()'''

import cv2
import numpy as np

# Read the image
image = cv2.imread("/home/aranyaa/Project/dataset_not_normalized/train/images/ID_0b10cbee_ID_f91d6a7_4.png")

# Apply median filtering to remove speckles
threshold = 150
despeckled_image = cv2.medianBlur(image, ksize=3)

edited_image = np.where(despeckled_image > threshold, 0, despeckled_image)


# Save the despeckled image
cv2.imwrite("edited_image.png", edited_image)
cv2.imwrite("despeckled_image.png", despeckled_image)


