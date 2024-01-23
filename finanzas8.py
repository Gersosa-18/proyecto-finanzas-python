import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import datetime as dt

def obtener_datos_accion():
    # Función para obtener datos de una acción desde el usuario
    ticker = input("Ingresa el símbolo de la acción (ej. AAPL): ").upper()
    fecha_compra = input("Ingresa la fecha de compra (AAAA-MM-DD): ")
    precio_compra = float(input("Ingresa el precio de compra: "))
    return ticker, fecha_compra, precio_compra

def graficar_cambio_porcentual(ticker, fecha_compra, precio_compra):
    # Descargar datos históricos con intervalo de "1d"
    fecha_fin = dt.datetime.now().strftime('%Y-%m-%d')
    df = yf.download(ticker, start=fecha_compra, end=fecha_fin, interval="1d")

    # Extraer precios de cierre
    df['Cierre'] = df['Close'].ffill()

    # Eliminar la columna 'Open'
    df = df.drop('Open', axis=1)

    # Calcular el cambio porcentual diario desde la fecha de compra
    df['Cambio Porcentual Diario'] = ((df['Cierre'] - precio_compra) / precio_compra) * 100

    # Obtén el último cambio porcentual
    ultimo_cambio_porcentual = df['Cambio Porcentual Diario'].iloc[-1]

    # Mostrar el DataFrame
    print(df[['Cierre', 'Cambio Porcentual Diario']])

    # Graficar el cambio porcentual diario
    plt.figure(figsize=(10, 6))
    df['Cambio Porcentual Diario'].plot(label='Cambio Porcentual Diario')
    plt.axhline(y=0, color='black', linestyle='--', label='Cero Cambio Porcentual')
    plt.title(f'Cambio Porcentual Diario para {ticker}\nÚltimo Cambio Porcentual: {ultimo_cambio_porcentual:.2f}%\nFecha de Compra: {fecha_compra} | Precio de Compra: {precio_compra}')
    plt.xlabel('Fecha')
    plt.ylabel('Cambio Porcentual')
    plt.legend()
    plt.show()

# Programa principal
while True:
    opcion = input("¿Quieres analizar una acción? (Sí/No): ").lower()
    if opcion != 'si':
        break
    
    ticker, fecha_compra, precio_compra = obtener_datos_accion()
    graficar_cambio_porcentual(ticker, fecha_compra, precio_compra)
