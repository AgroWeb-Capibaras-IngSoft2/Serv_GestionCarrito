# Servicio de Gestión de Carrito de Compras

Microservicio backend desarrollado en Flask para la gestión de carritos de compras, implementado con arquitectura limpia (Clean Architecture) y observabilidad con Prometheus.

## Características

- ✅ **Arquitectura Clean**: Separación clara entre capas de dominio, aplicación, adaptadores e infraestructura
- ✅ **Base de datos PostgreSQL**: Persistencia de carritos e ítems
- ✅ **Observabilidad**: Métricas con Prometheus (contadores, latencia, errores)
- ✅ **API REST**: Endpoints para gestión completa del carrito
- ✅ **Pool de conexiones**: Manejo eficiente de conexiones a la base de datos

## 1. Instrucciones de instalación

### Prerrequisitos
- Python 3.8+
- PostgreSQL
- Git

### Instalación

```bash
# Clona el repositorio
git clone https://github.com/AgroWeb-Capibaras-IngSoft2/GestionCarrito.git
cd GestionCarrito

# (Opcional) Crea y activa un entorno virtual
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate

# Instala las dependencias
pip install -r requirements.txt
```

### Configuración de base de datos

1. Crea un archivo `.env` en la raíz del proyecto:
```env
DATA_BASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_bd
```

2. Ejecuta las siguientes consultas SQL para crear las tablas:

```sql
-- Tabla carrito
CREATE TABLE IF NOT EXISTS carrito (
    id_carrito SERIAL,
    userDocument VARCHAR(15) NOT NULL,
    userDocumentType VARCHAR(4) NOT NULL,
    creationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(10,2) DEFAULT 0.00,
    PRIMARY KEY(id_carrito, userDocument, userDocumentType)
);

-- Tabla item_carrito
CREATE TABLE IF NOT EXISTS item_carrito (
    idItem SERIAL,
    id_carrito INTEGER NOT NULL,
    userDocument VARCHAR(15) NOT NULL,
    userDocumentType VARCHAR(4) NOT NULL,
    product_id INTEGER NOT NULL,
    product_name TEXT NOT NULL,
    cantidad INTEGER NOT NULL CHECK (cantidad > 0),
    medida TEXT NOT NULL,
    total_prod NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (idItem, id_carrito, userDocument, userDocumentType),
    FOREIGN KEY (id_carrito, userDocument, userDocumentType)
        REFERENCES carrito(id_carrito, userDocument, userDocumentType)
        ON DELETE CASCADE
);
```

## 2. Ejecución local

```bash
# Ejecuta la aplicación
python app.py
```

El servicio estará disponible en:
- **API**: `http://localhost:5003`
- **Métricas**: `http://localhost:5003/metrics`

## 3. Documentación de endpoints

### Gestión de Carrito

| Método | Endpoint                        | Descripción                        |
|--------|---------------------------------|------------------------------------|
| POST   | `/carrito/create`               | Crear un nuevo carrito             |
| POST   | `/carrito/addProduct`           | Añadir producto al carrito         |
| PUT    | `/carrito/changeQuantity`       | Cambiar cantidad de un producto    |
| DELETE | `/carrito/deleteProduct`        | Eliminar producto del carrito      |
| DELETE | `/carrito/vaciar`               | Vaciar el carrito completamente    |
| GET    | `/carrito/getCarrito/<id>`      | Obtener información del carrito    |
| GET    | `/carrito/total/<id_carrito>`   | Obtener el total del carrito       |

### Observabilidad

| Método | Endpoint    | Descripción                           |
|--------|-------------|---------------------------------------|
| GET    | `/metrics`  | Métricas Prometheus (observabilidad)  |

### Ejemplos de uso

#### Crear carrito
```http
POST /carrito/create
Content-Type: application/json

{
  "userDocument": "1234567890",
  "docType": "CC"
}
```

**Respuesta exitosa (200):**
```json
{
  "Success": true,
  "message": "Carrito creado exitosamente"
}
```

#### Añadir producto al carrito
```http
POST /carrito/addProduct
Content-Type: application/json

{
  "id_carrito": 1,
  "product_id": 123,
  "cantidad": 2
}
```

#### Obtener carrito
```http
GET /carrito/getCarrito/1
```

**Respuesta:**
```json
{
  "Success": true,
  "carrito": {
    "id_carrito": 1,
    "total": 25.50,
    "items": [
      {
        "product_id": 123,
        "product_name": "Producto ejemplo",
        "cantidad": 2,
        "medida": "KG",
        "total_prod": 25.50
      }
    ]
  }
}
```

#### Vaciar carrito
```http
DELETE /carrito/vaciar?id_carrito=1
```

## Observabilidad con Prometheus

El servicio incluye instrumentación básica con Prometheus que captura:

- **Contador de peticiones**: `carrito_requests_total`
- **Tiempos de respuesta**: `carrito_request_duration_seconds`
- **Errores por endpoint**: `carrito_errors_total`

Para ver las métricas en tiempo real, visita: `http://localhost:5003/metrics`

### Ejemplo de métricas:
```
# Peticiones totales
carrito_requests_total{endpoint="crear_carrito",method="POST"} 5.0

# Tiempo de respuesta promedio
carrito_request_duration_seconds_sum 1.34
carrito_request_duration_seconds_count 5.0

# Errores (códigos 4xx y 5xx)
carrito_errors_total{endpoint="crear_carrito"} 2.0
```

## Arquitectura

El proyecto sigue los principios de Clean Architecture:

```
GestionCarrito/
├── Domain/              # Entidades de dominio
├── Application/         # Casos de uso e interfaces
├── InterfaceAdapters/   # Implementaciones de interfaces
├── Infraestructure/     # Frameworks, DB, rutas
└── app.py              # Punto de entrada
```

## Tecnologías utilizadas

- **Flask**: Framework web
- **PostgreSQL**: Base de datos
- **psycopg2**: Conector de PostgreSQL
- **Prometheus**: Observabilidad y métricas
- **Flask-CORS**: Manejo de CORS

## Contribución

Este proyecto es parte del curso de Ingeniería de Software II de la Universidad Nacional de Colombia.

---

**Desarrollado por:** AgroWeb-Capibaras-IngSoft2
