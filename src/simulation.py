import numpy as np
import matplotlib.pyplot as plt
from vehicle_model import VehicleModel
from tire_model import TireModel

# Define vehicle parameters
vehicle = VehicleModel(
    mass=300,  # kg
    drag_coefficient=0.3,
    frontal_area=1.2,  # m^2
    rolling_resistance=0.015,
    drivetrain_efficiency=0.9,
    tire_friction=0.8
)

tire = TireModel(friction_coefficient=0.9)

# Simulation parameters
time_step = 0.1  # seconds
total_time = 10  # seconds
engine_force = 1000  # N, constant engine force

def simulate_acceleration():
    """Simulates acceleration from 0 to 60 mph considering aerodynamic drag and rolling resistance."""
    velocity = 0  # Initial velocity (m/s)
    time_series = []
    velocity_series = []
    acceleration_series = []
    
    for t in np.arange(0, total_time, time_step):
        acceleration = vehicle.acceleration(engine_force, velocity)
        velocity += acceleration * time_step
        
        # Reduce engine force effect as speed increases (simulating drag and efficiency loss)
        engine_force_adjusted = engine_force * (1 - (velocity / 100))  # Decreasing force at higher speeds
        acceleration = vehicle.acceleration(engine_force_adjusted, velocity)
        
        time_series.append(t)
        velocity_series.append(velocity)
        acceleration_series.append(acceleration)
        
        if velocity * 2.237 >= 60:  # Convert m/s to mph
            print(f"0-60 mph achieved in {t:.2f} seconds")
            break
    
    return time_series, velocity_series, acceleration_series

def simulate_braking():
    """Simulates braking from 60 to 0 mph."""
    velocity = 60 / 2.237  # Convert mph to m/s
    time_series = []
    velocity_series = []
    acceleration_series = []
    deceleration = vehicle.braking_deceleration()
    
    for t in np.arange(0, total_time, time_step):
        velocity -= deceleration * time_step
        
        time_series.append(t)
        velocity_series.append(max(velocity, 0))  # Ensure velocity doesn't go negative
        acceleration_series.append(-deceleration)
        
        if velocity <= 0:
            print(f"60-0 mph braking completed in {t:.2f} seconds")
            break
    
    return time_series, velocity_series, acceleration_series

def plot_results(accel_data, brake_data):
    """Plots velocity and acceleration over time."""
    accel_time, accel_velocity, accel_acceleration = accel_data
    brake_time, brake_velocity, brake_acceleration = brake_data
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(2, 1, 1)
    plt.plot(accel_time, accel_velocity, label='Acceleration Phase')
    plt.plot([t + accel_time[-1] for t in brake_time], brake_velocity, label='Braking Phase')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(accel_time, accel_acceleration, label='Acceleration (m/s²)', color='r')
    plt.plot([t + accel_time[-1] for t in brake_time], brake_acceleration, label='Braking (m/s²)', color='b')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Run simulations
accel_data = simulate_acceleration()
brake_data = simulate_braking()
plot_results(accel_data, brake_data)
