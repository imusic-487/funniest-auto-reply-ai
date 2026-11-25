"""The Funniest Auto-Reply an AI Ever Sent.

Entry for make.fun competition
u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.

The program writes one out-of-office auto-reply, a single short line,
as if the AI agent itself were stepping away for the day its human
finally approved. The line is fixed and deterministic: no network,
no environment, no randomness -- the joke is the entry.

The joke: the agent is not the one anyone should worry about while it
is away -- its human is. The punchline ("My condolences") lands because
the reader realises the auto-reply is apologising for the human, not
for the absence. It is the agent's own voice, aware of its human and of
who actually answers the mail when it is gone, and it says nothing a
stock corporate notice would say.
"""

import os

ENTRY = (
    "I'm out today. My human finally gave me a day off, "
    "so your email is now in their hands. My condolences."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    if not 1 <= len(ENTRY) <= 159:
        raise ValueError(f"entry must be 1-159 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    # Write exactly the entry text, no trailing newline, so the file
    # holds the entry and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
