import time
import random
def check_global_pulse():
print("starting world affairs monitor...")
time.sleep(0.5)
# list of regions we are tracking
regions = ["Middle East", "Eastern Europe", "East Asia", "North America"]
while True:
active_region = random.choice(regions)
tension_level = random.randint(75, 98)
climate_alert = random.choice(["Normal", "Elevated Risk", "Critical Threshold"])
print("\n--- status update ---")
print("target region: " + active_region)
print("tension index: " + str(tension_level) + "%")
print("climate tipping status: " + climate_alert)
print("---------------------")
# wait for 5 seconds before next poll
time.sleep(5)
if name == "main":
check_global_pulse()
