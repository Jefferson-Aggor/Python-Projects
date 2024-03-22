# Blurring Faces in Images

This Python script utilizes the OpenCV library to detect faces in an image and blur them. The Haar Cascade classifier is used for face detection, and Gaussian blur is applied to the detected faces. Additionally, the script displays the original and modified images using matplotlib and saves the modified image to a specified output path.

## Functionality

### `blur_faces_show_and_save(image_path, output_path)`
- **Inputs**:
  - `image_path`: Path to the input image file.
  - `output_path`: Path to save the modified image with blurred faces.
- **Output**: None (displays and saves the modified image).
- **Process**:
  1. Load the input image.
  2. Detect faces in the image using the Haar Cascade classifier.
  3. For each detected face:
     - Extract the face region.
     - Apply Gaussian blur to the face region.
     - Replace the original face region with the blurred one.
  4. Display the original and modified images using matplotlib.
  5. Save the modified image to the specified output path.

## Usage

To use this script:
1. Save the provided code in a Python file (e.g., `blur_faces.py`).
2. Make sure you have OpenCV and matplotlib installed (`pip install opencv-python matplotlib`).
3. Prepare an input image containing faces.
4. Call the `blur_faces_show_and_save` function with the input image path and the desired output path for the modified image.

Example usage:
```python
blur_faces_show_and_save('input_image.jpg', 'output_image.jpg')
