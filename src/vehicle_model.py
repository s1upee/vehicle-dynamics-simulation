import numpy as np

class VehicleModel:
    def __init__(self, mass, drag_coefficient, frontal_area, rolling_resistance, drivetrain_efficiency, tire_friction):
        self.mass = mass  # kg
        self.Cd = drag_coefficient  # Drag coefficient
        self.A = frontal_area  # m^2
        self.Cr = rolling_resistance  # Rolling resistance coefficient
        self.drivetrain_efficiency = drivetrain_efficiency  # Efficiency of power transfer
        self.mu = tire_friction  # Tire-road friction coefficient
        self.g = 9.81  # Gravity (m/s^2)
        self.rho_air = 1.225  # Air density (kg/m^3)
    
    def aerodynamic_drag(self, velocity):
        """Calculates aerodynamic drag force."""
        return 0.5 * self.Cd * self.A * self.rho_air * velocity**2
    
    def rolling_resistance_force(self):
        """Calculates rolling resistance force."""
        return self.Cr * self.mass * self.g
    
    def braking_force(self):
        """Calculates maximum braking force."""
        return self.mu * self.mass * self.g
    
    def acceleration_force(self, engine_force, velocity):
        """Calculates net force on vehicle considering resistive forces."""
        drag = self.aerodynamic_drag(velocity)
        rolling = self.rolling_resistance_force()
        net_force = (engine_force * self.drivetrain_efficiency) - drag - rolling
        return max(net_force, 0)  # Prevent negative acceleration force
    
    def acceleration(self, engine_force, velocity):
        """Calculates acceleration based on net force."""
        net_force = self.acceleration_force(engine_force, velocity)
        return net_force / self.mass  # F = ma
    
    def braking_deceleration(self):
        """Calculates maximum braking deceleration."""
        return self.braking_force() / self.mass
