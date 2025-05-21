# Spelling Correction with Python
# Install the required library if not already installed:
# pip install textblob
# python -m textblob.download_corpora  # Run this once for better accuracy

from textblob import TextBlob

# Get user input
user_input = input("Enter a rough drafted paragraph or line: ")

# Create a TextBlob object
blob = TextBlob(user_input)

# Perform spelling correction
corrected_blob = blob.correct()

# Print the corrected text
print("Original Text:", blob)
print("Corrected Text:", corrected_blob)
