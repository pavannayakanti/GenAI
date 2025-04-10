import os
import re

def capitalize_sentences(text):
    # This regex matches the beginning of a sentence and includes multiline support
    sentence_endings = re.compile(r'([.!?])\s+')
    parts = sentence_endings.split(text)
    
    # Capitalize the first letter of each sentence
    capitalized_parts = []
    for i in range(0, len(parts), 2):
        capitalized_parts.append(parts[i].capitalize())
        if i+1 < len(parts):
            capitalized_parts.append(parts[i+1] + " ")

    return ''.join(capitalized_parts).strip()

# Directory containing the text files
directory = "files"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        # Read the content of the file
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Capitalize the first letter of each sentence
        modified_content = capitalize_sentences(content)
        
        # Write the modified content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(modified_content)

print("Finished processing files.")
