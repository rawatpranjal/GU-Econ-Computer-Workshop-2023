import os
import platform
import psutil

def get_cpu_info():
    # CPU model and clock speed
    cpu_info = platform.processor()
    clock_speed = psutil.cpu_freq().current

    # Number of CPU cores and threads
    num_cores = psutil.cpu_count(logical=False)
    num_threads = psutil.cpu_count(logical=True)

    # CPU architecture
    architecture = platform.architecture()[0]

    # Get CPU cache size (may not be available on all systems)
    try:
        with open("/sys/devices/system/cpu/cpu0/cache/index0/size") as cache_file:
            cache_size = cache_file.read().strip()
    except Exception:
        cache_size = "N/A"

    # Thermal Design Power (TDP) - not available via Python
    tdp = "N/A"

    # Instruction set - get the platform machine information
    instruction_set = platform.machine()

    # Print CPU information
    print(f"CPU Model: {cpu_info}")
    print(f"CPU Clock Speed: {clock_speed} MHz")
    print(f"Number of CPU Cores: {num_cores}")
    print(f"Number of CPU Threads: {num_threads}")
    print(f"CPU Architecture: {architecture}")
    print(f"CPU Cache Size: {cache_size}")
    print(f"Thermal Design Power (TDP): {tdp}")
    print(f"Instruction Set: {instruction_set}")

if __name__ == "__main__":
    get_cpu_info()

