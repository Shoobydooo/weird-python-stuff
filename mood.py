from textblob import TextBlob


def analyze_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    elif -0.3 <= polarity <= 0.3:
        return "neutral"


def get_ascii_art(mood):
    arts = {
        "happy": r"""
          \  ^__^
           \ (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
        """,
        "sad": r'''
            .-""""-.
           /        \
          /_        _\
         // \      / \\
         |\__\    /__/|
          \    ||    /
           \        /
            \  __  /
             '.__.'
              |  |
              |  |
        ''',
        "neutral": r"""
           -----
          | . . |
          |  ^  |
          | '-' |
           -----
        """,
    }
    return arts.get(mood, "No art available for this mood.")


def main():
    text = input("Enter some text about your day: ")
    mood = analyze_mood(text)
    print(f"\nDetected mood: {mood}\n")
    art = get_ascii_art(mood)
    print(art)


if __name__ == "__main__":
    main()
