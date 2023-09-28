import time
import multiprocessing

def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

def sum_of_squares_partial(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i ** 2
    return total

N = 10000000  # Large number

# Single Processor Solution
start_time = time.time()
result_single = sum_of_squares(N)
end_time = time.time()
print(f"Single Processor Solution Result: {result_single}")
print(f"Time taken by Single Processor: {end_time - start_time} seconds")

# Multiprocessing Solution
num_processes = multiprocessing.cpu_count()  # Get the number of CPU cores
chunk_size = N // num_processes
ranges = [(i * chunk_size + 1, (i + 1) * chunk_size) for i in range(num_processes)]

start_time = time.time()
pool = multiprocessing.Pool(processes=num_processes)
results = pool.starmap(sum_of_squares_partial, ranges)
pool.close()
pool.join()
total_sum = sum(results)
end_time = time.time()

print(f"Multiprocessing Solution Result: {total_sum}")
print(f"Time taken by Multiprocessing: {end_time - start_time} seconds")

