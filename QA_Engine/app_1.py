from flask import Flask
from views_1 import views_1

app = Flask(__name__)
app.register_blueprint(views_1,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
