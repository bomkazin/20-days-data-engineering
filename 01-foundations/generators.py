import csv
import random
import os

# Setup (Create a dummy CSV file)
FILENAME = "transactions.csv"

def create_dummy_csv(filename):
    print(f"Creating dummy CSV file: {filename}...")
    with open(filename, 'w', newline ='') as f:
        writer = csv.writer(f)
        writer.writerow(["trasaction_id","user_id", "amount", "status"]) #header

        #generate 1 million rows to simulate a large file
        for i in range(1, 1000000):
            writer.writerow([i, random.randint(1000, 9999), 
                             random.randint(10, 2000), #amount between 10 and 2000
                             "completed"])
    print("Dummy CSV file created.")


def read_large_file(file_path):
    """
    Generator function to read a large CSV file line by line.
    It does not load the entire file into memory.
    """
    with open(file_path, 'r') as file:
        
        #Dictionary reader automatically parses the header row and maps values to keys.
        reader = csv.DictReader(file)
        for row in reader:
            #yield hands over control to the caller for this row
            yield row


def process_data(file_path):
    print("Processing data...")
    high_value_count = 0
    total_processed = 0

    #loop over the generator
    #at any single point in time, only one row is in memory
    for row in read_large_file(file_path):
        total_processed += 1

        #data type conversion (csv reads everything as strings)
        amount = float(row['amount'])

        if amount > 1000:
            high_value_count += 1

        #print progress every 100,000 rows
        if total_processed % 100000 == 0:
            print(f"Processed {total_processed} rows...")

    print(f"\n Done! Found {high_value_count} high value transactions out of {total_processed} total transactions.")

if __name__ == "__main__":
    # Create a dummy CSV file for demonstration
    if not os.path.exists(FILENAME):
        create_dummy_csv(FILENAME)

    # Process the large CSV file using the generator
    process_data(FILENAME)

# Clean up the dummy file after processing
    # if os.path.exists(FILENAME):
    #     os.remove(FILENAME)
    # print(f"Removed dummy CSV file: {FILENAME}")
