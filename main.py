import openai
import asyncio
from openai import AsyncOpenAI, OpenAI

client = OpenAI()
# Synchronous client
def call_gpt_sync(prompt: str) -> str:
    """
    Make a synchronous call to GPT-3.5 Turbo
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # Controls randomness (0.0 - 2.0)
            max_tokens=150,  # Maximum length of response
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling GPT-3.5 Turbo: {str(e)}")
        return None


# Asynchronous client
async def call_gpt_async(prompt: str) -> str:
    """
    Make an asynchronous call to GPT-3.5 Turbo
    """

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=150,
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling GPT-3.5 Turbo: {str(e)}")
        return None


# Example usage of synchronous call
def main_sync():
    prompt = "What is the capital of France?"
    response = call_gpt_sync(prompt)
    print(f"Response: {response}")


# Example usage of async call
async def main_async():
    prompt = "Hello world"
    print(prompt)
    response = await call_gpt_async(prompt)
    print(f"Response: {response}")


# Run examples
if __name__ == "__main__":
    # Synchronous example
    # print("Running synchronous example:")
    # main_sync()

    # Async example
    print("\nRunning asynchronous example:")
    asyncio.run(main_async())