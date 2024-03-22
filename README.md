# Plagiarism Detection Tool

This web application detects similarity between two text inputs and highlights the matching words. It utilizes the SequenceMatcher from the difflib library to calculate the similarity score and identify matching blocks of text.

## Usage
1. Enter the first text in the provided textarea labeled "Enter Text 1 Here...".
2. Enter the second text in the textarea labeled "Enter Text 2 Here...".
3. Click on the "Check Similarity" button to see the similarity score and highlighted matching words.

## Features
- **Similarity Score**: Displays the percentage of similarity between the two texts.
- **Highlighted Text**: Shows both texts with matching words highlighted in yellow.

## Instructions
- Make sure to enter the texts you want to compare in the provided textareas.
- After submitting, the application will display the similarity score and highlight the matching words in both texts.

## Interface
- **Header**: Displays the title "Plagiarism Detection Tool".
- **Textareas**: Two textareas for entering the texts to be compared.
- **Check Similarity Button**: Initiates the comparison process.
- **Similarity Score**: Shows the percentage of similarity between the texts.
- **Highlighted Text**: Displays the texts with matching words highlighted.

## Technologies Used
- **Flask**: Python web framework used for the backend.
- **HTML/CSS**: For structuring and styling the web interface.
- **difflib.SequenceMatcher**: Utilized to find the similarity between texts and highlight matching words.

## Run the Application
To run the application locally:
1. Save the provided Python code in a file (e.g., `app.py`).
2. Install Flask (`pip install Flask`).
3. Run the Python file (`python app.py`).
4. Open a web browser and go to `http://localhost:5000/` to access the application.

