from openai import OpenAI
from langchain_openai import ChatOpenAI

BASE_URL = "http://localhost:3000/v1"
API_KEY = "not-needed"

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
)

for model in ("auto:text", "auto:reasoning"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Explain what Free-AI Gateway does in one sentence.",
            }
        ],
    )
    print(f"{model}: {response.choices[0].message.content}")

llm = ChatOpenAI(
    model="auto:text",
    base_url=BASE_URL,
    api_key=API_KEY,
)

for chunk in llm.stream("Say hello in one sentence."):
    print(chunk.content, end="", flush=True)

print()
