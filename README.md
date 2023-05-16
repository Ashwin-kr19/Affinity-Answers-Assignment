# Affinity-Answers-Assignment
#1

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
