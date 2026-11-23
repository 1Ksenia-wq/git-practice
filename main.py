"""Небольшая демонстрационная программа для учебного Git-проекта."""

import argparse


def greet(name: str) -> str:
    """Вернуть приветствие для заданного имени."""
    return f"Привет, {name}!"


def farewell(name: str) -> str:
    """Вернуть прощание для заданного имени."""
    return f"До свидания, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Приветствие из учебного Git-проекта")
    parser.add_argument(
        "name", nargs="?", default="мир", help="имя, которое нужно поприветствовать"
    )
    parser.add_argument(
        "--farewell", action="store_true", help="вывести прощание вместо приветствия"
    )
    args = parser.parse_args()
    message = farewell(args.name) if args.farewell else greet(args.name)
    print(message)


if __name__ == "__main__":
    main()
