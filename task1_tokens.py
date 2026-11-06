import re

samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944",
    "",
    "یہ ایک مثال ہے"
]

for text in samples:
    whitespace = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)

    print("\nOriginal:", repr(text))
    print("Whitespace tokens:", whitespace)
    print("Word-like tokens:", words)
    print("Whitespace count:", len(whitespace))
    print("Word-like count:", len(words))