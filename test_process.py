import pytest
from process import process

# caso de prueba 1 
#ruta D || se prueba un valor positivo para verificar que se devuelve "positivo" y "par"

@pytest.mark.statement_coverage
@pytest.mark.parametrize("input, expected", 
    [([2], ["positivo", "par"])])
def test_statement_coverage(input, expected):
    assert process(input) == expected






