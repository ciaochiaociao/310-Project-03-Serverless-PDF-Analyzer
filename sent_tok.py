import re

def sent_tokenize(text):
    # Regular expression for finding sentences
    sentence_endings = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'
    sentences = re.split(sentence_endings, text)

    # Remove any empty strings in the list
    sentences = [sentence.strip() for sentence in sentences if sentence.strip() != '']

    return sentences

# Example usage
text = "Hello there! How are you doing? This is an example. Let's see how it works."
print(sent_tokenize(text))
