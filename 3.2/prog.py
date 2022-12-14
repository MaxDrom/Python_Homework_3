import json
from datetime import datetime

current_time = str(datetime.now())
try:
    result_file = open("result.json", "r")
except IOError:
    times = []
    print("First run")
else:
    times = json.load(result_file)
    print(*times[-3::1], sep="\n")
    result_file.close()

result_file = open("result.json", "w")
times.append(current_time)
json.dump(times, result_file)
result_file.close()