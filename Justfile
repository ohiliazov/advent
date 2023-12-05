#!/usr/bin/env just --justfile

format:
    poetry run pre-commit run --all
