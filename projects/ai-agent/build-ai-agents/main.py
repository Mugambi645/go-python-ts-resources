import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError(
        "OPENROUTER_API_KEY environment variable not found. "
        "Please ensure your .env file is configured correctly."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ]
)

# 5. Verify that the response's usage property is not None
if response.usage is None:
    raise RuntimeError(
        "The API response did not include token usage information. "
        "The request may have failed or was not fully processed."
    )

# 6. Print the token usage stats
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")

print(response.choices[0].message.content)


