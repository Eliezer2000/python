def notas(*n, sit=False):
    """
    => Função para analisar notas de alunos e avaliar sua situação.
    :param n: Notas para a análise.
    :param sit: Valor opcional indicando situação do aluno [Boa], [Razoavel], [Ruim]
    :return: Dicionário com várias informações sobre a turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/ len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r


resp = notas(5.5, 9.5, 10, 6.5,sit=True)
#print(resp)
help(notas)
