from sqlmodel import SQLModel, Field, Relationship
from typing import List

class Departamento(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str

    # Relación para el ORM: lista de empleados de un departamento
    empleados: List["Empleado"] = Relationship(back_populates="departamento")