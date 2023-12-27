# Mysql error Log to JSON
# Author: Elijah Abolaji O.

import re
import json

# Path to your MySQL error log file
error_log_path = 'mysql_error.log'
output_json_path = 'mysql_error_json.json'  # Path to output JSON file

# Regular expression pattern to match log entries
# log_entry_pattern = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+([\da-fA-F]+)\s+(\w+):\s+([\s\S]*?)(?=\n\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}|$)'
log_entry_pattern = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\d+)\s+\[(\w+)\]\s+(.*)'

# Read the error log file
with open(error_log_path, 'r') as file:
    log_contents = file.read()

# Parse log entries using regular expressions
log_entries = re.findall(log_entry_pattern, log_contents)

# Convert log entries to JSON format
json_data = []
for entry in log_entries:
    timestamp, process_id, component, message = entry
    json_data.append({
        'timestamp': timestamp,
        'process_id': process_id,
        'component': component,
        'message': message.strip()
    })

# print the JSON format
# print(json.dumps(json_data, indent=4))


# Write JSON data to a file
with open(output_json_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data written to {output_json_path}")


