from flask import Flask, render_template, request
import requests
from TweetAPI import TweetAPI
import logging
app = Flask(__name__)
PORT = 5000

log_file_path = './logs/log_output.log'

formatter = logging.Formatter('%(asctime)s %(message)s')  # Setting the desired log format

app.logger.setLevel(logging.INFO)  # Set log level to INFO
handler = logging.FileHandler(log_file_path)  # Log to the file
handler.setFormatter(formatter)
app.logger.addHandler(handler)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sentiment-analyzer', methods=['POST'])
def predict_sentiment():
    try:
        if request.method == 'POST':
            text_input = request.form.get('text_input', '')

            # Check if the input is a Twitter link
            if text_input.startswith('https://twitter.com/') or text_input.startswith('https://x.com/') :
                tweet_api = TweetAPI(API_KEY = 'apify_api_2QGQH8DkI54nayPr5grpIauvPmWqFL3NwQ4M')
                # Extract text from the Twitter link
                tweet_text = tweet_api.extract_text_from_twitter_link(text_input)
                if tweet_text:
                    text_input = tweet_text
                else:
                    raise Exception("Error extracting text from Twitter URL")

            # Perform sentiment analysis using the backend API
            response = requests.post("http://backend:6000/", files={'user_text': text_input})

            label = 'The statement is '

            if response.status_code == 200:
                predictions = response.json().get('predictions')

                n = len(predictions)

                for i, key in enumerate(predictions):
                    key = str(key)
                    if key.startswith('NOT_'): key = 'not ' + key.split('_')[-1]
                    label += str(key)
                    if i < n-2: label += ', '
                    elif i == n-2: label += ' and '
                    elif i == n-1: label += '.'
                    
                app.logger.info("Prediction for input text: %s is  %s",str(text_input), str(label))
                
                return render_template("result.html", label=label, text_input=text_input)

            else:
                error = "Error in prediction request. Status code: {}".format(response.status_code) + response.json().get('error')
                return render_template("result.html", err=error)

    except Exception as e:
        error = "Error: Text can't be processed"
        return render_template("result.html", err=e)

if __name__ == "__main__":
    app.run(port=PORT, debug=True, host='0.0.0.0')
    
