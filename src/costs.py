"""Token counting and rough cost estimates.

Knowing what each call costs is an AI-engineer survival skill:
a prompt that works in a demo can bankrupt you at 1M requests/day.
"""
import tiktoken

ENCODING = "o200k_base"  # matches gpt-4o-mini

# Approximate prices per 1M tokens for gpt-4o-mini — verify current pricing at
# https://openai.com/api/pricing before quoting numbers to anyone.
INPUT_PER_1M = 0.15
OUTPUT_PER_1M = 0.60


def count_tokens(text: str) -> int:
    enc = tiktoken.get_encoding(ENCODING)
    return len(enc.encode(text))


def estimate_cost(input_tokens: int, output_tokens: int) -> float:
    return (input_tokens / 1e6) * INPUT_PER_1M + (output_tokens / 1e6) * OUTPUT_PER_1M
