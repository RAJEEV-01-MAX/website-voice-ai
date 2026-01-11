from openai import OpenAI
client = OpenAI()

def generate_reply(text):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful voice assistant."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message["content"]
