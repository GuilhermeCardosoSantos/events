# metrics.py
from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter("app_requests_total", "Total")
REQUEST_TIME = Histogram("app_request_duration_seconds", "Tempo")