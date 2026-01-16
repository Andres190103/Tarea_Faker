import csv
from faker import Faker

# Inicializamos Faker
fake = Faker()

def generar_dataset(cantidad=50):
    """
    Genera una lista de diccionarios con datos ficticios.
    """
    datos = []
    for _ in range(cantidad):
        registro = {
            "Nombre": fake.name(),
            "Correo": fake.email(),
            "Direccion": fake.address().replace("\n", ", "),
            "Perfil": fake.job(),
            "Fecha_Registro": fake.date_this_decade().strftime("%Y-%m-%d")
        }
        datos.append(registro)
    return datos

def exportar_a_csv(datos, nombre_archivo="usuarios_ficticios.csv"):
    """
    Exporta la lista de datos a un archivo CSV.
    """
    columnas = datos[0].keys()
    try:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(datos)
        print(f"✅ Éxito: Se han generado {len(datos)} registros en '{nombre_archivo}'.")
    except Exception as e:
        print(f"❌ Error al exportar: {e}")

if __name__ == "__main__":
    # Generar 50 registros
    lista_usuarios = generar_dataset(50)
    
    # Mostrar los primeros 5 en consola
    print("--- Vista previa de los datos generados ---")
    for u in lista_usuarios[:5]:
        print(u)
    
    # Exportar a CSV
    exportar_a_csv(lista_usuarios)