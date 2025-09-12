import re
import pandas as pd

archivo = "facturacion.lst"

registros = []
headers = ["Numero", "NroFactura", "Fecha", "NroDeposito", "Cedula", "Nombre", "CodPago", 
           "Monto_100", "PorcBeca", "DesctoBeca", "Colegiatura_Beca", "MontoCobrado", "Detalle"]

with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        # Ignorar cabeceras, separadores y lineas vacías
        if not linea or linea.startswith("-") or "NUMERO" in linea or "Tipo-Talon" in linea:
            continue
        
        # Solo filas que empiezan con número (ej: "1 17351 ...")
        if re.match(r"^\d+", linea):
            # Separar por 2+ espacios
            partes = re.split(r"\s{2,}", linea)
            
            # Ajustar a 13 columnas (en caso de que falte algo)
            if len(partes) >= 13:
                numero       = partes[0].split()[0]         # "1"
                nro_factura  = partes[0].split()[1]         # "17351"
                fecha        = partes[1]                    # "01/09/2025"
                nro_deposito = partes[2]                    # "31ATC-875"
                cedula       = partes[3]                    # "7759024"
                nombre       = partes[4]                    # "VARGAS TORRICO AYELEN DEYANIRA"
                cod_pago     = partes[5]                    # "1262-2DA.CUOTA"
                monto100     = partes[6]
                porc_beca    = partes[7] if "%" in partes[7] or partes[7].replace(".","",1).isdigit() else ""
                descto_beca  = partes[8] if porc_beca else ""
                colegiatura  = partes[-3]
                monto_cob    = partes[-2]
                detalle      = partes[-1]
                
                registros.append([numero, nro_factura, fecha, nro_deposito, cedula, nombre, cod_pago, 
                                  monto100, porc_beca, descto_beca, colegiatura, monto_cob, detalle])

# Crear DataFrame
df = pd.DataFrame(registros, columns=headers)

# Exportar
df.to_csv("facturacion.csv", index=False, encoding="utf-8")

print("✅ Archivo 'facturacion.csv' creado con", len(df), "registros")
print(df.head())
