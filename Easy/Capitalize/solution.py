# Complete the solve function below.
def solve(s):
    cap_words = [word.capitalize() for word in s.split(" ")]
    return " ".join(word for word in cap_words)
