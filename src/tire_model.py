import numpy as np

def simple_friction_model(normal_force, friction_coefficient):
    """Calculates maximum lateral force using a basic friction model."""
    return friction_coefficient * normal_force

class TireModel:
    def __init__(self, friction_coefficient=1.0):
        self.mu = friction_coefficient  # Coefficient of friction

    def lateral_force(self, normal_force):
        """Calculates lateral force using a simplified tire friction model."""
        return self.mu * normal_force
    
    def longitudinal_force(self, normal_force):
        """Calculates longitudinal force (traction or braking) using friction."""
        return self.mu * normal_force
