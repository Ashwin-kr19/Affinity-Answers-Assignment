import re

racial_slurs = {"slur1", "slur2", "slur3"}  # Replace with the actual racial slurs

def calculate_profanity(tweet):
    words = re.findall(r'\w+', tweet.lower())  # Extract words from the tweet
    total_words = len(words)
    profane_words = 0

    for word in words:
        if word in racial_slurs:
            profane_words += 1

    if total_words == 0:
        return 0

    profanity_degree = (profane_words / total_words) * 100
    return profanity_degree


def main():
    file_path = "tweets.txt"  # Replace with the actual file path

    with open(file_path, 'r') as file:
        tweets = file.readlines()

    for tweet in tweets:
        profanity_degree = calculate_profanity(tweet)
        print(f"Tweet: {tweet.strip()}")
        print(f"Profanity Degree: {profanity_degree}%")
        print()


if __name__ == '__main__':
    main()
