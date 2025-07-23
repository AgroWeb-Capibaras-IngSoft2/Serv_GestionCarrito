
# Changelog

## [2.1.1] - 2025-07-23
### Changed
- Se eliminó la caché del repositorio para evitar archivos temporales innecesarios.
- Se corrigió el archivo `.gitignore` para asegurar que los archivos de caché y temporales no sean versionados.

## [2.1.0] - 2025-07-23
### Added
- Endpoints adicionales para gestión de carritos y productos:
  - Añadir producto al carrito
  - Cambiar cantidad de producto
  - Vaciar carrito
  - Eliminar producto del carrito
  - Calcular total del carrito
  - Obtener carrito por usuario
- Documentación Swagger para todos los endpoints principales
- Comandos SQL correctos y ejemplos en el README

### Changed
- Se actualiza la forma de establecer la conexión con la base de datos para mayor robustez
- Mejoras en los mensajes y códigos de respuesta HTTP
- Centralización y mejora de la estructura del README

### Fixed
- Corrección de bugs en la gestión de carritos y productos
- Ajuste para enviar productId como varchar en vez de int
- Corrección de errores en la integración con el servicio de productos

### Documentation
- Se añade y actualiza el README del proyecto
- Se añade y actualiza la documentación Swagger

---

## [2.0.0] - 2025-07-14
### Added
- Estructura modular por servicios (subdirectorios para cada microservicio)
- Soporte multi-servicio: preparado para Productos, Usuarios y servicios futuros
- Configuración centralizada: pytest.ini y conftest.py globales con marcadores específicos por servicio
- Utilidades compartidas entre servicios
- Documentación unificada y sistema de reportes para múltiples servicios
- Variables de entorno para configuración flexible

### Changed
- Migración de estructura plana a organización por servicios

### Fixed
- Resueltos conflictos de imports entre utilidades de diferentes servicios
- Corregidos problemas de rutas relativas
- Separadas configuraciones específicas por servicio

---

## [1.0.0] - 2025-07-12
### Added
- Suite completa de pruebas de integración para el servicio de productos
- Pruebas de API REST, ciclo de vida, manejo de errores y rendimiento
- Generación de reportes PDF y métricas de observabilidad
- Configuración Cassandra y datos de prueba realistas
