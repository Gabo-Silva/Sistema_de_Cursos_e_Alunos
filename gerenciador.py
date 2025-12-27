# Criando meu banco de dados.
def criarBanco():
    global conexao
    global cursor
    import sqlite3
    conexao = sqlite3.connect('cursos.db')
    cursor = conexao.cursor()


def criarTabelas():
    # Criando as tabelas
    cursor.execute('''
    create table if not exists alunos (
                   id integer primary key not null,
                   nome varchar(100) not null,
                   email varchar(255) not null
    );
''')
    cursor.execute('''
    create table if not exists cursos (
                   id integer primary key not null,
                   nome_do_curso varchar(100) not null unique,
                   carga_horaria tinyint unsigned not null
    );
''')
    cursor.execute('''
    create table if not exists matriculas (
                   aluno_id integer not null,
                   curso_id integer not null,
                   foreign key (aluno_id) references alunos (id),
                   foreign key (curso_id) references cursos (id)
    );
''')


def leiaInt(msg, PodeZero=False):
    while True:
        try:
            num = str(input(msg).strip())
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! VALOR INCORRETO')
            print('-' * 120)
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! VALOR INCORRETO')
            print('-' * 120)
        else:
            # Se o parâmetro "PodeZero" for igual a true, esse bloco de comando será ativado.
            if PodeZero == True:
                # Se a variável "num" não conter somente números ou o número digitado for menor do que zero, uma mensagem de erro será exibida.
                if num.isnumeric() == False or int(num) < 0:
                    print('ERRO! VALOR INCORRETO')
                    print('-' * 120)
                else:
                    # Retorna a variável com ela agora sendo do tipo inteiro.
                    return int(num)
            # Se a variável "num" não conter somente números ou o número digitado for menor do que um, uma mensagem de erro será exibida.
            elif num.isnumeric() == False or int(num) < 1:
                print('ERRO! VALOR INCORRETO')
                print('-' * 120)
            else:
                # Retorna a variável com ela agora sendo do tipo inteiro.
                return int(num)


def leiaString(msg):
    while True:
        # Se a variável "msg" for igual a "Nome: ", esse bloco de comando será ativado.
        if msg == 'Nome: ':
            try:
                nome = str(input(msg).strip().title())
                nome_sem_espacos = nome.split()
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! NOME INVÁLIDO')
                print('-' * 120)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! NOME INVÁLIDO')
                print('-' * 120)
            else:
                # Se a variável "nome_sem_espacos" possui somente letras do alfabeto, esse bloco de comando será ativado.
                if ''.join(nome_sem_espacos).isalpha():
                    # Retorna a variável "nome"
                    return nome
                # Se a variável "nome_sem_espacos" não possui somente letras do alfabeto, esse bloco de comando será ativado.
                else:
                    print('ERRO! NOME INVÁLIDO')
                    print('-' * 120)
        # Se a variável "msg" for igual a "Nome do Curso: ", esse bloco de comando será ativado.
        elif msg == 'Nome do Curso: ':
            try:
                nome_curso = str(input(msg).strip().title())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! NOME INVÁLIDO')
                print('-' * 120)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! NOME INVÁLIDO')
                print('-' * 120)
            # Se a variável "nome_curso" estiver vazia, uma mensagem de erro será exibida.
            if len(nome_curso) == 0:
                print('ERRO! NOME INVÁLIDO')
                print('-' * 120)
            else:
                # Retorna a variável "nome_curso".
                return nome_curso
        # Se a variável "msg" for igual a "Email: ", esse bloco de comando será ativado.
        elif msg == 'Email: ':
            import re
            # Caracteres que serão aceitas no email.
            caracteres = r'[A-Za-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,7}'
            try:
                email = str(input(msg).strip())
            # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
            except KeyboardInterrupt:
                print('\nERRO! EMAIL INVÁLIDO')
                print('-' * 120)
            # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
            except EOFError:
                print('ERRO! EMAIL INVÁLIDO')
                print('-' * 120)
            else:
                # Se todas as caracteres estiverem corretas, a variável "email" será retornada.
                if re.fullmatch(caracteres, email):
                    return email
                else:
                    print('ERRO! EMAIL INVÁLIDO')
                    print('-' * 120)


