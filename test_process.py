import pytest
from process import process

# caso de prueba 1 
#ruta D || se prueba un valor positivo para verificar que se devuelve "positivo" y "par"

@pytest.mark.statement_coverage
@pytest.mark.parametrize("input, expected", 
    [([2], ["positivo", "par"])])
def test_statement_coverage(input, expected):
    assert process(input) == expected

#Caso de prueba 2 
@pytest.mark.branch_coverage
@pytest.mark.parametrize("input, expected", 
                         [
                             ([2], ["positivo", "par"]),([-1],[]), ([],[])
                         ]
                         )
def test_branch_coverage(input, expected):
    assert process(input) == expected

#caso de prueba 3
@pytest.mark.path_coverage
@pytest.mark.parametrize("input, expected", 
                         [
                             ([-1,-1], []),
                             ([-1,1], ["positivo"]), 
                             ([-1,0], ["par"]),
                             ([-1,2], ["positivo","par"]),
                             ([1,-1], ["positivo"]),
                             ([1,1], ["positivo","positivo"]),
                             ([1,2], ["positivo","positivo","par"]),
                             ([0,-1], ["par"]),
                             ([0,1], ["par","positivo"]),
                             ([0,0], ["par","par"]),
                             ([0,2], ["par","positivo","par"]),
                             ([2,-1], ["positivo","par"]),
                             ([2,1], ["positivo","par","positivo"]),
                             ([2,0], ["positivo","par","par"]),
                             ([2,2], ["positivo","par","positivo","par"]),
                         ]
                         )
def test_path_coverage(input, expected):
    assert process(input) == expected
