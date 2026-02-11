from extract import extract_state_from_file


def build_output(state: str) -> str:
    data = {
        "project": "UML demo",
        "items": ["auth", "api", "db"],
        "version": "1.0.0",
    }

    if state == "brief":
        return f"[{state}] Проект: {data['project']}"

    if state == "full":
        return (
            f"[{state}] Проект: {data['project']}\n"
            f"Компоненты: {', '.join(data['items'])}\n"
            f"Версия: {data['version']}"
        )

    if state == "debug":
        return (
            f"[{state}] DEBUG OUTPUT\n"
            f"raw_data={data}\n"
            f"items_count={len(data['items'])}"
        )

    return f"[unknown:{state}] Неизвестное состояние, используем безопасный режим"


def main() -> None:
    state = extract_state_from_file("1.md", default="brief")
    print(build_output(state))


if __name__ == "__main__":
    main()
