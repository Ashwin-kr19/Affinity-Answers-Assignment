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
# Open Images: Vast and Diverse Dataset

The Open Images dataset is a valuable resource for computer vision researchers and developers. It offers a vast collection of images accompanied by annotations such as object boundaries, making it unique and highly useful for various applications.

## Key Features

- **Size and Variety**: The Open Images dataset comprises millions of images from diverse categories, including people, animals, and objects. This extensive collection provides a wide range of visual data for training and testing computer vision models.

- **Annotations**: The dataset includes annotations such as object boundaries, which aid in improving object recognition and scene understanding. These annotations enable researchers and developers to develop more accurate and efficient computer vision algorithms.

- **Ongoing Updates**: The Open Images dataset is regularly updated, allowing users to stay up-to-date with the latest developments in the field of computer vision. This feature ensures access to new images and annotations, facilitating continuous progress in training and testing computer vision models.

## Benefits and Applications

- **Improved Model Training**: With its extensive size and variety, the Open Images dataset offers a rich source of data for training computer vision models. Its diverse collection enables researchers and developers to create more robust and generalized models.

- **Enhanced Object Recognition**: The availability of annotations such as object boundaries helps refine object recognition algorithms. This dataset enables researchers and developers to develop models capable of accurately identifying and localizing objects within images.

- **Scene Understanding**: The Open Images dataset contributes to advancing scene understanding by providing a large and diverse collection of images. This resource assists researchers in studying and developing algorithms that can comprehend and interpret complex visual scenes.

## Getting Started

To access the Open Images dataset, visit the official website: [Open Images](https://opensource.google/projects/open-images-dataset)

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
