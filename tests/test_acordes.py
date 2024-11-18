import pytest

from notas_musicais.acordes import acorde

"""
Entrada:
acorde C

Saída:
I - III - V
C - E - G

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""


@pytest.mark.parametrize(
    ('nota', 'saida'),
    [('C', ['C', 'E', 'G']), ('Cm', ['C', 'D#', 'G']), ('F#', ['F#', 'A#', 'C#'])],
)
def test_acorde_deve_retornar_as_notas_correspondentes(nota, saida):
    notas, _ = acorde(nota).values()

    assert notas == saida


@pytest.mark.parametrize(
    ('cifra', 'saida'),
    [('C', ['I', 'III', 'V']), ('Cm', ['I', 'III-', 'V']), ('C°', ['I', 'III-', 'V-'])],
)
def test_acorde_deve_retornar_as_graus_correspondentes(cifra, saida):
    _, graus = acorde(cifra).values()

    assert graus == saida
