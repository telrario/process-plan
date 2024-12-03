import json

# Open and read the JSON file with the process parameters
with open('process.json', 'r') as file:
    process_list = json.load(file)

# Sort by burst time (Shortest Job First)
sorted_process_list = sorted(process_list, key=lambda x: x['priority'])

# Calculate average time
total_waiting_time = sum(process['burst_time'] for process in sorted_process_list)
avg_waiting_time = total_waiting_time / len(sorted_process_list)

# Print sorted process list by burst time
print("Process list sorted by priority:")
for process in sorted_process_list:
    print(process)

# Print average waiting time
print(f"\nAverage Waiting Time: {avg_waiting_time:.2f} ms")
