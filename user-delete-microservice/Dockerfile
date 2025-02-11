# Imagen base
FROM python:3.9

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto
EXPOSE 4000

# Comando de ejecución
CMD ["python", "main.py"]
