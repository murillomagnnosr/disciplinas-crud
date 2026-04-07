disciplinas = []

def create_disciplina(data):
    disciplinas.append(data)
    return data

def get_disciplinas():
    return disciplinas

def update_disciplina(index, nova):
    disciplinas[index] = nova
    return nova

def delete_disciplina(index):
    return disciplinas.pop(index)
