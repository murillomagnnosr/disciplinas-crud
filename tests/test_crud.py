from app.routes import *

def test_create():
    d = {"titulo": "Teste", "data_inicio": "2026", "data_fim": "2026", "vagas": 10, "verao": False}
    result = create_disciplina(d)
    assert result == d

def test_read():
    assert isinstance(get_disciplinas(), list)

def test_update():
    d = {"titulo": "Nova"}
    create_disciplina(d)
    updated = update_disciplina(0, {"titulo": "Atualizado"})
    assert updated["titulo"] == "Atualizado"

def test_delete():
    create_disciplina({"titulo": "Temp"})
    delete_disciplina(0)
    assert isinstance(get_disciplinas(), list)
