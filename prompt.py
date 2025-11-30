
# textutil/prompt.py
"""
Utility functions for text prompts.
This module must contain only imports and function/class definitions.
No code should run at import time.
"""

from typing import List, Optional

def normalize_text(s: str) -> str:
    """
    Minimal example helper — normalize whitespace and lowercase.
    Replace with your real functions required by tests.
    """
    if s is None:
        return ""
    return " ".join(s.split()).lower()

def split_sentences(text: str) -> List[str]:
    """
    Example function — split text into sentences (very simple).
    """
    if text is None:
        return []
    # NOTE: very naive split, replace with assignment logic if needed
    return [t.strip() for t in text.split('.') if t.strip()]

# Add here the real functions the tests expect.
# Example:
# def expected_function(...):
#     ...
