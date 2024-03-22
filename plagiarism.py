from flask import Flask, request, render_template_string
from difflib import SequenceMatcher

app = Flask(__name__)

def tokenize(text):
    #Tokenize the input text into words and return a list of words.
    return text.split()

def detokenize(tokens):
    return ' '.join(tokens)

def highlight_matches(words, matches):
    # Make a copy of the list to avoid modifying the original
    highlighted_words = words[:]  
    for start, _, length in matches:
        for i in range(start, start + length):
            highlighted_words[i] = "<span class='highlight'>" + highlighted_words[i] + "</span>"
    return detokenize(highlighted_words)

def find_similarity_and_matches(a, b):
    # Tokenize both texts
    words_a, words_b = tokenize(a), tokenize(b)
    # Create a SequenceMatcher to compare the tokenized texts
    sequence_matcher = SequenceMatcher(None, words_a, words_b)
    similarity_score = sequence_matcher.ratio() * 100
    # Find matching blocks
    matches = sequence_matcher.get_matching_blocks()[:-1]
    # Highlight matching words in both texts
    highlighted_a = highlight_matches(words_a, matches)
    highlighted_b = highlight_matches(words_b, [(match.b, match.a, match.size) for match in matches])
    
    return similarity_score, highlighted_a, highlighted_b

@app.route('/', methods=['GET', 'POST'])
def index():
    similarity_score = None
    highlighted_text1 = highlighted_text2 = ""
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        similarity_score, highlighted_text1, highlighted_text2 = find_similarity_and_matches(text1, text2)
    # HTML Template
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Plagiarism Detection Tool</title>
            <style>
                body {font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; color: #333;}
                .container {width: 80%; margin: auto; overflow: hidden;}
                header {background: #50a3a2; color: #fff; padding-top: 30px; min-height: 70px; border-bottom: #077187 1px solid;}
                header h1 {text-align: center; margin: 0; padding-bottom: 10px;}
                form {margin-top: 20px; text-align: center;}
                textarea {width: 40%; height: 100px; margin: 10px; border: 1px solid #ddd; border-radius: 5px; padding: 5px;}
                input[type="submit"] {padding: 10px; border: none; background-color: #50a3a2; color: white; font-size: 16px; border-radius: 5px; cursor: pointer;}
                input[type="submit"]:hover {background-color: #077187;}
                .highlight {background-color: yellow;}
                .text-output {margin: 20px auto; padding: 20px; background: #fff; border: 1px solid #ddd; border-radius: 5px; width: 80%;}
            </style>
        </head>
        <body>
            <header><h1>Plagiarism Detection Tool</h1></header>
            <div class="container">
                <form method="post">
                    <textarea name="text1" placeholder="Enter Text 1 Here...">{{ text1 }}</textarea>
                    <textarea name="text2" placeholder="Enter Text 2 Here...">{{ text2 }}</textarea><br>
                    <input type="submit" value="Check Similarity">
                </form>
                {% if similarity_score is not none %}
                <div class="text-output">
                    <h2>Similarity Score: {{ "%.2f" % similarity_score }}%</h2>
                    <h3>Text 1</h3>
                    <p>{{ highlighted_text1|safe }}</p>
                    <h3>Text 2</h3>
                    <p>{{ highlighted_text2|safe }}</p>
                </div>
                {% endif %}
              
            </div>
        </body>
        </html>
        ''', similarity_score=similarity_score, highlighted_text1=highlighted_text1, highlighted_text2=highlighted_text2)

if __name__ == '__main__':
    app.run(debug=True)
