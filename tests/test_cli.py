import pytest
from typer.testing import CliRunner

from notas_musicais.cli import app

runner = CliRunner()


def test_cli_must_return_zero_to_stdout():
    result = runner.invoke(app)

    assert result.exit_code == 0


@pytest.mark.parametrize('nota', ['C', 'D', 'E', 'F', 'G', 'A', 'B'])
def test_cli_must_have_notes(nota):
    result = runner.invoke(app)

    assert nota in result.stdout


@pytest.mark.parametrize('nota', ['F', 'G', 'A', 'A#', 'C', 'D', 'E'])
def test_cli_must_have_notes_from_f(nota):
    # Nota Fá
    result = runner.invoke(app, ['F'])

    assert nota in result.stdout


@pytest.mark.parametrize('grau', ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII'])
def test_cli_must_have_all_scales(grau):
    result = runner.invoke(app, ['F'])

    assert grau in result.stdout
