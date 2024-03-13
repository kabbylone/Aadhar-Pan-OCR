# import cv2
# import numpy as np

# # Read the PAN card image
# pan_card_image = cv2.imread('E:\pann.jpg')

# # Convert the image to grayscale
# gray_image = cv2.cvtColor(pan_card_image, cv2.COLOR_BGR2GRAY)

# # Apply thresholding to get a binary image
# _, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# # Find contours in the binary image
# contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Assuming the signature is the largest contour
# largest_contour = max(contours, key=cv2.contourArea)

# # Get the bounding box of the contour
# x, y, w, h = cv2.boundingRect(largest_contour)

# # Crop the signature region from the image
# signature = pan_card_image[y:y+h, x:x+w]

# # Save the cropped signature as a new image file
# cv2.imwrite('signature.jpg', signature)

# print("Signature extracted and saved successfully!")
import cv2
import os

# Read the PAN card image
pan_card_image = cv2.imread('E:\pann.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(pan_card_image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to get a binary image
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Assuming the signature is the largest contour
largest_contour = max(contours, key=cv2.contourArea)

# Get the bounding box of the contour
x, y, w, h = cv2.boundingRect(largest_contour)

# Crop the signature region from the image
signature = pan_card_image[y:y+h, x:x+w]

# Specify the folder to save the signature image (in volume E)
output_folder = 'E:/signature'

# Create the folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Save the cropped signature as a new image file
output_path = os.path.join(output_folder, 'signature.jpg')
cv2.imwrite(output_path, signature)

print("Signature extracted and saved successfully at:", output_path)
