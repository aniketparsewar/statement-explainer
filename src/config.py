"""Central configuration: API keys, model choice, client setup."""
import os
from functools import lru_cache

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# gpt-4o-mini: cheap and fast — ideal for learning loops where you'll
# iterate on prompts dozens of times.
# Approximate pricing (verify at https://openai.com/api/pricing):
#   ~$0.15 / 1M input tokens, ~$0.60 / 1M output tokens
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


@lru_cache(maxsize=1)
def get_client() -> OpenAI:
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env "
            "and add your key from https://platform.openai.com/api-keys"
        )
    return OpenAI(api_key=key)
