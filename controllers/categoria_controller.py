from models.categoria_model import CategoriaModel
from db import db

class CategoriaController:
    def getAll(self):
        try:
            record = CategoriaModel.query.all()
            response = []
            for categoria in record:
                response.append(categoria.toJson())

            return response, 200
        except Exception as e:
            return {
                'message': e.args[0],
            }
        
    def create(self, data):
        try:
            categoria = CategoriaModel(nombre=data['nombre'])
            db.session.add(categoria)
            db.session.commit()

            return categoria.toJson(), 201
        except Exception as e:
            return {
                'message': e.args[0],
            }