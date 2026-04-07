Feature: Gerenciamento de Disciplinas

  Scenario: Criar disciplina
    Given que tenho dados válidos
    When eu criar a disciplina
    Then ela deve existir
