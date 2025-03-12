import numpy as np
import matplotlib.pyplot as plt

# Example: RC Circuit Step Response
R = 10e3  # 10kΩ
C = 1e-6  # 1µF
tau = R * C

t = np.linspace(0, 5 * tau, 1000)
V_in = 1  # Step input voltage
V_out = V_in * (1 - np.exp(-t / tau))

# Save plot
plt.plot(t * 1e3, V_out)
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (V)")
plt.title("RC Circuit Step Response")
plt.grid()
plt.savefig("simulation_results.png")
print("Simulation complete. Results saved.")
