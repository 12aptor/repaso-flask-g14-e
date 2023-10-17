from sqlalchemy import Integer, String, DateTime, Boolean, func
from sqlalchemy.orm import mapped_column, Mapped
from db import db

class CategoriaModel(db.Model):
    __tablename__ = 'categoria'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_creacion: Mapped[str] = mapped_column(DateTime, default=func.now())
    fecha_actualizacion: Mapped[str] = mapped_column(DateTime, default=func.now())
    estado: Mapped[bool] = mapped_column(Boolean, default=True)

    def __str__(self):
        return f'Categoria: {self.nombre}'
    
    def toJson(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'fecha_creacion': str(self.fecha_creacion),
            'fecha_actualizacion': str(self.fecha_actualizacion),
            'estado': self.estado,
        }