from flask import Flask
from routes import bp
import os
import random as rd

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0',port=port)
    #app.run(debug=True)
