"Make the 600 delivery orders. Same seed, same file, on every PC."
import csv
import numpy as np

rng = np.random.default_rng(42)
n = 600
distance_km = np.round(rng.uniform(0.5, 12.0, n), 2)
prep_time_min = np.round(rng.uniform(5, 30, n), 0)
traffic_level = rng.integers(1, 4, n)
rain = rng.binomial(1, 0.25, n)
delivery_min = np.round(6.0 + 3.1 * distance_km + 0.65 * prep_time_min
                        + 4.2 * traffic_level + 5.5 * rain
                        + rng.normal(0, 2.5, n), 1)

with open("data.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["distance_km", "prep_time_min", "traffic_level", "rain", "delivery_min"])
    for i in range(n):
        w.writerow([distance_km[i], int(prep_time_min[i]), int(traffic_level[i]),
                    int(rain[i]), delivery_min[i]])
print("wrote data.csv with", n, "orders")
