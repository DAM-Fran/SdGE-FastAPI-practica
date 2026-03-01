from sqlmodel import SQLModel, Field, Relationship
# from typing import Optional

class Empleado(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True) #
    nombre: str
    apellido: str
    puesto: str

    # foreign key
    departamentoId: int | None = Field(default=None, foreign_key="departamento.id")

    # Relación para el ORM: departamento al que pertenece un empleado
    departamento: "Departamento" = Relationship(back_populates="empleados")