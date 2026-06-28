import time

class HydraulicBrakeSystem:
    def __init__(self, master_cyl_area, slave_cyl_area, vehicle_mass, friction_coefficient):
        # Areas can be in cm^2, force in Newtons
        self.master_cyl_area = master_cyl_area 
        self.slave_cyl_area = slave_cyl_area   
        self.vehicle_mass = vehicle_mass       # in kilograms
        self.friction_coefficient = friction_coefficient
        self.vehicle_speed = 0                 # meters per second

    def apply_brakes(self, pedal_force):
        # 1. Pascal's Law: Pressure = Force / Area
        pressure = pedal_force / self.master_cyl_area

        # 2. Force exerted by slave cylinder (clamping force on the rotor)
        # Because slave area > master area, force is multiplied!
        slave_force = pressure * self.slave_cyl_area

        # 3. Calculate friction force between brake pads and rotor
        friction_force = slave_force * self.friction_coefficient

        # 4. Calculate deceleration (Newton's Second Law: a = F/m)
        deceleration = friction_force / self.vehicle_mass
        
        return pressure, slave_force, deceleration

    def simulate(self, initial_speed, pedal_forces, dt=1.0):
        """Simulates braking over discrete time steps (dt)."""
        self.vehicle_speed = initial_speed
        print(f"--- Simulation Started ---")
        print(f"Initial Vehicle Speed: {self.vehicle_speed:.2f} m/s\n")

        for step, force in enumerate(pedal_forces):
            if self.vehicle_speed <= 0:
                print("Vehicle has successfully come to a stop.")
                self.vehicle_speed = 0
                break

            pressure, slave_force, deceleration = self.apply_brakes(force)
            
            # Update vehicle speed (v = u - at)
            self.vehicle_speed -= deceleration * dt
            self.vehicle_speed = max(0, self.vehicle_speed) # Prevent negative speed

            print(f"Time Step {step+1} (Pedal Force = {force} N):")
            print(f"  System Pressure : {pressure:.2f} N/cm^2")
            print(f"  Clamping Force  : {slave_force:.2f} N")
            print(f"  Deceleration    : {deceleration:.2f} m/s^2")
            print(f"  Current Speed   : {self.vehicle_speed:.2f} m/s\n")
            
            time.sleep(0.5) # Pause to simulate time passing

# --- Run the Simulation ---
if __name__ == "__main__":
    # Initialize the brake system
    brakes = HydraulicBrakeSystem(
        master_cyl_area=5.0,  # cm^2
        slave_cyl_area=20.0,  # cm^2 (Yields a mechanical force multiplier of 4)
        vehicle_mass=1500,    # 1500 kg car
        friction_coefficient=0.8
    )

    # Simulated pedal forces applied by the driver over time (in Newtons)
    # The driver presses gently, then harder, then holds it.
    driver_input_forces = [50, 100, 200, 300, 300, 300, 300, 0]
    
    # Start at ~30 m/s (approx 108 km/h or 67 mph)
    brakes.simulate(initial_speed=30.0, pedal_forces=driver_input_forces)