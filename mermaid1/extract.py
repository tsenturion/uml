import re
from pathlib import Path


def extract_state_from_mermaid(markdown_text: str, default: str = "brief") -> str:
    """
    Ищет блоки ```mermaid``` в markdown и извлекает state=...
    Пример: C[state=full]
    """
    mermaid_blocks = re.findall(r"```mermaid\s*(.*?)```", markdown_text, flags=re.DOTALL | re.IGNORECASE)

    for block in mermaid_blocks:
        match = re.search(r"\bstate\s*=\s*([a-zA-Z0-9_-]+)\b", block)
        if match:
            return match.group(1).lower()

    return default


def extract_state_from_file(markdown_path: str = "1.md", default: str = "brief") -> str:
    content = Path(markdown_path).read_text(encoding="utf-8")
    return extract_state_from_mermaid(content, default=default)


if __name__ == "__main__":
    print(extract_state_from_file())
