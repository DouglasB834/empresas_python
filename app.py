from flask import Flask
from flasgger import Swagger
from models.models import db
from routes.company_routes import company_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Swagger(app) 
app.config["SECRET_KEY"] = "COGNITO"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres.qnrmwwuiglvkgzchsmxa:G1xXYhZt9BKKWfDD@aws-0-sa-east-1.pooler.supabase.com:6543/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True 


db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(company_bp)

if __name__ == "__main__":
    app.run(debug=True)
