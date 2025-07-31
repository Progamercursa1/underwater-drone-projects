import time
import matplotlib.pyplot as plt

# Миссия
mission_name = "Mission 01 – Simulated Lake Study"
date = "2025-07-30"
location = "Simulated Lake Alpha"

# Симулированные данные
time_steps = [0, 10, 20, 30, 40]  # секунды
depths = [0.0, 1.2, 2.3, 3.1, 4.0]  # метры
temps = [22.1, 21.9, 21.4, 20.8, 20.0]  # градусы Цельсия
turbidity = [12, 14, 17, 20, 22]  # мутность в %

# Для визуализации
recorded_time = []
recorded_temp = []
recorded_turbidity = []

print(f"\n{mission_name}")
print(f"Date: {date}")
print(f"Location: {location}")
print("Objective: Explore the lake bottom and collect basic environmental parameters")
print("-------------------------------------------------------------\n")

plt.ion() 

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

for i in range(len(time_steps)):
    print(f"Time: {time_steps[i]}s")
    print(f"→ Depth: {depths[i]} m")
    print(f"→ Temperature: {temps[i]} °C")
    print(f"→ Turbidity: {turbidity[i]} %")
    print("-------------------------------------------------------------")

    recorded_time.append(time_steps[i])
    recorded_temp.append(temps[i])
    recorded_turbidity.append(turbidity[i])

    ax1.clear()
    ax2.clear()

    ax1.plot(recorded_time, recorded_temp, marker='o', color='blue')
    ax1.set_title("Water Temperature over Time")
    ax1.set_xlabel("Time (s)")
    ax1.set_ylabel("Temp (°C)")
    ax1.grid(True)

    ax2.plot(recorded_time, recorded_turbidity, marker='o', color='green')
    ax2.set_title("Turbidity over Time")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Turbidity (%)")
    ax2.grid(True)

    plt.tight_layout()
    plt.pause(1)

plt.ioff()
plt.show()
