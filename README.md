# **Microservicio Factorial**

## **Descripcion**
Este microservicio recibe un numero entero por la URL y devuelve una respuesta en formato **JSON** con:

- El numero recibido  
- Su factorial  
- Una etiqueta `"par"` o `"impar"` segun el resultado del factorial  

### **Ejemplo de uso**
```
GET http://127.0.0.1:8000/factorial/5
```

**Respuesta:**
```json
{
  "number": 5,
  "factorial": 120,
  "etiqueta": "par"
}
```

---

## **Tecnologias usadas**
- Python 3.10  
- Flask  
- Docker  

---

## **Instalacion y ejecucion local**

### Clonar el repositorio
```bash
git clone https://github.com/JuanmaFl/Parcial02_JuanManuelFlorez.git
cd Parcial02_JuanManuelFlorez
```


### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar el microservicio
```bash
python app.py
```

### Probar en el navegador 
```
http://127.0.0.1:8000/factorial/3
```
o en terminal:
```bash
curl http://127.0.0.1:8000/factorial/3
```

---

## **Ejecucion con Docker (opcional)**

### Construir la imagen
```bash
docker build -t microservicio-factorial .
```

### Ejecutar el contenedor
```bash
docker run -p 8000:8000 microservicio-factorial
```

### Probar
```
http://127.0.0.1:8000/factorial/4
```

---


---

## **Pregunta de análisis**

Si el microservicio tuviera que comunicarse con otro servicio que almacena el historial de calculos en una base de datos externa, modificaria el diseño de la siguiente manera:

- **Separacion de responsabilidades:**  
  Crearia **dos microservicios independientes**:
  1. **Service A (Factorial):** Calcula el factorial y genera la respuesta JSON.  
  2. **Service B (Historial):** Recibe y guarda los datos en la base de datos.  

- **Comunicacion entre servicios:**  
  El microservicio de factorial enviaria una **peticion HTTP (POST)** al servicio de historial despues de realizar el calculo, enviando los datos del numero, factorial y etiqueta.  
  Esto lo podria implementar usando la libreria `requests`.

- **Ventajas del diseño:**  
  - Se mantiene un **acoplamiento débil**, permitiendo modificar o escalar los servicios de forma independiente.  
  - Permite **persistir y consultar** el historial sin afectar el rendimiento del servicio principal.  
  - Mejora la **escalabilidad y mantenimiento** del sistema.

