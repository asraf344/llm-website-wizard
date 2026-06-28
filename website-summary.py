import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv('GEMINI_API_KEY')

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=api_key)

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""


def messages_for(website):
    """Create message list for the LLM."""
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]


def summarize(url):
    """Fetch and summarize a website using Ollama."""
    website = fetch_website_contents(url)
    response = gemini.chat.completions.create(model="gemini-2.5-flash-lite", messages=messages_for(website))

    return response.choices[0].message.content


def main():
    """Main entry point for testing."""
    url = input("Enter a URL to summarize: ")
    print("\nFetching and summarizing...\n")
    summary = summarize(url)
    print(summary)


if __name__ == "__main__":
    main()


