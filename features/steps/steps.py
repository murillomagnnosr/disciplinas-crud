from behave import given, when, then
from app.routes import *

@given('que tenho dados válidos')
def step_given(context):
    context.disciplina = {"titulo": "Matemática"}

@when('eu criar a disciplina')
def step_when(context):
    context.result = create_disciplina(context.disciplina)

@then('ela deve existir')
def step_then(context):
    assert context.result in get_disciplinas()
