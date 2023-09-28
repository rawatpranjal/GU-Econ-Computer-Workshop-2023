import multiprocessing
import time

# Define a simple function to simulate a task
def task():
    for _ in range(10**7):  # Simulate a CPU-bound task
        pass

# Number of processes to create (equal to the number of CPU cores)
num_processes = 16  # Adjust this number based on your available CPU cores

# Single-process version
start_time = time.time()
for _ in range(num_processes):
    task()
single_process_time = time.time() - start_time

# Multi-process (parallel) version
processes = []
start_time = time.time()
for _ in range(num_processes):
    process = multiprocessing.Process(target=task)
    process.start()
    processes.append(process)

# Wait for all processes to finish
for process in processes:
    process.join()

multi_process_time = time.time() - start_time

print(f"Single-process time: {single_process_time:.2f} seconds")
print(f"Multi-process time: {multi_process_time:.2f} seconds")

