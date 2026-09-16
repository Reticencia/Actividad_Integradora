def celsius_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def kilometros_millas(kilometros):
    return round(kilometros * 0.621371, 2)

def pesos_dolares(peso):
    tasa_cambio = 18.50
    return round(peso / tasa_cambio, 2)

if __name__ == "__main__":
    print("--- Conversor de Unidades ---")
    valor = float(input("Ingresa el valor numérico a convertir: "))
    print(f"{valor} Celsius a Fahrenheit: {celsius_fahrenheit(valor)}")
    print(f"{valor} Kilómetros a Millas: {kilometros_millas(valor)}")
    print(f"{valor} Pesos a Dólares: {pesos_dolares(valor)}")