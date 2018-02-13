from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <html>
            <title>ORF 401: Assignment #1 - Python - Spring 2018</title>
            <body>
                <center>
                <br><br>
                <h1>riidr carsharing service</h1>
                <br><br>
                <img src="riidr_logo.png"/>
                <br><br>

                <p>Enter a single origin/destination to search for:</p>

                <form method="get">
                    <input type="text" name="query"/>
                    <input type="submit"/>
                </form>
                </center>
            </body>
        </html>
    '''
