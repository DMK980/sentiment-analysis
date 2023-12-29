''' 
    Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.

'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask,render_template,request

# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask("SentimentAnalyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    # getting the text from the mywebscript API
    texttoanalyze = request.args.get("textToAnalyze")

    # sending text to sentiment_analyzer
    response_ans = sentiment_analyzer(texttoanalyze)

    # formating response
    label = response_ans["label"]
    score = response_ans["score"]

    # different response if invalid input
    if label == "none" and score == "none":
        return "Invalid input ! Try again."
    return f"The given text has been identified as {label} with a score of {score}"

@app.route("/")
def render_index_page():
    ''' 
        This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
