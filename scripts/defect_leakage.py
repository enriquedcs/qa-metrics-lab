# scripts/defect_leakage.py

import csv
import sys
from pathlib import Path

def cargar_defectos_desde_csv(csv_path):
    """Lee defectos de QA vs Producción desde un CSV"""
    defectos = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                issue_key = row['Issue Key'].strip()
                defectos[issue_key] = {
                    "defectos_qa": int(row['Defects QA']),
                    "defectos_prod": int(row['Defects Production']),
                    "componente": row['Component'].strip(),
                }
        
        if not defectos:
            raise ValueError("El CSV está vacío o no tiene datos válidos")
        
        return defectos
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Campo faltante en el CSV: {e}")
        print("Campos requeridos: Issue Key, Defects QA, Defects Production, Component")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def analizar_defect_leakage(defectos):
    """Calcula la tasa de fuga de defectos (Leakage Rate)"""
    print(f"{'--- Análisis de Defect Leakage ---':^60}")
    print(f"{'ID':<10} | {'QA':<6} | {'Prod':<6} | {'Total':<6} | {'Leakage %':<12} | {'Estado'}")
    print("-" * 75)
    
    total_qa = 0
    total_prod = 0
    
    for id, data in defectos.items():
        qa = data["defectos_qa"]
        prod = data["defectos_prod"]
        total = qa + prod
        
        # Leakage Rate = (Defectos en Prod / Total de Defectos) * 100
        if total > 0:
            leakage_rate = (prod / total) * 100
        else:
            leakage_rate = 0
        
        # Clasificación
        if leakage_rate > 20:
            status = "🔴 CRÍTICO (Mejorar QA)"
        elif leakage_rate > 10:
            status = "🟡 ALTO (Revisar proceso)"
        else:
            status = "🟢 ACEPTABLE"
        
        print(f"{id:<10} | {qa:<6} | {prod:<6} | {total:<6} | {leakage_rate:<12.1f} | {status}")
        
        total_qa += qa
        total_prod += prod
    
    print("-" * 75)
    if total_qa + total_prod > 0:
        overall_leakage = (total_prod / (total_qa + total_prod)) * 100
    else:
        overall_leakage = 0
    
    print(f"{'TOTAL':<10} | {total_qa:<6} | {total_prod:<6} | {total_qa + total_prod:<6} | {overall_leakage:<12.1f} |")

if __name__ == "__main__":
    # Obtener ruta del CSV desde argumentos o usar default
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "../data/jira_exports/defect_leakage.csv"
    
    print(f"📊 Cargando defectos desde: {csv_file}\n")
    defectos = cargar_defectos_desde_csv(csv_file)
    analizar_defect_leakage(defectos)
