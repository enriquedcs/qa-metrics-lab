# scripts/defect_density.py

import csv
import sys
from pathlib import Path

def cargar_historias_desde_csv(csv_path):
    """Lee historias de usuario desde un CSV exportado de Jira"""
    user_stories = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                issue_key = row['Issue Key'].strip()
                user_stories[issue_key] = {
                    "story_points": int(row['Story Points']),
                    "bugs": int(row['Bug Count']),
                    "component": row['Component'].strip(),
                }
        
        if not user_stories:
            raise ValueError("El CSV está vacío o no tiene datos válidos")
        
        return user_stories
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Campo faltante en el CSV: {e}")
        print("Campos requeridos: Issue Key, Story Points, Bug Count, Component")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def analizar_calidad_sprint(stories):
    print(f"{'--- Análisis de Densidad de Defectos ---':^50}")
    print(f"{'ID':<10} | {'Puntos':<8} | {'Bugs':<6} | {'Densidad':<10} | {'Estado'}")
    print("-" * 60)

    for id, data in stories.items():
        # Cálculo de densidad (Bugs / Puntos)
        densidad = data["bugs"] / data["story_points"]
        
        # Lógica de diagnóstico de Senior QA
        if densidad > 0.7:
            status = "🔴 CRÍTICO (Refactorizar)"
        elif densidad > 0.4:
            status = "🟡 RIESGOSO (Revisar DoD)"
        else:
            status = "🟢 ESTABLE"
            
        print(f"{id:<10} | {data['story_points']:<8} | {data['bugs']:<6} | {densidad:<10.2f} | {status}")

if __name__ == "__main__":
    # Obtener ruta del CSV desde argumentos o usar default
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "../data/jira_exports/user_stories.csv"
    
    print(f"📊 Cargando historias desde: {csv_file}\n")
    user_stories = cargar_historias_desde_csv(csv_file)
    analizar_calidad_sprint(user_stories)