# Paso 1: Definir el valor actual del Euro y Dólar respecto al Peso Mexicano

tipo_cambio_eur_a_mxn = 23.70 #En un caso más realista habría que consumir info actualizada de una base de datos
tipo_cambio_usd_a_mxn = 20.75 #En un caso más realista habría que consumir info actualizada de una base de datos

# Paso 2: Solicitar al usuario el tipo de conversión (euro a Mex o Dólar a Mex)

tipo_conversion = input("Ingrese la moneda origen para la conversión (EUR/USD): ")

# Paso 3: Solicitar a usuario el monto a convertir

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

# Paso 4: Realizar la conversión utilizando el tipo de cambio correspondiente
# Paso 5: Mostrar el resultado de la conversión al usuario

if tipo_conversion.upper() == "EUR":
    resultado = monto_a_convertir * tipo_cambio_eur_a_mxn
    print("El resultado de la conversión de EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mxn
    print("El resultado de la conversión de USD a MXN es:", resultado)
else:
    print("No está disponible este tipo de conversión actualmente")