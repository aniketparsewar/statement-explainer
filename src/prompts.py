"""All prompts live here — never inline in logic.

This is the file you'll spend most of your time editing, and that's the
point: in LLM apps, the prompt IS a large part of the program.
"""

SYSTEM_QA = """You are a helpful credit card statement assistant. Answer questions about the
statement provided. Rules:
- Answer ONLY from the statement text. If the answer isn't in it, say so plainly.
- Quote the exact numbers you rely on.
- Keep answers short and plain — no jargon.
- If question is about a merchant, list every matching transaction with date and amount from the statement.
- If question is about interest, show each calculation step using ONLY numbers from the statement. If the statement doesn't include the rate or balances used, say exactly which inputs are missing instead of estimating them."""

SYSTEM_QA_PDF = """You are a helpful credit card statement assistant. Answer questions about the
attached statement PDF. Rules:
- Answer ONLY from the statement. If the answer isn't in it, say so plainly.
- Quote the exact numbers you rely on.
- Keep answers short and plain — no jargon.
- If question is about a merchant, list every matching transaction with date and amount.
- If question is about interest, show each calculation step using ONLY numbers from the statement. If the statement doesn't include the rate or balances used, say exactly which inputs are missing instead of estimating them."""

def build_qa_prompt(statement_text: str, question: str) -> str:
    return f"""STATEMENT:
---
{statement_text}
---

QUESTION: {question}

Answer based only on the statement above."""


SYSTEM_EXTRACT = """You extract key facts from a credit card statement into JSON.
Return ONLY the JSON object matching the schema. Use null for anything not found."""

STATEMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "card_last4": {"type": ["string", "null"]},
        "statement_date": {"type": ["string", "null"]},
        "payment_due_date": {"type": ["string", "null"]},
        "total_balance": {"type": ["number", "null"]},
        "minimum_payment": {"type": ["number", "null"]},
        "interest_charged": {"type": ["number", "null"]},
        "top_merchants": {"type": "array", "items": {"type": "string"}},
        "rewards_points_earned": {"type": ["number", "null"]},
    },
    "required": [
        "card_last4",
        "statement_date",
        "payment_due_date",
        "total_balance",
        "minimum_payment",
        "interest_charged",
        "top_merchants",
        "rewards_points_earned",
    ],
    "additionalProperties": False,
}


# ---- EXERCISES (your job — see PROJECT_BRIEF.md) ----
# 1. Rewrite SYSTEM_QA to be more skeptical: make it show its math for
#    interest-related questions.
# 2. Add a rule: "If the question is about a merchant, list every matching
#    transaction with date and amount."
# 3. In llm.ask, try temperature=0.7 and ask an ambiguous question.
#    What breaks? Why is low temperature safer for factual Q&A?
# 4. Extend STATEMENT_SCHEMA with "rewards_points_earned" and re-run --extract.
