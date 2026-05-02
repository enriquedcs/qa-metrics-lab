# scripts/defect_density.py

# Definimos nuestras historias de usuario como diccionarios
user_stories = {
    "US-101": {"story_points": 5, "bugs": 2, "component": "PolicyCenter"},
    "US-102": {"story_points": 8, "bugs": 1, "component": "BillingCenter"},
    "US-103": {"story_points": 3, "bugs": 4, "component": "DataModel"},
}

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
    analizar_calidad_sprint(user_stories)