"""Open AI."""
from typing import List

import openai
from gptancial.config import OPEN_AI_API_KEY

openai.api_key = OPEN_AI_API_KEY

def generate_completion(
    symbol: str,
    engine: str,
    data_input: str,
    max_tokens: int = 256,
    n_completitons: int = 1,
    temperature: float = 0.5,
) -> List[str]:
    input_prompt = (
        f"Here's a huge amount of indicators for {symbol} stock.\n\n"
        f"{data_input}\n\n\n"
        "Can you please summarize this data, providing insights about it, "
        "some conclusions over the performance of the stock, and some "
        "perspectives for future performance of the stock price? "
        "Be as detailed as you can, as if you were talking for someone that is not a financial expert."
    )

    response = openai.Completion.create(
        engine=engine,
        prompt=input_prompt,
        max_tokens=max_tokens,
        n=n_completitons,
        stop=None,
        temperature=temperature,
    )

    return [choice.text.strip() for choice in response.choices]


def generate_chat(
    symbol: str,
    model: str,
    data_input: str,
    user_question: str,
) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Here's some indicators for {symbol} stock.\n\n{data_input}"},
        {"role": "user", "content": user_question},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )

    return response["choices"][0]["message"]["content"]
