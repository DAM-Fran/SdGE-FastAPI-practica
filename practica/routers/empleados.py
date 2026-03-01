from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from practica.database import get_session
from practica.models.departamento import Departamento
from practica.models.empleado import Empleado

router = APIRouter(
    prefix="/empleados",
    tags=["empleados"]
)

# empleados: list[Empleado] = []

@router.get("/")
def get_all_root(session: Session = Depends(get_session)):
    return session.exec(select(Empleado)).all()

@router.post("/")
def insertar_empleado(empleado: Empleado, session: Session = Depends(get_session)):
    # Verificamos si el departamento existe
    dep = session.get(Departamento, empleado.departamentoId)
    if not dep:
        raise HTTPException(status_code=404, detail="Departamento no existe")
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    return empleado

@router.get("/{id}")
def leer_empleado(id: int, session: Session = Depends(get_session)):
    db_emp = session.get(Empleado, id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return db_emp

@router.put("/{id}")
def actualizar_empleado(id: int, emp_nuevo: Empleado, session: Session = Depends(get_session)):
    db_emp = session.get(Empleado, id)
    if not db_emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    emp_data = emp_nuevo.model_dump(exclude_unset=True)
    for key, value in emp_data.items():
        setattr(db_emp, key, value)

    session.add(db_emp)
    session.commit()
    session.refresh(db_emp)
    return db_emp

@router.delete("/{id}")
def borrar_empleado(id: int, session: Session = Depends(get_session)):
    db_empleado = session.get(Empleado, id)
    if not db_empleado:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(db_empleado)
    session.commit()
    return {"status": "borrado"}