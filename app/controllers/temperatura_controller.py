from app.database import get_connection

# 🔹 INSERT
def guardar_temperatura(valor: float):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO temperaturas (valor) VALUES (%s)",
        (valor,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"mensaje": "Guardado en DB", "valor": valor}
# 🔹 SELECT
def obtener_datos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, valor FROM temperaturas")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    datos = [{"id": r[0], "valor": r[1]} for r in rows]
    edades= [12,48,23,15,17]
    def ordenar():
        n = len(edades)
        for i in range(n-1):
            for j in range(i+1,n):
                if edades [i] > edades [j]:
                    aux = edades [i]
                    edades [i] = edades [j]
                    edades [j] = aux
    
    return {"datos": datos, "lista ordenada": suma, "Longitud:": n}
