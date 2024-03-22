import cv2
import numpy as np
import pickle

# Load the parking space positions
with open("CarParkPosition", "rb") as f:
    parking_spaces = pickle.load(f)

# Load the image
img = cv2.imread("images/carParkImg.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Function to check if a parking space is occupied
def is_occupied(parking_space, contours):
    x1, y1, w1, h1 = parking_space
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if x < x1 + w1 and x + w > x1 and y < y1 + h1 and y + h > y1:
            return True
    return False

# Assuming standard size for all parking spaces
standard_width, standard_height = 107, 40

# Draw parking spaces, check occupancy, and label
empty_spaces = 0
font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.5
font_thickness = 1
for index, space in enumerate(parking_spaces, start=1):
    x, y = space
    w, h = standard_width, standard_height
    label = str(index)
    
    # Calculate text size to center the label
    text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
    text_x = x + (w - text_size[0]) // 2
    text_y = y + (h + text_size[1]) // 2

    if not is_occupied((x, y, w, h), contours):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, label, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)
        empty_spaces += 1
    else:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255 ,0), 2)
        cv2.putText(img, label, (text_x, text_y), font, font_scale, (0, 255, 0), font_thickness)

# Display the result
cv2.imshow("Parking Lot", img)

# Save the image with labeled parking spaces
cv2.imwrite("labeled_carParkImg.png", img)
print("Image saved")

cv2.waitKey(0)
cv2.destroyAllWindows()
