"""Statement Explainer — ask plain-language questions about a credit card statement PDF.

Usage:
    python main.py statement.pdf --question "Why did my interest charge go up?"
    python main.py statement.pdf --extract        # structured key-facts JSON
"""
import argparse
import json

from src import llm, pdf_reader, prompts


def cmd_ask(pdf_path: str, question: str):
    text, pages = pdf_reader.extract_text(pdf_path)
    print(f"Loaded {pages} pages from {pdf_path}\n")
    result = llm.ask(prompts.SYSTEM_QA, prompts.build_qa_prompt(text, question))
    print(result["answer"])
    print(
        f"\n[tokens: {result['input_tokens']} in / {result['output_tokens']} out | "
        f"~${result['cost_usd']:.4f}]"
    )


def cmd_extract(pdf_path: str):
    text, pages = pdf_reader.extract_text(pdf_path)
    print(f"Loaded {pages} pages from {pdf_path}\n")
    result = llm.extract_json(
        prompts.SYSTEM_EXTRACT,
        f"STATEMENT:\n---\n{text}\n---",
        prompts.STATEMENT_SCHEMA,
    )
    print(json.dumps(result["data"], indent=2))
    print(
        f"\n[tokens: {result['input_tokens']} in / {result['output_tokens']} out | "
        f"~${result['cost_usd']:.4f}]"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Ask questions about a credit card statement PDF."
    )
    parser.add_argument("pdf", help="Path to the statement PDF")
    parser.add_argument("--question", "-q", help="Question to ask about the statement")
    parser.add_argument("--extract", action="store_true",
                        help="Extract key facts as JSON")
    args = parser.parse_args()

    if args.extract:
        cmd_extract(args.pdf)
    elif args.question:
        cmd_ask(args.pdf, args.question)
    else:
        parser.error("Provide --question '...' or --extract")


if __name__ == "__main__":
    main()
