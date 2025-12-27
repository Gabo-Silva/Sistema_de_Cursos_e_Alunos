# Importando minhas funções.
import gerenciador
# Lista com as minhas funções.
funcoes = [gerenciador.cadastrarAluno, gerenciador.listarAlunos, gerenciador.removerAluno,
           gerenciador.cadastrarCursos, gerenciador.listarCursos, gerenciador.removerCurso, gerenciador.matricularAluno, gerenciador.listarCursosAluno, gerenciador.listarAlunosDeCurso, gerenciador.cancelarMatricula]
while True:
    # Criando meu banco de dados.
    gerenciador.criarBanco()
    # Menu
    opcao_escolhida = gerenciador.menu('Cadastrar Aluno', 'Listar Alunos', 'Remover Aluno', 'Cadastrar Curso', 'Listar Cursos', 'Remover Curso',
                                       'Matricular Aluno em Curso', 'Listar Cursos de um Aluno', 'Listar Alunos de um Curso', 'Cancelar Matrícula')
    # Se a opção escolhida pelo usuário for zero, o programa termina.
    if opcao_escolhida == 0:
        break
    else:
        # Chamando uma das minhas funções.
        funcoes[opcao_escolhida - 1]()
# Fim
print('-' * 120)
print('OBRIGADO POR USAR O MEU SISTEMA DE CURSOS E ALUNOS'.center(120))
print('-' * 120)
