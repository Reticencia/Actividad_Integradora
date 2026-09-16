import pytest 
from conversor import celsius_fahrenheit, kilometros_millas, pesos_dolares

#ID:PR1
#Prueba parametros y con marker unitario
@pytest.mark.unit
@pytest.mark.parametrize("entrada_celsius, resultado_fahrenheit", [
    (0, 32.00),
    (100, 212.00),
    (-40, -40.00)
])

def test_celsius_fahrenheit(entrada_celsius, resultado_fahrenheit):
    assert celsius_fahrenheit(entrada_celsius) == resultado_fahrenheit

#ID:PR2
# Prueba de distancia
@pytest.mark.unit
def test_kilometros_millas():
    assert kilometros_millas(1) == 0.62
    assert kilometros_millas(5) == 3.11
    assert kilometros_millas(10) == 6.21

#ID:PR3
# Prueba de pesos a dolares
@pytest.mark.unit
def test_pesos_dolares():
    assert pesos_dolares(18.50) == 1.00
    assert pesos_dolares(92.50) == 5.00
    assert pesos_dolares(185.00) == 10.00