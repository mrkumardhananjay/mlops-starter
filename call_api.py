"Send three requests to the delivery service and print exactly what comes back."
import sys
import httpx

port = sys.argv[1] if len(sys.argv) > 1 else "8000"
base = f"http://127.0.0.1:{port}"
order = {"distance_km": 5.0, "prep_time_min": 20, "traffic_level": 2, "rain": 0}

try:
    r = httpx.get(f"{base}/health")
    print("GET  /health          ->", r.status_code, r.text)
    r = httpx.post(f"{base}/predict", json=order)
    print("POST /predict (good)  ->", r.status_code, r.text)
    r = httpx.post(f"{base}/predict", json={**order, "traffic_level": 9})
    print("POST /predict (bad)   ->", r.status_code, r.text)
except httpx.TransportError as problem:
    print(f"No answer on port {port}: {problem}")
    print("Is the service running? If it was just started, wait 10 seconds and try again.")
