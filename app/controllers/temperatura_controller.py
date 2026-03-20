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
list = [12,12,34,26,37,15]
# 🔹 SELECT
def obtener_datos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, valor FROM temperaturas")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    datos = [{"id": r[0], "valor": r[1]} for r in rows]
    def mostrar():
        for i in range(n):
            print(lis[i])
    def ordenar():
        n = len(list)
        for i in range(n-1):
            for j in range(i+1,n):
                if list [i] > list [j]:
                    aux = list [i]
                    list [i] = list [j]
                    list [j] = aux
        mostrar()
    return {"datos": datos, "lista": list}
