# 📖 Vehicle Dynamics Model Explanation

## 📜 Physics Formulas Used
This document explains the physics behind the vehicle dynamics model used in this project.

### 1️⃣ Longitudinal Motion (Acceleration & Braking)
The net force acting on the vehicle is calculated as:
\[
F_{net} = F_{engine} - F_{drag} - F_{rolling resistance}
\]

The resulting acceleration is determined by Newton’s Second Law:
\[
 a = \frac{F_{net}}{m}
\]
where:
- \( F_{net} \) = Net force on the vehicle (N)
- \( F_{engine} \) = Engine force after drivetrain efficiency losses (N)
- \( F_{drag} \) = Aerodynamic drag force (N)
- \( F_{rolling resistance} \) = Rolling resistance force (N)
- \( m \) = Vehicle mass (kg)
- \( a \) = Acceleration (m/s²)

---

### 2️⃣ Aerodynamic Drag Force
Aerodynamic drag force is the resistance due to air acting against the vehicle’s motion:
\[
F_{drag} = \frac{1}{2} C_d A \rho v^2
\]
where:
- \( C_d \) = Drag coefficient (dimensionless)
- \( A \) = Frontal area of the vehicle (m²)
- \( \rho \) = Air density (kg/m³), typically 1.225 kg/m³ at sea level
- \( v \) = Vehicle speed (m/s)

---

### 3️⃣ Rolling Resistance Force
Rolling resistance is caused by the friction between the tires and the ground:
\[
F_{rolling} = C_r m g
\]
where:
- \( C_r \) = Rolling resistance coefficient (dimensionless, typically 0.01 - 0.03 for road tires)
- \( m \) = Vehicle mass (kg)
- \( g \) = Acceleration due to gravity (9.81 m/s²)

---

### 4️⃣ Braking Force
The maximum braking force is determined by the friction between the tires and the road:
\[
F_{brake} = \mu m g
\]
where:
- \( \mu \) = Tire-road friction coefficient (typically 0.7-1.0 for dry asphalt, lower for wet surfaces)
- \( m \) = Vehicle mass (kg)
- \( g \) = Gravity (9.81 m/s²)

---

### 5️⃣ Tire Grip & Slip Conditions
Tire grip and slip conditions define how the vehicle maintains control during acceleration, braking, and cornering.

#### **Simplified Friction Model**
A basic approach assumes that the maximum tire force is:
\[
F_{tire} = \mu F_{normal}
\]
where:
- \( \mu \) = Tire-road friction coefficient
- \( F_{normal} \) = Normal force on the tire

#### **Pacejka Tire Model (Optional Advanced Model)**
For a more detailed approach, the Pacejka "Magic Formula" is used to model tire behavior more accurately:
\[
F_y = D \sin(C \tan^{-1}(Bx - E(Bx - \tan^{-1}(Bx))))
\]
where:
- \( F_y \) = Lateral force
- \( B, C, D, E \) = Empirical constants based on tire characteristics
- \( x \) = Slip angle or slip ratio

These calculations are implemented in `tire_model.py` to simulate realistic tire behavior under various driving conditions.

---

## 🚗 Application in Vehicle Model
These equations are implemented in `vehicle_model.py` and `tire_model.py` to compute real-time forces acting on the vehicle under different conditions. The model considers:
- Engine force through drivetrain efficiency
- Air resistance and rolling friction at different speeds
- Braking force limits based on tire friction
- Tire grip and slip conditions during cornering

These calculations allow us to simulate **acceleration, braking distance, and cornering dynamics** for an SAE Baja/Formula-style vehicle.

🔧 **Next Steps:** Implement full simulation in `simulation.py` to test vehicle performance. 🚀
