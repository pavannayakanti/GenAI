import os
import re
import wikipediaapi

# Initialize Wikipedia API with user agent
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='MyDataAnalysisScript/1.0 (https://myprojectsite.com; pavan130980@gmail.com)'
)

def fetch_wikipedia_summary(prompt):
    # Function to fetch the summary of a Wikipedia page
    page = wiki_wiki.page(prompt)
    if page.exists():
        return page.summary
    else:
        return "The page does not exist."

def fetch_wikipedia_content(prompt):
    # Function to fetch the full content of a Wikipedia page
    page = wiki_wiki.page(prompt)
    if page.exists():
        return page.text
    else:
        return "The page does not exist."

def capitalize_sentences(text):
    # Function to capitalize the first letter of each sentence in the text
    def capitalize(match):
        return match.group(1).upper() + match.group(2)
    return re.sub(r'(^|\.\s+)(\w)', capitalize, text)

# Directory containing the text files
input_directory = "files"

# Iterate over all files in the directory to capitalize sentences
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):  # Check if the file is a text file
        file_path = os.path.join(input_directory, filename)
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Capitalize the first letter of each sentence
        modified_content = capitalize_sentences(content)
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

print("First letter of each sentence in all text files has been capitalized.")

# Prompts to fetch summaries and content from Wikipedia
prompts = [
    "Albert Einstein",
    "Quantum Mechanics",
    "Python (programming language)",
    "Artificial Intelligence",
    "Machine Learning"
]

# Fetch and display summaries from Wikipedia
for prompt in prompts:
    print(f"Prompt: {prompt}")
    summary = fetch_wikipedia_summary(prompt)
    print(f"Summary:\n{summary}\n")

# Extended task: Fetch detailed content for a specific topic
topic = "Artificial Intelligence"
content = fetch_wikipedia_content(topic)
print(f"Content for {topic}:\n{content[:2000]}...\n")  # Displaying first 2000 characters for brevity
