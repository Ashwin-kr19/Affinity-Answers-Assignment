#!/bin/bash

# URL of the text file containing the data
url="https://www.amfiindia.com/spages/NAVAll.txt"

# Temporary file to store the downloaded data
tmp_file="/tmp/nav_all.txt"

# Download the data file
curl -s "$url" -o "$tmp_file"

# CSV file to store the extracted fields
csv_file="scheme_data.csv"

# Extract Scheme Name and Asset Value fields and save them in the CSV file
awk -F ';' 'BEGIN {OFS=","} {print $3, $8}' "$tmp_file" > "$csv_file"

# Display success message
echo "Extraction complete. Data saved in $csv_file."
