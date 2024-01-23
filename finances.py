import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt

def descargar_datos(symbol, start_date, end_date):
    try:
        data = yf.download(symbol, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"No se pudieron descargar datos para {symbol}. Error: {e}")
        return None

def calcular_rsi(data):
    try:
        rsi = ta.rsi(data['Close'])
        return rsi
    except Exception as e:
        print(f"No se pudo calcular el RSI. Error: {e}")
        return None

def comparar_rsi(acciones, start_date, end_date):
    plt.figure(figsize=(10, 5))

    for accion in acciones:
        print(f"Procesando {accion}...")
        datos = descargar_datos(accion, start_date, end_date)
        
        if datos is None or datos.empty:
            print(f"No se encontraron datos para {accion}.")
            continue

        rsi = calcular_rsi(datos)

        if rsi is not None and not rsi.isnull().all():
            plt.plot(datos.index, rsi, label=f"{accion} RSI")

    # Agregar líneas horizontales en 30% y 70%
    plt.axhline(y=30, color='r', linestyle='--', label='RSI 30%')
    plt.axhline(y=70, color='g', linestyle='--', label='RSI 70%')

    plt.title("Comparación de RSI")
    plt.xlabel("Fecha")
    plt.ylabel("RSI")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Pedir al usuario que ingrese los símbolos de las acciones
    acciones = input("Ingrese los símbolos de las acciones separados por comas (por ejemplo, AAPL,GOOGL,MSFT,AMZN): ").split(',')

    # Fechas de inicio y fin
    start_date = '2023-01-23'
    end_date = '2024-01-23'

    # Comparar los RSI de las acciones y mostrar gráfico único
    comparar_rsi(acciones, start_date, end_date)
