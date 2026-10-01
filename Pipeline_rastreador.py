import json
import time

# Base de datos simulada que el agente extrae de portales como Glassdoor
ofertas_extraidas_sucias = [
    {"puesto": "Editor de Video Corto", "empresa": "Media Agency", "modalidad": "Remoto", "postulacion": "Candidatura rapida"},
    {"puesto": "Data Entry Junior", "empresa": "Tech Solutions", "modalidad": "Presencial", "postulacion": "Formulario externo largo"},
    {"puesto": "Soporte de Atencion al Cliente", "empresa": "E-commerce Global", "modalidad": "Remoto", "postulacion": "Candidatura rapida"},
    {"puesto": "Asistente de Carga de Datos", "empresa": "Logistica SRL", "modalidad": "Remoto", "postulacion": "Formulario externo largo"},
    {"puesto": "Creador de Contenido / Clipper", "empresa": "Streamer Pro", "modalidad": "Remoto", "postulacion": "Candidatura rapida"}
]

def agente_rastreador_filtro(ofertas):
    print("🕵️‍♂️ [Agente Rastreador] Iniciando análisis y filtrado masivo de ofertas...")
    time.sleep(1)
    
    ofertas_optimas = []
    
    for oferta in ofertas:
        # El criterio del CEO: Solo remoto y con postulación en 1 clic (Candidatura rápida)
        if oferta["modalidad"] == "Remoto" and oferta["postulacion"] == "Candidatura rapida":
            ofertas_optimas.append(oferta)
            print(f"✅ ¡Oferta Óptima Encontrada! -> {oferta['puesto']} en {oferta['empresa']}")
        else:
            print(f"❌ Oferta Descartada (No rentable en tiempo) -> {oferta['puesto']} ({oferta['modalidad']})")
            
    return ofertas_optimas

if __name__ == "__main__":
    print("==============================================================")
    print("🏢 SIMULACIÓN DE AGENTE DE EMPRESA DIGITAL")
    print("==============================================================")
    
    resultados_finales = agente_rastreador_filtro(ofertas_extraidas_sucias)
    
    print("\n📊 [Reporte Final para el Usuario]")
    print(f"Total de ofertas analizadas: {len(ofertas_extraidas_sucias)}")
    print(f"Total de enlaces listos para postulación manual rápida: {len(resultados_finales)}")
    print("==============================================================")
