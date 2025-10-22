#!/usr/bin/env python3
"""Tiny CLI for unit/integration tests demo."""
import argparse
import logging
from typing import List, Optional

LOGGER_FORMAT = "%(levelname)s: %(message)s"

def generate_messages(name: str, repeat: int) -> List[str]:
    if repeat < 1:
        raise ValueError("repeat must be >= 1")
    return [f"Hello, {name}!" for _ in range(repeat)]

def run(name: str, repeat: int, logger: Optional[logging.Logger] = None) -> None:
    logger = logger or logging.getLogger(__name__)
    for idx, msg in enumerate(generate_messages(name, repeat), start=1):
        logger.info("(%d) %s", idx, msg)

def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="TestingPy.py")
    parser.add_argument("name", help="Name to greet")
    parser.add_argument("-r", "--repeat", type=int, default=1, help="How many times to repeat (>=1)")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT)
    try:
        run(args.name, args.repeat)
    except ValueError as e:
        logging.getLogger(__name__).error(str(e))
        return 2
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
