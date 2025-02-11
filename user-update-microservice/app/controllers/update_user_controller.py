from app.services.db_service import get_db_connection
import datetime

def update_user(user_id: int, username: str = None, email: str = None, password: str = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Construcción dinámica de la consulta SQL para actualizar solo los campos proporcionados
    update_fields = []
    params = []

    if username:
        update_fields.append("\"username\" = %s")  # Corrección de nombres de columna
        params.append(username)

    if email:
        update_fields.append("\"email\" = %s")  # Corrección de nombres de columna
        params.append(email)

    if password:
        update_fields.append("\"password\" = %s")  # Corrección de nombres de columna
        params.append(password)

    if not update_fields:
        return {"error": "No se enviaron campos válidos para actualizar"}

    # Agregar updatedAt para registrar la actualización con comillas dobles
    update_fields.append("\"updatedAt\" = %s")
    params.append(datetime.datetime.utcnow())

    # Agregar el ID del usuario como parámetro final
    params.append(user_id)

    query = f'UPDATE "Users" SET {", ".join(update_fields)} WHERE "id" = %s RETURNING "id", "username", "email", "updatedAt";'

    try:
        cursor.execute(query, params)
        updated_user = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        if updated_user:
            return {"message": "Usuario actualizado con éxito", "user": updated_user}
        else:
            return {"error": "Usuario no encontrado"}

    except Exception as e:
        conn.rollback()
        return {"error": f"Error en la actualización: {str(e)}"}
