from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Empresa(db.Model):
    __tablename__ = "empresa"
    
    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), index=True, unique=True, nullable=False)
    register_name = db.Column(db.String(255), index=True, unique=True, nullable=False)
    business_name = db.Column(db.String(150), nullable=False)
    cnae = db.Column(db.String(7), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
