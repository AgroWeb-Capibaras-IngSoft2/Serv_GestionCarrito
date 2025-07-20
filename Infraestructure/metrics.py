from prometheus_client import Counter, Histogram

# Métricas globales
REQUEST_COUNT = Counter('carrito_requests_total', 'Total requests', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('carrito_request_duration_seconds', 'Request latency')
ERROR_COUNT = Counter('carrito_errors_total', 'Total_errors', ['endpoint'])
