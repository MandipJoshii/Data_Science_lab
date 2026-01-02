# 5. Use the re module to write a script that searches through a paragraph and extracts all
# words that start with an uppercase letter (e.g., "London", "Python") to identify proper
# nouns or sentence starters.
import re
paragraph = """
Python is a popular programming language.
London is the capital of England Lol2.
Many developers use Python for Data Science.
"""

pattern = r"\b[A-Z][a-zA-Z]*\b"
capital_words = re.findall(pattern, paragraph)


print("Words starting with uppercase letters:")
print(capital_words)