def continuar(msg, Sair=False):
    # Função responsável pro determinar se a função escolhida pelo usuário irá continuar ou não.
    while True:
        try:
            res_continuar = str(input(msg).strip().upper())
        # Caso ocorra uma interrupção indevida por parte do usuário, uma mensagem de erro será exibida.
        except KeyboardInterrupt:
            print('\nERRO! OPÇÃO INVÁLIDA')
            print('-' * 120)
        # Caso ocorra algum problema durante a leitura, uma mensagem de erro será exibida.
        except EOFError:
            print('ERRO! OPÇÃO INVÁLIDA')
            print('-' * 120)
        else:
            # Se o parâmetro "Sair" for igual a "True", esse bloco de comando será ativado.
            if Sair == True:
                # Se a variável "res_continuar" for diferente de "S", uma mensagem de erro será exibida.
                if res_continuar != 'S':
                    print('ERRO! OPÇÃO INVÁLIDA')
                    print('-' * 120)
                else:
                    return res_continuar
            else:
                # Se a variável "res_continuar" for diferente de "S" ou "N", uma mensagem de erro será exibida.
                if res_continuar not in ('S', 'N'):
                    print('ERRO! OPÇÃO INVÁLIDA')
                    print('-' * 120)
                else:
                    return res_continuar


def menu(* opcoes):
    # Chamando a função criar tabelas.
    criarTabelas()
    # Menu.
    print(f'-' * 120)
    print(f'{'Alunos':>20} {'Cursos':>42} {'Matrículas':>42}')
    print('-' * 120)
    print(f'1 - {opcoes[0]} {'4':>30} - {opcoes[3]} {'7':>18} - {opcoes[6]}')
    print(f'2 - {opcoes[1]} {'5':>32} - {opcoes[4]} {'8':>20} - {opcoes[7]}')
    print(
        f'{'3'} - {opcoes[2]} {'6':>32} - {opcoes[5]} {'9':>20} - {opcoes[8]}')
    print(f'{'10':>87} - {opcoes[9]}')
    print('-' * 120)
    while True:
        res_opcao = leiaInt(
            'Deseja qual opção [Digite 0 para sair]? ', PodeZero=True)
        # Se a opção escolhida pelo usuário for maior que o número de opções predeteminadas, uma mensagem de erro será exibida.
        if res_opcao > len(opcoes):
            print('ERRO! VALOR INCORRETO')
            print('-' * 120)
        else:
            return res_opcao


def cadastrarAluno():
    while True:
        # Pegando as informações do alunos.
        print('-' * 120)
        print('CADASTRO DE ALUNO'.center(120))
        print('-' * 120)
        nome_aluno = leiaString('Nome: ')
        print('-' * 120)
        email_aluno = leiaString('Email: ')
        cursor.execute(
            f'insert into alunos (nome, email) values ("{nome_aluno}", "{email_aluno}")')
        conexao.commit()
        print('-' * 120)
        print('CADASTRO DO ALUNO CONCLUÍDO'.center(120))
        print('-' * 120)
        usuario_escolha = continuar('Quer continuar [S/N]? ')
        # Se o usuário não quiser continuar, a função será encerrada.
        if usuario_escolha == 'N':
            conexao.close()
            break


def listarAlunos():
    # Listando todos os alunos cadastrados.
    cursor.execute('select * from alunos')
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    else:
        print('-' * 120)
        print('ALUNOS CADASTRADOS'.center(120))
        print('-' * 120)
        print('-'.center(120))
        cursor.execute('select * from alunos order by nome')
        for indice, alunos in enumerate(cursor.fetchall()):
            print('-' * 120)
            print(f'{indice + 1}'.center(120))
            print('-' * 120)
            print(f'Nome do Aluno: {alunos[1]}')
            print(f'Email do Aluno: {alunos[2]}')
        print('-' * 120)
        usuario_escolha = continuar('Sair[S]? ', Sair=True)
        # Se o usuário decidir sair, a função será encerrada.
        if usuario_escolha == 'S':
            conexao.close()


