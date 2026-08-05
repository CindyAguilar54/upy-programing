#Sensor
sensor = [32, 35, 40, 50, 29, 25, 34, 35, 37, 40, 14, 12]
morning = sensor[:6]
afternoon = sensor[6:]
sampled = sensor[::3]
print("morning: ", morning)
print("afternoon: ", afternoon)
print("sampled: ", sampled)