NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala a partir de uma tônica e uma tonalidade.

    Parameters:
        tonica: Nota que será a tônica da escala
        tonalidade: a tonalidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus correspondentes.

    Raises:
        ValueError: Se a tonica não for uma nova válida
        KeyError: Se a escala não exista ou não foi implementada

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'maior')
        {'notas': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """  # noqa: E501
    tonica = tonica.upper()

    try:
        tonica_pos = NOTAS.index(tonica)
        intervalos = ESCALAS[tonalidade]
    except ValueError:
        raise ValueError(f'Nota inválida, tente uma dessas {NOTAS}')
    except KeyError:
        raise KeyError(f'Escala não existe, tente uma dessas {list(ESCALAS.keys())}')

    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % len(NOTAS)
        temp.append(NOTAS[nota])

    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
