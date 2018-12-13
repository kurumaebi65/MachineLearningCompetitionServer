from flask import Flask
from flask_login import LoginManager
from application.upload import upload
from application.results import results
from application.description import description

app = Flask(__name__)
app.secret_key='very secret key'

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(upload.app)
app.register_blueprint(results.app)
app.register_blueprint(description.app)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
