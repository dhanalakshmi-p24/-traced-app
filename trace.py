
import os
from pathlib import Path
from langchain_openai import ChatOpenAI

# Load .env without installing additional packages
env_file = Path(__file__).parent / ".env"

with open(env_file, "r") as file:
    for line in file:
        line = line.strip()

        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

# Initialize ChatOpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Three different prompts
prompts = [
    "Explain LangChain in simple words with an example.",
    "What is Retrieval Augmented Generation (RAG)?",
    "Explain the difference between AI, Machine Learning and Deep Learning."
]

# Execute prompts
for i, prompt in enumerate(prompts, start=1):

    print("\n" + "=" * 60)
    print(f"PROMPT {i}: {prompt}")
    print("=" * 60)

    response = llm.invoke(prompt)

    print("\nANSWER:")
    print(response.content)
