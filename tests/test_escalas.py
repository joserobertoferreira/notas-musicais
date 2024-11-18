from pytest import mark, raises  # noqa: PT013

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_must_work_with_lowercase_notes():
    tonica = 'c'
    tonalidade = 'maior'

    result = escala(tonica, tonalidade)

    assert result


def test_must_return_error_when_note_is_not_valid():
    tonica = 'z'
    tonalidade = 'maior'

    error_message = f'Nota inválida, tente uma dessas {NOTAS}'

    with raises(ValueError) as error:  # noqa: PT011
        escala(tonica, tonalidade)

    assert error_message == str(error.value)


def test_must_return_error_when_scale_is_not_valid():
    tonica = 'C'
    tonalidade = 'tonalidade_invalida'

    error_message = f'Escala não existe, tente uma dessas {list(ESCALAS.keys())}'

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert error_message == error.value.args[0]


@mark.parametrize(
    ('tonica', 'esperado'),
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_must_return_correct_notes(tonica, esperado):
    result = escala(tonica, 'maior')
    assert result['notas'] == esperado