def cadastrarCursos():
    # Pegando as informações dos cursos.
    while True:
        print('-' * 120)
        print('CADASTRAR CURSO'.center(120))
        print('-' * 120)
        nome_do_curso = leiaString('Nome do Curso: ')
        print('-' * 120)
        carga_horaria = leiaInt('Carga Horária: ')
        try:
            cursor.execute(
                f'insert into cursos (nome_do_curso, carga_horaria) values ("{nome_do_curso}", "{carga_horaria}")')
            conexao.commit()
        # Se o curso for um curso repetido, esse bloco de comando será ativado.
        except:
            print('-' * 120)
            print('ERRO! CURSO JÁ EXISTENTE'.center(120))
            print('-' * 120)
            print('-'.center(120))
        else:
            print('-' * 120)
            print('CADASTRO DO CURSO CONCLUÍDO'.center(120))
            print('-' * 120)
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break


def listarCursos():
    # Lista todos os cursos existentes
    cursor.execute('select * from cursos')
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    else:
        print('-' * 120)
        print('CURSOS CADASTRADOS'.center(120))
        print('-' * 120)
        print('-'.center(120))
        cursor.execute('select * from cursos order by nome_do_curso')
        for indice, cursos in enumerate(cursor.fetchall()):
            print('-' * 120)
            print(f'{indice + 1}'.center(120))
            print('-' * 120)
            print(f'Nome do Curso: {cursos[1]}')
            print(f'Carga Horária: {cursos[2]} Horas')
        print('-' * 120)
        usuario_escolha = continuar('Sair[S]? ', Sair=True)
        # Se o usuário decidir sair, a função será encerrada.
        if usuario_escolha == 'S':
            conexao.close()


def matricularAluno():
    # Função responsável por matricular os alunos nas disciplinas.
    cursor.execute('select * from alunos')
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    cursor.execute('select * from cursos')
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    # Se possuir pelo menos um aluno e um curso, esse bloco de comando será ativado.
    if len(cursor.execute('select * from alunos').fetchall()) > 0 and len(cursor.execute('select * from cursos').fetchall()) > 0:
        while True:
            aluno_encontrado = 0
            print('-' * 120)
            print('MATRICULAR ALUNO'.center(120))
            print('-' * 120)
            # Exibindo todos os alunos.
            cursor.execute('select * from alunos order by nome')
            for i, a in enumerate(cursor.fetchall()):
                print(f'{i + 1} - {a[1]}')
                print('-' * 120)
            while True:
                # Usuário escolhe qual aluno ele quer.
                indice_aluno = leiaInt(
                    'Qual aluno você deseja matricular [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from alunos order by nome')
                for indice_encontrado, aluno in enumerate(cursor.fetchall()):
                    # Caso o aluno seja encontrado, esse bloco de comando será ativado.
                    if indice_encontrado == indice_aluno - 1 or indice_aluno == 0:
                        # Pegando o id do aluno.
                        aluno_id = aluno[0]
                        # Variável "aluno_encontrado" ganhando +1.
                        aluno_encontrado += 1
                # Se a variável "aluno_encontrado" for igual a zero, esse bloco de comando será ativado.
                if aluno_encontrado == 0:
                    print('ERRO! ALUNO NÃO ENCONTRADO')
                    print('-' * 120)
                else:
                    break
            # Se o número digitado pelo usuário foi zero, essa função será encerrada.
            if indice_aluno == 0:
                conexao.close()
                break
            else:
                # Exibindo os cursos.
                print('-' * 120)
                print('CURSOS'.center(120))
                print('-' * 120)
                cursor.execute('select * from cursos order by nome_do_curso')
                for indice_curso, curso in enumerate(cursor.fetchall()):
                    print(f'{indice_curso + 1} - {curso[1]}')
                    print('-' * 120)
                while True:
                    curso_repetido = 0
                    curso_encontrado = 0
                    # Perguntando qual curso o aluno será matriculado.
                    res_curso = leiaInt(
                        f'Qual curso o aluno será matriculado [Digite 0 para sair]? ', PodeZero=True)
                    cursor.execute(
                        'select * from cursos order by nome_do_curso')
                    for i_c, c in enumerate(cursor.fetchall()):
                        # Caso o curso seja encontrado, esse bloco de comando será ativado.
                        if i_c == res_curso - 1 or res_curso == 0:
                            # Pegando o nome do curso.
                            curso_nome = c[1]
                            # Pegando o id do curso.
                            curso_id = c[0]
                            # Variável "curso_encontrado" ganhando +1.
                            curso_encontrado += 1
                    # Se o número digitado pelo usuário foi zero, esse parte do comando será encerrada.
                    if res_curso == 0:
                        break
                    # Se a variável "curso_encontrado" for igual a zero, esse bloco de comando será ativado.
                    elif curso_encontrado == 0:
                        print('ERRO! CURSO NÃO ENCONTRADO')
                        print('-' * 120)
                    else:
                        # Caso o aluno já esteja matriculado no curso desejado, uma mensagem de erro será exibida.
                        cursor.execute('select * from alunos order by nome')
                        for i, matricula in enumerate(cursor.fetchall()):
                            if i == indice_aluno - 1:
                                cursor.execute(
                                    f'select nome_do_curso from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]}')
                        for cursos in cursor.fetchall():
                            if cursos[0] == curso_nome:
                                curso_repetido += 1
                        # Caso o aluno já esteja matriculado no curso desejado, uma mensagem de erro será exibida.
                        if curso_repetido > 0:
                            print('ERRO! ALUNO JÁ ESTÁ MATRICULADO NESTE CURSO')
                            print('-' * 120)
                        else:
                            break
                # Se o número digitado pelo usuário foi zero, essa função será encerrada.
                if res_curso == 0:
                    conexao.close()
                    break
                else:
                    # Matriculando o aluno.
                    cursor.execute(
                        f'insert into matriculas (aluno_id, curso_id) values ("{aluno_id}", "{curso_id}")')
                    conexao.commit()
                    print('-' * 120)
                    print('ALUNO MATRICULADO'.center(120))
                    print('-' * 120)
                    usuario_escolha = continuar('Quer continuar [S/N]? ')
                    # Se o usuário não quiser continuar, a função será encerrada.
                    if usuario_escolha == 'N':
                        conexao.close()
                        break


