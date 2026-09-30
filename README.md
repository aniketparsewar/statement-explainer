# Statement Explainer

Ask plain-language questions about a credit card statement PDF, powered by an LLM.

```bash
python main.py statement.pdf --question "Why did my interest charge go up?"
python main.py statement.pdf --extract   # key facts as structured JSON
```

Project 1 of the [AI Engineer in 3 Months](..) track. The goal isn't the app —
it's learning how LLM apps actually work: prompts, structured output, tokens, cost.

## Setup

1. Python 3.11+
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your OpenAI API key
   ([get one here](https://platform.openai.com/api-keys))
4. `python main.py --help`

A full weekend of experimenting costs well under $2 on `gpt-4o-mini`.

## Project structure

```
main.py            # CLI entry: --question for Q&A, --extract for JSON facts
src/
  config.py        # env loading, model choice, API client
  pdf_reader.py    # PDF text extraction (PyMuPDF)
  llm.py           # raw OpenAI SDK wrappers — ask() and extract_json()
  prompts.py       # ALL prompts live here; this is where you'll iterate
  costs.py         # token counting + cost estimates per call
```

Deliberately no LangChain yet — learn what the raw SDK does first, then you'll
understand what frameworks are abstracting.

## What I learned

- LLM APIs: chat completions, system vs user messages, temperature
- Structured output via JSON schema mode (deterministic extraction)
- Token counting with tiktoken and per-call cost awareness
- Prompt iteration: the prompt is part of the program, version it like code

## Exercises completed

- [x] Rewrote SYSTEM_QA to show its math on interest questions
- [x] Added merchant-transaction listing rule
- [x] Compared temperature 0.2 vs 0.7 on ambiguous questions
- [x] Extended extraction schema with rewards points

## Privacy note

`*.pdf` is gitignored — never commit a real statement to GitHub. Use a
redacted/sample statement for demos.
