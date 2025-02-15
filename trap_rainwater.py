import numpy as np
import rasterio  # To read real-world elevation data
import matplotlib.pyplot as plt
from multiprocessing import Pool
import os


def load_dem(file_path):
    """
    Load Digital Elevation Model (DEM) data from a raster file.
    """
    with rasterio.open(file_path) as dataset:
        elevation = dataset.read(1)  # Read the first band
        elevation = np.nan_to_num(elevation, nan=0)  # Replace NaNs with 0
    return elevation


def preprocess_terrain(elevation):
    """
    Convert 2D elevation data into a 1D height array by averaging columns.
    """
    return np.mean(elevation, axis=0).astype(int)


def trap_rain_water(height):
    """
    Compute trapped rainwater using the two-pointer approach.
    """
    if not height or len(height) < 3:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])
    
    return water_trapped


def visualize_trapped_water(height):
    """
    Visualizes terrain and trapped water.
    """
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    for i in range(n):
        trapped_water[i] = max(0, min(left_max[i], right_max[i]) - height[i])

    x = np.arange(n)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x, height, color='blue', alpha=0.6, label="Terrain")
    ax.bar(x, trapped_water, bottom=height, color='cyan', alpha=0.6, label="Trapped Water")
    ax.set_xlabel("Position")
    ax.set_ylabel("Height")
    ax.set_title("Trapped Rainwater Visualization")
    ax.legend()
    plt.show()


def parallel_compute_trap(height_chunks):
    """
    Computes trapped water in parallel for large datasets.
    """
    with Pool(os.cpu_count()) as pool:
        results = pool.map(trap_rain_water, height_chunks)
    return sum(results)


def main():
    # Load real-world DEM data (update with your file path)
    dem_file = "sample_dem.tif"  # Replace with actual DEM file
    if not os.path.exists(dem_file):
        print("DEM file not found. Please provide a valid path.")
        return

    elevation = load_dem(dem_file)
    height_array = preprocess_terrain(elevation)
    
    # Compute trapped water
    total_water = trap_rain_water(height_array)
    print(f"Total trapped rainwater: {total_water} units")
    
    # Visualize
    visualize_trapped_water(height_array)
    
    # Parallel processing for large datasets
    chunk_size = len(height_array) // os.cpu_count()
    height_chunks = [height_array[i:i+chunk_size] for i in range(0, len(height_array), chunk_size)]
    parallel_water = parallel_compute_trap(height_chunks)
    print(f"Parallel Computation - Total Trapped Water: {parallel_water} units")


if __name__ == "__main__":
    main()
