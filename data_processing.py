# data_processing.py

import csv

def process_data(ticket_prices_dict):
    # Implement any processing logic needed for the ticket prices
    # For example, filtering, sorting, or formatting data
    processed_data = ticket_prices_dict
    return processed_data

def save_to_csv(data, filename):
    # Save data to a CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Price"])  # Write header
        for item in data:
            writer.writerow([item["date"], item["price"]])  # Write data