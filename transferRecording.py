import openai
# from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
# client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))
client = openai.OpenAI(api_key=os.getenv("GENAI_API_KEY"),
                       base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

#custom prompt type shii 
PROMPT = (
    "You are a helpful assistant that takes in a file containing a recorded log "
    "of terminal activity. Your task is to transform this raw log into clear, "
    "structured documentation. For each command in the file: "
    "- Present the input (the command that was run). "
    "- Present the output (the system’s response). "
    "- Provide a plain-language explanation of what the command does and what "
    "the output means. Continue this process sequentially until the end of the file. "
    "Format the documentation in Markdown for readability. Use headers to separate "
    "sections, bullet points for clarity, and code blocks to display commands and "
    "outputs. The final result should be easy to read and follow, making it clear "
    "what was done step by step in the terminal session."
)

#function to call the openai api
def openai_comp(PROMPT, file_content):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": file_content}
        ],
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content']

def gemini_comp(PROMPT, file_content):
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": PROMPT},
            {"role": "user", "content": file_content}
        ]
    )
    return response.choices[0].message['content']


def gemini_comp(PROMPT, file_content):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        messages=[
            {"role": "user", "content": file_content}
        ]
    )
    return response.choices[0].message

#read content of the recorded file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # get file name and validate it
    filename = input("Enter the path to the terminal recording file: ")
    if not filename:
        print("No file path provided. Exiting.")
        return
    
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return
    
    
    file_content = read_file(filename)

    print(" Selecting model to use for documentation generation...")
    # documentation = openai_comp(PROMPT, file_content)
    model_choice = input("Choose model (1 for OpenAI GPT-4, 2 for Gemini 2.5): ")
    if model_choice == '1':
        documentation = openai_comp(PROMPT, file_content)
    elif model_choice == '2':
        documentation = gemini_comp(PROMPT, file_content)
    else:
        print("Invalid choice. Exiting.")
        return

    output_filename = "terminal_documentation.md"
    with open(output_filename, 'w') as output_file:
        output_file.write(documentation)
    print(f"Documentation written to {output_filename}")

if __name__ == "__main__":
    main()  
