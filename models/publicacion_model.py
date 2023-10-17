from sqlalchemy import Integer, String, DateTime, Boolean, func, Text, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from db import db

class PublicacionModel(db.Model):
    __tablename__ = 'publicacion'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(250), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(250), nullable=False)
    contenido: Mapped[str] = mapped_column(Text, nullable=False)
    imagen: Mapped[str] = mapped_column(Text, nullable=False)
    fecha_creacion: Mapped[str] = mapped_column(DateTime, default=func.now())
    fecha_actualizacion: Mapped[str] = mapped_column(DateTime, default=func.now())
    estado: Mapped[bool] = mapped_column(Boolean, default=True)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey('categoria.id'), nullable=False)

    def __str__(self):
        return f'Publicacion: {self.titulo}'
    
    def toJson(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'contenido': self.contenido,
            'imagen': self.imagen,
            'fecha_creacion': str(self.fecha_creacion),
            'fecha_actualizacion': str(self.fecha_actualizacion),
            'estado': self.estado,
            'categoria_id': self.categoria_id,
        }