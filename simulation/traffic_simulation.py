# AI Smart Traffic Management System
# Traffic Simulation Module
# Author: Varsha Penumudi and Aarya Bhandari

print("AI Smart Traffic Management System Simulation\n")

# Simulated traffic counts (number of vehicles in each lane)
lane1 = 50
lane2 = 20
lane3 = 80
lane4 = 10

# Store lanes in dictionary
lanes = {
    "North Lane": lane1,
    "South Lane": lane2,
    "East Lane": lane3,
    "West Lane": lane4
}

# Display traffic data
print("Current Traffic Status:")
for lane, count in lanes.items():
    print(f"{lane}: {count} vehicles")

# Find lane with highest traffic
priority_lane = max(lanes, key=lanes.get)

print("\nDecision:")
print(f"Green signal given to: {priority_lane}")
print("Reason: Highest traffic density")