def listarCursosAluno():
    cursor.execute('select * from alunos')
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    cursor.execute('select * from cursos')
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    # Se possuir pelo menos um aluno e um curso, esse bloco de comando será ativado.
    if len(cursor.execute('select * from alunos').fetchall()) > 0 and len(cursor.execute('select * from cursos').fetchall()) > 0:
        while True:
            # Exibindo todos os alunos.
            print('-' * 120)
            print('LISTAR CURSOS DE UM ALUNO'.center(120))
            print('-' * 120)
            cursor.execute('select * from alunos order by nome')
            for indice, aluno in enumerate(cursor.fetchall()):
                print(f'{indice + 1} - {aluno[1]}')
                print('-' * 120)
            while True:
                cursos_encontrados = 0
                res_aluno = leiaInt(
                    'De qual aluno você deseja listar os cursos [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from alunos')
                # Se o número digitado for maior que o tamanho da lista de alunos, uma mensagem de erro será exibida.
                if res_aluno > len(cursor.fetchall()):
                    print('ERRO! ALUNO NÃO ENCONTRADO')
                    print('-' * 120)
                # Se o número for igual a zero, a função será encerrada.
                elif res_aluno == 0:
                    break
                else:
                    # Verificando se o aluno está matriculado em algum curso.
                    cursor.execute('select * from alunos order by nome')
                    for i, matricula in enumerate(cursor.fetchall()):
                        if i == res_aluno - 1:
                            cursor.execute(
                                f'select nome_do_curso, carga_horaria from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                            for cursos_sendo_feitos in cursor.fetchall():
                                cursos_encontrados += 1
                    # Se não tiver, esse bloco de comando será ativado.
                    if cursos_encontrados == 0:
                        print('-' * 120)
                        print(
                            'ESSE ALUNO NÃO ESTÁ MATRICULADO EM NENHUM CURSO'.center(120))
                        print('-' * 120)
                        break
                    else:
                        # Exibindo os cursos do aluno.
                        print('-' * 120)
                        print(
                            'ESSES SÃO OS CURSOS QUE O ALUNO ESTÁ MATRICULADO'.center(120))
                        print('-' * 120)
                        cursor.execute('select * from alunos order by nome')
                        for i, matricula in enumerate(cursor.fetchall()):
                            if i == res_aluno - 1:
                                cursor.execute(
                                    f'select nome_do_curso, carga_horaria from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                                for id, cursos_sendo_feitos in enumerate(cursor.fetchall()):
                                    print(
                                        f'{id + 1} - {cursos_sendo_feitos[0]} - {cursos_sendo_feitos[1]} Horas')
                                    print('-' * 120)
                        if cursos_encontrados > 0:
                            break
            # Se o número for igual a zero, a função será encerrada.
            if res_aluno == 0:
                conexao.close()
                break
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break


def listarAlunosDeCurso():
    cursor.execute('select * from alunos')
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    cursor.execute('select * from cursos')
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    # Se possuir pelo menos um aluno e um curso, esse bloco de comando será ativado.
    if len(cursor.execute('select * from alunos').fetchall()) > 0 and len(cursor.execute('select * from cursos').fetchall()) > 0:
        while True:
            # Exibindo os cursos.
            print('-' * 120)
            print('LISTAR ALUNOS DE UM CURSO'.center(120))
            print('-' * 120)
            cursor.execute('select * from cursos order by nome_do_curso')
            for indice, cursos in enumerate(cursor.fetchall()):
                print(f'{indice + 1} - {cursos[1]}')
                print('-' * 120)
            while True:
                alunos_encontrados = 0
                res_curso = leiaInt(
                    'De qual curso você deseja listar os alunos [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from cursos')
                # Se o número digitado for maior que o tamanho da lista de alunos, uma mensagem de erro será exibida.
                if res_curso > len(cursor.fetchall()):
                    print('ERRO! CURSO NÃO ENCONTRADO')
                    print('-' * 120)
                # Se o número for igual a zero, a função será encerrada.
                elif res_curso == 0:
                    break
                else:
                    # Verificando se o curso tem alunos matriculados.
                    cursor.execute(
                        'select * from cursos order by nome_do_curso')
                    for i, matricula in enumerate(cursor.fetchall()):
                        if i == res_curso - 1:
                            cursor.execute(
                                f'select nome from alunos inner join matriculas on alunos.id = matriculas.aluno_id where matriculas.curso_id = {matricula[0]} order by nome')
                            for alunos_fazendo_curso in cursor.fetchall():
                                alunos_encontrados += 1
                    # Se não tiver, esse bloco de comando será ativado.
                    if alunos_encontrados == 0:
                        print('-' * 120)
                        print(
                            'NÃO HÁ NENHUM ALUNO MATRICULADO NESSE CURSO'.center(120))
                        print('-' * 120)
                        break
                    else:
                        # Exibindo os alunos de um curso.
                        print('-' * 120)
                        print(
                            'ESSES SÃO OS ALUNOS MATRICULADOS NESSE CURSO'.center(120))
                        print('-' * 120)
                        cursor.execute(
                            'select * from cursos order by nome_do_curso')
                        for i, matricula in enumerate(cursor.fetchall()):
                            if i == res_curso - 1:
                                cursor.execute(
                                    f'select nome, email from alunos inner join matriculas on alunos.id = matriculas.aluno_id where matriculas.curso_id = {matricula[0]} order by nome')
                                for id, alunos_desse_curso in enumerate(cursor.fetchall()):
                                    print(
                                        f'{id + 1} - {alunos_desse_curso[0]}')
                                    print(f'Email: {alunos_desse_curso[1]}')
                                    print('-' * 120)
                        if alunos_encontrados > 0:
                            break
            # Se o número for igual a zero, a função será encerrada.
            if res_curso == 0:
                conexao.close()
                break
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break


def cancelarMatricula():
    cursor.execute('select * from alunos')
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    cursor.execute('select * from cursos')
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    # Se possuir pelo menos um aluno e um curso, esse bloco de comando será ativado.
    if len(cursor.execute('select * from alunos').fetchall()) > 0 and len(cursor.execute('select * from cursos').fetchall()) > 0:
        while True:
            # Exibindo todos os alunos.
            print('-' * 120)
            print('CANCELAR MATRICULA'.center(120))
            print('-' * 120)
            cursor.execute('select * from alunos order by nome')
            for indice, aluno in enumerate(cursor.fetchall()):
                print(f'{indice + 1} - {aluno[1]}')
                print('-' * 120)
            while True:
                cursos_encontrados = 0
                res_aluno = leiaInt(
                    'De qual aluno você deseja listar os cursos [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from alunos')
                # Se o número digitado for maior que o tamanho da lista de alunos, uma mensagem de erro será exibida.
                if res_aluno > len(cursor.fetchall()):
                    print('ERRO! ALUNO NÃO ENCONTRADO')
                    print('-' * 120)
                # Se o número for igual a zero, a função será encerrada.
                elif res_aluno == 0:
                    break
                else:
                    # Verificando se o aluno esta matriculado em algum curso.
                    cursor.execute('select * from alunos order by nome')
                    for i, matricula in enumerate(cursor.fetchall()):
                        if i == res_aluno - 1:
                            cursor.execute(
                                f'select nome_do_curso, carga_horaria from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                            for cursos_sendo_feitos in cursor.fetchall():
                                cursos_encontrados += 1
                    # Se não estiver, esse bloco de comando será ativado.
                    if cursos_encontrados == 0:
                        print('-' * 120)
                        print(
                            'ESSE ALUNO NÃO ESTÁ MATRICULADO EM NENHUM CURSO'.center(120))
                        print('-' * 120)
                        res_curso = 1
                        break
                    else:
                        # Exibindo os cursos do aluno.
                        print('-' * 120)
                        print(
                            'ESSES SÃO OS CURSOS QUE O ALUNO ESTÁ MATRICULADO'.center(120))
                        print('-' * 120)
                        cursor.execute('select * from alunos order by nome')
                        for i, matricula in enumerate(cursor.fetchall()):
                            if i == res_aluno - 1:
                                cursor.execute(
                                    f'select nome_do_curso, carga_horaria from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                                for id, cursos_sendo_feitos in enumerate(cursor.fetchall()):
                                    print(
                                        f'{id + 1} - {cursos_sendo_feitos[0]} - {cursos_sendo_feitos[1]} Horas')
                                    print('-' * 120)
                        while True:
                            res_curso = leiaInt(
                                'De qual curso você quer cancelar a matrícula [Digite 0 para sair]? ', PodeZero=True)
                            # Se o número for igual a zero, a função será encerrada.
                            if res_curso == 0:
                                break
                            else:
                                # Desmatriculando o aluno do curso escolhido.
                                cursor.execute(
                                    'select * from alunos order by nome')
                                for i_c, matricula in enumerate(cursor.fetchall()):
                                    if i_c == res_aluno - 1:
                                        cursor.execute(
                                            f'select id from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                                        for indice_do_curso, curso in enumerate(cursor.fetchall()):
                                            if indice_do_curso == res_curso - 1:
                                                id_curso = curso[0]
                                cursor.execute(
                                    'select * from alunos order by nome')
                                for i_a, aluno in enumerate(cursor.fetchall()):
                                    if i_a == res_aluno - 1:
                                        id_aluno = aluno[0]
                                try:
                                    cursor.execute(
                                        f'delete from matriculas where aluno_id = "{id_aluno}" and curso_id = "{id_curso}"')
                                # Caso o curso não exista, essa mensagem de erro será exibida.
                                except:
                                    print('ERRO! CURSO INEXISTENTE')
                                    print('-' * 120)
                                else:
                                    conexao.commit()
                                    print('-' * 120)
                                    print(
                                        'MATRICULA CANCELADA COM SUCESSO'.center(120))
                                    print('-' * 120)
                                    break
                        break
            # Se o número for igual a zero, a função será encerrada.
            if res_aluno == 0 or res_curso == 0:
                conexao.close()
                break
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break


def removerAluno():
    # Se não existir nenhum aluno cadastrado, esse bloco de comando será ativado.
    cursor.execute('select * from alunos')
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM ALUNO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    else:
        while True:
            print('-' * 120)
            print('REMOVER ALUNO'.center(120))
            print('-' * 120)
            # Exibindo todos os alunos.
            cursor.execute('select * from alunos order by nome')
            for indice, aluno in enumerate(cursor.fetchall()):
                print(f'{indice + 1} - {aluno[1]}')
                print(f'Email: {aluno[2]}')
                print('-' * 120)
            while True:
                res_remover = leiaInt(
                    'Qual aluno você deseja remover [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from alunos')
                # Se o número digitado for maior que o tamanho da lista de alunos, uma mensagem de erro será exibida.
                if res_remover > len(cursor.fetchall()):
                    print('ERRO! ALUNO NÃO ENCONTRADO')
                    print('-' * 120)
                # Se o número for igual a zero, a função será encerrada.
                elif res_remover == 0:
                    break
                else:
                    # Caso o aluno esteja matriculado em alguma disciplina.
                    cursor.execute('select * from alunos order by nome')
                    for i, matricula in enumerate(cursor.fetchall()):
                        if i == res_remover - 1:
                            cursor.execute(
                                f'select nome_do_curso, carga_horaria from cursos inner join matriculas on cursos.id = matriculas.curso_id where matriculas.aluno_id = {matricula[0]} order by nome_do_curso')
                            número_de_cursos = len(cursor.fetchall())
                    # Uma mensagem de erro será exibida.
                    if número_de_cursos > 0:
                        print('-' * 120)
                        print(
                            'ERRO! ESSE ALUNO ESTÁ MATRICULADO EM UM CURSO'.center(120))
                        print('-' * 120)
                        break
                    else:
                        # Removendo o aluno.
                        cursor.execute('select * from alunos order by nome')
                        for indice_pra_remover, aluno in enumerate(cursor.fetchall()):
                            if indice_pra_remover == res_remover - 1:
                                cursor.execute(
                                    f'delete from alunos where id = "{aluno[0]}"')
                                conexao.commit()
                                print('-' * 120)
                                print('ALUNO REMOVIDO COM SUCESSO'.center(120))
                                print('-' * 120)
                        break
            # Se o número for igual a zero, a função será encerrada.
            if res_remover == 0:
                conexao.close()
                break
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break


def removerCurso():
    # Se não existir nenhum curso cadastrado, esse bloco de comando será ativado.
    cursor.execute('select * from cursos')
    if len(cursor.fetchall()) == 0:
        print('-' * 120)
        print('NENHUM CURSO CADASTRADO'.center(120))
        print('-' * 120)
        print('-'.center(120))
    else:
        while True:
            print('-' * 120)
            print('REMOVER CURSO'.center(120))
            print('-' * 120)
            # Exibindo todos os cursos.
            cursor.execute('select * from cursos order by nome_do_curso')
            for indice, cursos in enumerate(cursor.fetchall()):
                print(f'{indice + 1} - {cursos[1]}')
                print('-' * 120)
            while True:
                res_curso_remover = leiaInt(
                    'Qual curso você deseja remover [Digite 0 para sair]? ', PodeZero=True)
                cursor.execute('select * from cursos')
                # Se o número digitado for maior que o tamanho da lista de alunos, uma mensagem de erro será exibida.
                if res_curso_remover > len(cursor.fetchall()):
                    print('ERRO! CURSO NÃO ENCONTRADO')
                    print('-' * 120)
                # Se o número for igual a zero, a função será encerrada.
                elif res_curso_remover == 0:
                    break
                else:
                    # Caso o curso tenha algum aluno matriculado.
                    cursor.execute(
                        'select * from cursos order by nome_do_curso')
                    for i, matricula in enumerate(cursor.fetchall()):
                        if i == res_curso_remover - 1:
                            cursor.execute(
                                f'select nome from alunos inner join matriculas on alunos.id = matriculas.aluno_id where matriculas.curso_id = {matricula[0]} order by nome')
                            alunos_fazendo_curso = len(cursor.fetchall())
                    # Uma mensagem de erro será exibida.
                    if alunos_fazendo_curso > 0:
                        print('-' * 120)
                        print(
                            'ERRO! ESSE CURSO TEM ALUNOS MATRICULADOS'.center(120))
                        print('-' * 120)
                        break
                    else:
                        # Removendo o curso.
                        cursor.execute(
                            'select * from cursos order by nome_do_curso')
                        for indice_remover, curso in enumerate(cursor.fetchall()):
                            if indice_remover == res_curso_remover - 1:
                                cursor.execute(
                                    f'delete from cursos where id = "{curso[0]}"')
                                conexao.commit()
                                print('-' * 120)
                                print('CURSO REMOVIDO COM SUCESSO'.center(120))
                                print('-' * 120)
                        break
            # Se o número for igual a zero, a função será encerrada.
            if res_curso_remover == 0:
                conexao.close()
                break
            usuario_escolha = continuar('Quer continuar [S/N]? ')
            # Se o usuário não quiser continuar, a função será encerrada.
            if usuario_escolha == 'N':
                conexao.close()
                break
