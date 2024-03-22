import cv2
import matplotlib.pyplot as plt

def blur_faces_show_and_save(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image from BGR (OpenCV default) to RGB (for matplotlib)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale (needed for face detection)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, 1.1, 4)

    # Blur each face found
    for (x, y, w, h) in faces:
        # Extract the face region
        face_region = image[y:y+h, x:x+w]
        
        # Apply a Gaussian blur to this face region
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
        
        # Replace the original face region with the blurred one
        image[y:y+h, x:x+w] = blurred_face

    # Convert the modified image to RGB (for matplotlib and saving)
    blurred_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the original and blurred images using matplotlib
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    ax[0].imshow(image_rgb)
    ax[0].set_title('Original Image')
    ax[0].axis('off')

    ax[1].imshow(blurred_image_rgb)
    ax[1].set_title('Image with Blurred Faces')
    ax[1].axis('off')

    plt.show()

    # Save the modified image
    cv2.imwrite(output_path, cv2.cvtColor(blurred_image_rgb, cv2.COLOR_BGR2RGB))
    print('Blurred Face Image saved.')

# Example usage
blur_faces_show_and_save('test.jpg', 'blurredface_image.jpg')