from notas_musicais.escalas import escala


def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas_da_escala, _ = escala(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]


def acorde(cifra):
    """
    Examples:
      >>> acorde('C')
      {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
    """
    if 'm' in cifra:
        nota, _ = cifra.split('m')
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']
    elif '°' in cifra:
        nota, _ = cifra.split('°')
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V-']
    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
