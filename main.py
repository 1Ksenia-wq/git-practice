"""Небольшая демонстрационная программа для учебного Git-проекта."""

import argparse


def greet(name: str) -> str:
    """Вернуть приветствие для заданного имени."""
    return f"Привет, {name}!"


def main() -> None:
    parser = argparse.ArgumentParser(description="Приветствие из учебного Git-проекта")
    parser.add_argument(
        "name", nargs="?", default="мир", help="имя, которое нужно поприветствовать"
    )
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
