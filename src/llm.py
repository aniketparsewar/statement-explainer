"""Thin wrappers around the OpenAI API.

Raw SDK on purpose — learn what the frameworks abstract before you ever
touch LangChain. Every call returns usage stats so cost is always visible.
"""
import json

from . import config
from . import costs


def ask(system_prompt: str, user_prompt: str, temperature: float = 0.2) -> dict:
    """Plain chat completion.

    Returns {"answer", "input_tokens", "output_tokens", "cost_usd"}.
    """
    resp = config.get_client().chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
    )
    usage = resp.usage
    return {
        "answer": resp.choices[0].message.content,
        "input_tokens": usage.prompt_tokens,
        "output_tokens": usage.completion_tokens,
        "cost_usd": costs.estimate_cost(usage.prompt_tokens, usage.completion_tokens),
    }


def extract_json(system_prompt: str, user_prompt: str, schema: dict) -> dict:
    """Structured output: forces the model to return valid JSON matching schema.

    temperature=0.0 — extraction should be deterministic, not creative.
    Returns {"data", "input_tokens", "output_tokens", "cost_usd"}.
    """
    resp = config.get_client().chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        response_format={
            "type": "json_schema",
            "json_schema": {"name": "extraction", "schema": schema, "strict": True},
        },
    )
    usage = resp.usage
    return {
        "data": json.loads(resp.choices[0].message.content),
        "input_tokens": usage.prompt_tokens,
        "output_tokens": usage.completion_tokens,
        "cost_usd": costs.estimate_cost(usage.prompt_tokens, usage.completion_tokens),
    }

import base64

def ask_with_pdf(system_prompt: str, question: str, pdf_path: str) -> dict:
    with open(pdf_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    resp = config.get_client().chat.completions.create(
        model=config.MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": question},
                {"type": "file", "file": {
                    "filename": "statement.pdf",
                    "file_data": f"data:application/pdf;base64,{b64}",
                }},
            ]},
        ],
        temperature=0.2,
    )
    usage = resp.usage
    return {
        "answer": resp.choices[0].message.content,
        "input_tokens": usage.prompt_tokens,
        "output_tokens": usage.completion_tokens,
        "cost_usd": costs.estimate_cost(usage.prompt_tokens, usage.completion_tokens),
    }
