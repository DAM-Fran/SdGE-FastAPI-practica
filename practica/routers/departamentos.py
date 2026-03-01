from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from practica.database import get_session
from practica.models.departamento import Departamento

router = APIRouter(
    prefix="/departamentos",
    tags=["departamentos"]
)

# departamentos: list[Departamento] = []

@router.get("/")
def get_all_root(session: Session = Depends(get_session)):
    return session.exec(select(Departamento)).all()

@router.post("/")
def insertar_departamento(departamento: Departamento, session: Session = Depends(get_session)):
    session.add(departamento)
    session.commit()
    session.refresh(departamento)
    return departamento

@router.get("/{id}")
def leer_departamento(id: int, session: Session = Depends(get_session)):
    db_dep = session.get(Departamento, id)
    if not db_dep:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return db_dep

@router.put("/{id}")
def actualizar_departamento(id: int, dep_nuevo: Departamento, session: Session = Depends(get_session)):
    db_dep = session.get(Departamento, id)
    if not db_dep:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    dep_data = dep_nuevo.model_dump(exclude_unset=True)
    for key, value in dep_data.items():
        setattr(db_dep, key, value)
    session.add(db_dep)
    session.commit()
    session.refresh(db_dep)
    return db_dep

@router.delete("/{id}")
def borrar_departamento(id: int, session: Session = Depends(get_session)):
    db_dep = session.get(Departamento, id)
    if not db_dep:
        raise HTTPException(status_code=404, detail="No encontrado")
    session.delete(db_dep)
    session.commit()
    return {"status": "borrado"}