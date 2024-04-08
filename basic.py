import math

# Function to calculate GPS coordinates of the object
def calculate_object_coordinates(drone_latitude, drone_longitude, drone_heading, distance, object_direction):
    # Convert heading to bearing (radians)
    bearing = math.radians(90 - drone_heading)

    # Calculate lateral and longitudinal displacements
    dEast = distance * math.sin(bearing)
    dNorth = distance * math.cos(bearing)

    # Convert displacements to GPS coordinates
    object_latitude = drone_latitude + (dNorth / 111111)  # Approximate value for latitude degrees
    object_longitude = drone_longitude + (dEast / (111111 * math.cos(math.radians(drone_latitude))))  # Adjust for longitude

    return object_latitude, object_longitude

# Example values (replace with actual data)
drone_latitude = 37.7749  # Example latitude of the drone
drone_longitude = -122.4194  # Example longitude of the drone
drone_heading = 45  # Example heading of the drone in degrees
distance = 100  # Example distance to the object in meters
object_direction = 30  # Example direction of the object in degrees

# Calculate GPS coordinates of the object
object_latitude, object_longitude = calculate_object_coordinates(drone_latitude, drone_longitude, drone_heading, distance, object_direction)

# Output the calculated GPS coordinates
print("Object GPS Coordinates:")
print("Latitude:", object_latitude)
print("Longitude:", object_longitude)

