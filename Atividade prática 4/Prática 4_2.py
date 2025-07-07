def registrar_notas():
    alunos = []
    total_notas = 0
    total_alunos = 0

    try:
        qtd_alunos = int(input("Digite o número de alunos: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        return

    for i in range(qtd_alunos):
        nome = input(f"\nDigite o nome do aluno {i+1}: ")
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
        except ValueError:
            print("Nota inválida. Use ponto (.) em vez de vírgula (,).")
            return

        alunos.append((nome, nota))
        total_notas += nota
        total_alunos += 1

    print("\nNotas dos alunos:")
    for aluno in alunos:
        print(f"{aluno[0]}: {aluno[1]}")

    if total_alunos > 0:
        media_turma = total_notas / total_alunos
        print(f"\nMédia da turma: {media_turma:.2f}")
    else:
        print("Nenhuma nota registrada.")

registrar_notas()