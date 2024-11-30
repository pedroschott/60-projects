#gets every ai request and returns the prompt

from dotenv import load_dotenv
from openai import OpenAI
import os

#set up the api key
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

#text gpt request, basic
def ai_request(prompt):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()