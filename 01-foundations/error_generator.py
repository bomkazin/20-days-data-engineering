import random
import os

FILENAME = "server_log.log"

def generate_dummy_log(filename):
    #open file in 'w' mode to clear previous contents
    with open(filename, 'w', newline='') as f:
        for i in range(1000000):

            #generate a random million lines of log entries
            random_number = random.random()

            if random_number < 0.01: #1% chance of error
                f.write(f"ERROR: 500 Internal Server Error at [Timestamp]\n")
            else:
                f.write(f"INFO: User logged in \n")


def read_large_log(file_path):
    """
    Generator function to read a large log file line by line.
    It does not load the entire file into memory.
    """
    with open(file_path, 'r') as file:
        for line in file:
            #yield hands over control to the caller for this line
            yield line


def process_log(file_path):
    print("Processing log file...")
    error_count = 0
    total_lines = 0

    #loop over the generator
    #at any single point in time, only one line is in memory
    for line in read_large_log(file_path):
        total_lines += 1

        if "ERROR" in line:
            error_count += 1

        #print progress every 100,000 lines
        if total_lines % 100000 == 0:
            print(f"Processed {total_lines} lines...")

    print(f"\n Done! Found {error_count} error entries out of {total_lines} total log entries.")


if __name__ == "__main__":
    if not os.path.exists(FILENAME):
        generate_dummy_log(FILENAME)
        
    process_log(FILENAME)