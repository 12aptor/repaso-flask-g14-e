from models.publicacion_model import PublicacionModel
from db import db

class PublicacionController:
    def getAll(self):
        try:
            record = PublicacionModel.query.all()

            return [pub.toJson() for pub in record], 200
        except Exception as e:
            return {
                'message': e.args[0],
            }
        
    def create(self, data):
        try:
            publicacion = PublicacionModel(
                titulo=data['titulo'],
                descripcion=data['descripcion'],
                contenido=data['contenido'],
                imagen=data['imagen'],
                categoria_id=data['categoria_id']
            )
            db.session.add(publicacion)
            db.session.commit()
            
            return publicacion.toJson(), 201
        except Exception as e:
            return {
                'message': e.args[0],
            }