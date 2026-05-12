# scripts/test_coverage.py

import csv
import sys
from pathlib import Path

def cargar_cobertura_desde_csv(csv_path):
    """Lee datos de cobertura de pruebas desde un CSV"""
    cobertura = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                componente = row['Component'].strip()
                cobertura[componente] = {
                    "lineas_codigo": int(row['Lines of Code']),
                    "lineas_cubiertas": int(row['Lines Covered']),
                    "pruebas": int(row['Tests']),
                }
        
        if not cobertura:
            raise ValueError("El CSV está vacío o no tiene datos válidos")
        
        return cobertura
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_path}")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Campo faltante en el CSV: {e}")
        print("Campos requeridos: Component, Lines of Code, Lines Covered, Tests")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def analizar_test_coverage(cobertura):
    """Calcula y analiza la cobertura de pruebas"""
    print(f"{'--- Análisis de Test Coverage ---':^75}")
    print(f"{'Componente':<20} | {'LoC':<8} | {'Cubierto':<10} | {'Coverage %':<12} | {'Pruebas':<8} | {'Estado'}")
    print("-" * 90)
    
    total_loc = 0
    total_covered = 0
    total_tests = 0
    
    for componente, data in cobertura.items():
        loc = data["lineas_codigo"]
        covered = data["lineas_cubiertas"]
        tests = data["pruebas"]
        
        # Coverage % = (Líneas Cubiertas / Total Líneas) * 100
        if loc > 0:
            coverage_pct = (covered / loc) * 100
        else:
            coverage_pct = 0
        
        # Clasificación
        if coverage_pct >= 80:
            status = "🟢 EXCELENTE"
        elif coverage_pct >= 70:
            status = "🟡 BUENO"
        elif coverage_pct >= 50:
            status = "🟠 REGULAR"
        else:
            status = "🔴 INSUFICIENTE"
        
        print(f"{componente:<20} | {loc:<8} | {covered:<10} | {coverage_pct:<12.1f} | {tests:<8} | {status}")
        
        total_loc += loc
        total_covered += covered
        total_tests += tests
    
    print("-" * 90)
    if total_loc > 0:
        overall_coverage = (total_covered / total_loc) * 100
    else:
        overall_coverage = 0
    
    overall_status = "🟢 EXCELENTE" if overall_coverage >= 80 else "🟡 BUENO" if overall_coverage >= 70 else "🟠 REGULAR" if overall_coverage >= 50 else "🔴 INSUFICIENTE"
    
    print(f"{'TOTAL':<20} | {total_loc:<8} | {total_covered:<10} | {overall_coverage:<12.1f} | {total_tests:<8} | {overall_status}")

if __name__ == "__main__":
    # Obtener ruta del CSV desde argumentos o usar default
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    else:
        csv_file = "../data/jira_exports/test_coverage.csv"
    
    print(f"📊 Cargando cobertura desde: {csv_file}\n")
    cobertura = cargar_cobertura_desde_csv(csv_file)
    analizar_test_coverage(cobertura)
