import fastf1 as ff1
from fastf1 import plotting
import matplotlib.pyplot as plt


#Graphics configure
ff1.plotting.setup_mpl()

#Enable cache
ff1.Cache.enable_cache('cache')

#Charge race
race = ff1.get_session(2024, 'Azerbaijan Grand Prix', 'R')

#Get the laps
race.load(telemetry=True)

laps_r = race.laps

#Compare race-times per lap Piastri Leclerc

piastri = laps_r.pick_driver('PIA')

leclerc = laps_r.pick_driver('LEC')


plt.rcParams['figure.figsize'] = [10, 6]

fig, ax = plt.subplots()

fig.suptitle('Race telemetry compare between Piastri & Leclerc')

ax.plot(piastri['LapNumber'], piastri['LapTime'], label='PIA')
ax.plot(leclerc['LapNumber'], leclerc['LapTime'], label='LEC')
ax.set(ylabel='Time race', xlabel='Laps')
ax.legend(loc='upper center')

plt.show()


#Analyze the overtake lap Piastri-Leclerc

pia_overtake = piastri[piastri.LapNumber == 20]

lec_overtaken = leclerc[leclerc.LapNumber == 20]


print(f'Piastri time at lap 20 ', pia_overtake.LapTime)

print(f'Leclerc time at lap  20 ', lec_overtaken.LapTime)


pia_tel = pia_overtake.get_car_data().add_distance()

lec_tel = lec_overtaken.get_car_data().add_distance()


plt.rcParams['figure.figsize'] = [15, 15]

fig, ax = plt.subplots(3)

fig.suptitle('Telemetry overtake comparation')

ax[0].plot(pia_tel['Distance'], pia_tel['Speed'], label='PIA')
ax[0].plot(lec_tel['Distance'], lec_tel['Speed'], label='LEC')
ax[0].set_xlabel('Distance in m')
ax[0].set_ylabel('Speed in km/h')
ax[0].legend()

ax[1].plot(pia_tel['Distance'], pia_tel['Brake'], label='PIA')
ax[1].plot(lec_tel['Distance'], lec_tel['Brake'], label='LEC')
ax[1].set_xlabel('Distance in m')
ax[1].set_ylabel('Brake')

ax[2].plot(pia_tel['Distance'], pia_tel['Throttle'], label='PIA')
ax[2].plot(lec_tel['Distance'], lec_tel['Throttle'], label='LEC')
ax[2].set_xlabel('Distance in m')
ax[2].set_ylabel('Acceleration')

plt.suptitle('Piastri overtake Leclerc in lap 20 telemetry comparison')

plt.show()