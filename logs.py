import os
from collections import Counter
from datetime import datetime

# Palabras a buscar
CLAVES = ["ERROR", "WARNING", "Timeout"]

def buscar_logs(directorio):
    return [f for f in os.listdir(directorio) if f.endswith(".log")]

def analizar_log(ruta_carpeta):
    conteo = Counter()
    eventos_relev = []

    logs = buscar_logs(ruta_carpeta)
    print(f"Archivos encontrados: {logs}")

    for log in logs:
        ruta = os.path.join(ruta_carpeta, log)
        with open(ruta, "r", encoding="utf-8", errors="ignore") as archivo:
            for line in archivo:
                for clave in CLAVES:
                    if clave.lower() in line.lower():
                        conteo[clave] += 1
                        eventos_relev.append(f"[{datetime.now().strftime('%Y-%m-%d')}] {log}: {line.strip()}")
                        break

    return conteo, eventos_relev

def guardar_results(eventos, carpeta_salida=""):
    os.makedirs(carpeta_salida, exist_ok=True)
    fecha = datetime.now().strftime("%d-%m-%Y")
    nombre_archivo = f"logs_filters_{fecha}.txt"
    ruta_salida = os.path.join(carpeta_salida, nombre_archivo)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(f"Analisis ejecutado: {datetime.now()}\n")
        f.write("="*40 + "\n")
        for line in eventos:
            f.write(line + "\n")

if __name__ == "__main__":
    carpeta_logs = "C:\\Windows\\System32\\winevt\\Logs"

    conteo, eventos = analizar_log(carpeta_logs)
    guardar_results(eventos)

    print("Resumen de eventos encontrados:")
    for clave, cant in conteo.items():
        print(f" - {clave}: {cant}")

