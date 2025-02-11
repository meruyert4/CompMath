import numpy as np
import matplotlib.pyplot as plt

beta = 0.0003  # Infection rate
gamma = 0.1  # Recovery rate
h = 0.1  # Step size (0.1 day)
days = 100

# Initial conditions (in fractions of 1 million)
S0 = 999000 / 1e6
I0 = 1000 / 1e6
R0 = 0 / 1e6

N = S0 + I0 + R0

def dS_dt(S, I):
    return -beta * S * I


def dI_dt(S, I):
    return beta * S * I - gamma * I


def dR_dt(I):
    return gamma * I


# runge kutta 4th method
def runge_kutta(S0, I0, R0, h, days):
    steps = int(days / h)
    S, I, R = np.zeros(steps), np.zeros(steps), np.zeros(steps)
    S[0], I[0], R[0] = S0, I0, R0

    for t in range(1, steps):
        k1_S, k1_I, k1_R = dS_dt(S[t - 1], I[t - 1]), dI_dt(S[t - 1], I[t - 1]), dR_dt(I[t - 1])
        k2_S, k2_I, k2_R = dS_dt(S[t - 1] + h / 2 * k1_S, I[t - 1] + h / 2 * k1_I), dI_dt(S[t - 1] + h / 2 * k1_S, I[
            t - 1] + h / 2 * k1_I), dR_dt(I[t - 1] + h / 2 * k1_R)
        k3_S, k3_I, k3_R = dS_dt(S[t - 1] + h / 2 * k2_S, I[t - 1] + h / 2 * k2_I), dI_dt(S[t - 1] + h / 2 * k2_S, I[
            t - 1] + h / 2 * k2_I), dR_dt(I[t - 1] + h / 2 * k2_R)
        k4_S, k4_I, k4_R = dS_dt(S[t - 1] + h * k3_S, I[t - 1] + h * k3_I), dI_dt(S[t - 1] + h * k3_S,
                                                                                  I[t - 1] + h * k3_I), dR_dt(I[t - 1] + h * k3_R)

        S[t] = S[t - 1] + (h / 6) * (k1_S + 2 * k2_S + 2 * k3_S + k4_S)
        I[t] = I[t - 1] + (h / 6) * (k1_I + 2 * k2_I + 2 * k3_I + k4_I)
        R[t] = R[t - 1] + (h / 6) * (k1_R + 2 * k2_R + 2 * k3_R + k4_R)

        if t % 10 == 0:
            print(f"Day {t * h:.1f}: S = {S[t]:.6f}, I = {I[t]:.6f}, R = {R[t]:.6f}")

    return S * 1e6, I * 1e6, R * 1e6, np.arange(0, days, h)


print("Original scenario")
S, I, R, time = runge_kutta(S0, I0, R0, h, days)

# Plot original scenario
plt.figure(figsize=(12, 6))
plt.plot(time, S, label='Susceptible')
plt.plot(time, I, label='Infected')
plt.plot(time, R, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Original Scenario - SIR Model')
plt.legend()
plt.grid(True)
plt.show()

# Vaccination campaign: Reduce initial susceptible population by 50%
print("\nVaccination campaign: Reduce initial susceptible population by 50%")
S_vaccine, I_vaccine, R_vaccine, _ = runge_kutta(S0 * 0.5, I0, R0, h, days)
plt.figure(figsize=(12, 6))
plt.plot(time, S_vaccine, label='Susceptible (Vaccination)')
plt.plot(time, I_vaccine, label='Infected (Vaccination)')
plt.plot(time, R_vaccine, label='Recovered (Vaccination)')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Vaccination Campaign - SIR Model')
plt.legend()
plt.grid(True)
plt.show()

print("\nSocial distancing")
beta *= 0.5  # New infection rate for social distancing
S_social, I_social, R_social, _ = runge_kutta(S0, I0, R0, h, days)
plt.figure(figsize=(12, 6))
plt.plot(time, S_social, label='Susceptible (Social Distancing)')
plt.plot(time, I_social, label='Infected (Social Distancing)')
plt.plot(time, R_social, label='Recovered (Social Distancing)')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Social Distancing')
plt.legend()
plt.grid(True)
plt.show()

# Original Scenario
peak_infected = max(I)
peak_day = time[np.argmax(I)]
total_infected = (S0 * 1e6 - S[-1]) + (R[-1] - R0 )
print(f"Original Scenario:\n  Peak Infected: {int(peak_infected)} on day {peak_day:.1f}")
print(f"  Total Infected: {int(total_infected)}")

# Vaccination Scenario
peak_infected_vaccine = max(I_vaccine)
peak_day_vaccine = time[np.argmax(I_vaccine)]
total_infected_vaccine = (S0 * 0.5 * 1e6 - S_vaccine[-1]) + (R_vaccine[-1] - R0 )
print(f"\nVaccination Scenario:\n  Peak Infected: {int(peak_infected_vaccine)} on day {peak_day_vaccine:.1f}")
print(f"  Total Infected: {int(total_infected_vaccine)}")

# Social Distancing Scenario
peak_infected_social = max(I_social)
peak_day_social = time[np.argmax(I_social)]
total_infected_social = (S0 * 1e6 - S_social[-1]) + (R_social[-1] - R0)
print(f"\nSocial Distancing Scenario:\n  Peak Infected: {int(peak_infected_social)} on day {peak_day_social:.1f}")
print(f"  Total Infected: {int(total_infected_social)}")


