# Affinity-Answers-Assignment
# 1

# Twitter Profanity Detector

The Twitter Profanity Detector is a program written in Python that analyzes a file containing Twitter tweets and indicates the degree of profanity for each sentence. It uses a set of provided racial slurs as a reference for detecting profane language.

## Assumptions

- The program assumes that the tweets are stored in a text file, with one tweet per line.
- The racial slurs set needs to be updated with the actual racial slurs you want to detect. Replace the placeholders in the code with the appropriate slurs.
- The program uses regular expressions to extract words from the tweets. It assumes that each tweet is on a separate line and that there are no other special characters or formatting that may affect the extraction of words.

## Usage

1. Clone the repository or download the Python script.

2. Open the Python script file (`twitter_profanity_detector.py`) in a text editor.

3. Locate the `racial_slurs` set declaration in the script. Replace the placeholders (`"slur1"`, `"slur2"`, `"slur3"`) with the actual racial slurs you want to detect. For example:

   ```python
   racial_slurs = {"racial_slur1", "racial_slur2", "racial_slur3"}
Add or remove slurs as necessary, ensuring they are enclosed in double quotes and separated by commas.

4. Save the modified Python script.

5. Prepare a text file containing the Twitter tweets you want to analyze. Each tweet should be on a separate line. Ensure that there are no empty lines or additional formatting in the file.

6. Move the tweet file to the same directory as the Python script.

7. Open a terminal or command prompt and navigate to the directory where the Python script is located.

8. Run the following command to execute the script:

   ```python
   python twitter_profanity_detector.py
 This command runs the Python interpreter and executes the script, initiating the Twitter profanity analysis.

9. The program will process each tweet in the file and display the tweet along with the corresponding profanity degree. The profanity degree represents the percentage of words in each tweet that match the racial slurs set.

10. Review the results to assess the profanity level of each tweet. The higher the profanity degree, the more potentially offensive or inappropriate the tweet may be.

---

# 2

---

# 3
# Scheme Data Extraction

This shell script is designed to extract the Scheme Name and Asset Value fields from a given URL and save them in a CSV file. The script uses `curl` to download the data and `awk` to extract the desired fields.

## Prerequisites

To run this script, you need to have the following dependencies installed on your system:

- `curl`: A command-line tool for transferring data using various network protocols.
- `awk`: A versatile programming language primarily used for text manipulation.

Make sure you have these dependencies installed before executing the script.

## Usage

1. Download the shell script file (`extract_scheme_data.sh`) from this repository.

2. Open a terminal and navigate to the directory where the script file is located.

3. Make the script file executable by running the following command:

   ```shell
   chmod +x extract_scheme_data.sh
   
4. Run the script using the following command:
   ```shell
   ./extract_scheme_data.sh
   
6. The script will download the data from the provided URL (https://www.amfiindia.com/spages/NAVAll.txt), extract the Scheme Name and Asset Value fields, and save them in a CSV file named scheme_data.csv in the same directory.

6. Once the script finishes executing, you will see a success message indicating that the data has been saved in the CSV file.

## Output

The extracted Scheme Name and Asset Value fields are saved in a CSV file named `scheme_data.csv`. Each row in the CSV file represents a scheme, and the columns contain the following information:

- **Scheme Name**: The name of the scheme.
- **Asset Value**: The asset value of the scheme.
