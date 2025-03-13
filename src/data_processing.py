import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        """Loads telemetry data from a CSV file or generates synthetic data."""
        if self.file_path:
            self.data = pd.read_csv(self.file_path)
        else:
            # Generate synthetic telemetry data if no file is provided
            time = np.arange(0, 10, 0.1)  # 10 seconds, 0.1s step
            speed = np.clip(3 * time, 0, 30)  # Simulated speed increase
            acceleration = np.gradient(speed, 0.1)
            braking_force = np.zeros_like(time)
            braking_force[50:] = -5  # Simulated braking at 5s
            steering_angle = np.sin(time) * 10  # Simulated cornering
            
            self.data = pd.DataFrame({
                'time': time,
                'speed': speed,
                'acceleration': acceleration,
                'braking_force': braking_force,
                'steering_angle': steering_angle
            })
    
    def preprocess_data(self):
        """Smooths and filters noisy telemetry data."""
        if self.data is None:
            raise ValueError("No data loaded. Run load_data() first.")
        
        # Apply a rolling mean filter to smooth noise
        self.data['speed_smooth'] = self.data['speed'].rolling(window=5, center=True).mean()
        self.data['acceleration_smooth'] = self.data['acceleration'].rolling(window=5, center=True).mean()
        self.data['braking_force_smooth'] = self.data['braking_force'].rolling(window=5, center=True).mean()
    
    def save_processed_data(self, output_path='processed_data.csv'):
        """Saves the processed data to a CSV file."""
        self.data.to_csv(output_path, index=False)
    
# Example usage
if __name__ == "__main__":
    processor = DataProcessor()
    processor.load_data()
    processor.preprocess_data()
    processor.save_processed_data("data/processed_data.csv")
    print("Data processing complete. Processed data saved to processed_data.csv.")
