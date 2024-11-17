from pytest import raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_must_work_with_lowercase_notes():
    tonica = "c"
    tonalidade = "maior"

    result = escala(tonica, tonalidade)

    assert result


def test_must_return_error_when_note_is_not_valid():
    tonica = "z"
    tonalidade = "maior"

    error_message = f"Nota inválida, tente uma dessas {NOTAS}"

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert error_message == str(error.value)


def test_must_return_error_when_scale_is_not_valid():
    tonica = "C"
    tonalidade = "tonalidade_invalida"

    error_message = f"Escala não existe, tente uma dessas {list(ESCALAS.keys())}"

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert error_message == error.value.args[0]
