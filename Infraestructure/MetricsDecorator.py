import time
from functools import wraps
from flask import request
from Infraestructure.metrics import REQUEST_COUNT, REQUEST_LATENCY, ERROR_COUNT

def monitor_endpoint(endpoint_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            # 1. Medir tiempo de inicio
            start_time = time.time()

            # 2. Contar la petición
            REQUEST_COUNT.labels(method=request.method, endpoint=endpoint_name).inc()

            try:
                # 3. Ejecutar la función
                response = func(*args, **kwargs)

                # 4. Medir tiempo total
                REQUEST_LATENCY.observe(time.time() - start_time)

                # 5. Verificar si hay errores HTTP (4xx, 5xx)
                # response puede ser una tupla (data, status_code) o solo data
                status_code = 200  # Por defecto
                if isinstance(response, tuple) and len(response) >= 2:
                    status_code = response[1]

                # Contar errores HTTP (4xx y 5xx)
                if status_code >= 400:
                    ERROR_COUNT.labels(endpoint=endpoint_name).inc()

                return response
            except Exception as e:
                # 5. Contar errores de excepción
                ERROR_COUNT.labels(endpoint=endpoint_name).inc()
                # Medir tiempo aunque haya error
                REQUEST_LATENCY.observe(time.time() - start_time)
                raise e  # Re-lanzar la excepción
        return wrapper
    return decorator