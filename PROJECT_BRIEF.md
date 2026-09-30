# Project 1 Brief — Statement Explainer

## Goal
Build a CLI tool that answers plain-language questions about a credit card
statement PDF. Ship it to GitHub as the first portfolio project.

## User stories
1. As a cardholder, I upload my statement PDF and ask "why did my interest
   charge go up?" — I get a short, plain answer quoting exact numbers.
2. As a cardholder, I run `--extract` and get key facts (balance, due date,
   minimum payment, interest) as JSON I could feed into a spreadsheet.

## Scope (keep it small)
- Local CLI only. No web UI, no auth, no database.
- Single PDF in, text answer or JSON out.
- Raw OpenAI SDK only — no LangChain/LlamaIndex.

## Weekend task list

### Day 1 — Make it work
- [x] Python env + `pip install -r requirements.txt`
- [x] `.env` with `OPENAI_API_KEY` (platform.openai.com/api-keys)
- [x] Run `python main.py <statement.pdf> --question "What is my total balance?"`
- [x] Run `python main.py <statement.pdf> --extract`
- [x] Read `src/llm.py` until you can explain every parameter of the API call
- [x] Note the token/cost line after each call — build the cost instinct early

### Day 2 — Make it yours (the actual learning)
- [ ] Exercise 1 in `src/prompts.py`: rewrite SYSTEM_QA to show its math
- [ ] Exercise 2: merchant-transaction listing rule
- [ ] Exercise 3: temperature 0.2 vs 0.7 experiment — write down what broke
- [ ] Exercise 4: extend the extraction schema, re-run `--extract`
- [ ] Break it on purpose: ask a question the statement can't answer.
      Does it hallucinate or say "not in the statement"? Fix the prompt until it refuses.
- [ ] `git init`, first commits, push to GitHub (see README)
- [ ] Fill in the "What I learned" section of the README honestly

## Done means
- [ ] Both commands work on a real statement
- [ ] README documents setup, structure, and learnings
- [ ] Repo is public on GitHub with a clean commit history
- [ ] You can explain: tokens, temperature, structured output, why prompts live
      in one file, and roughly what each call costs

## Stretch (only if Day 2 finishes early)
- Multi-question mode: keep asking without re-parsing the PDF each time
- `--compare statement1.pdf statement2.pdf`: "what changed month over month?"

## Concepts this teaches (for interviews later)
"How do you control LLM output format?" → JSON schema structured output.
"How do you manage cost?" → token counting, model choice, per-call visibility.
"How do you stop hallucinations?" → grounding rules in the system prompt,
refusal behavior, low temperature for factual tasks.
