#!/usr/bin/env python3
"""Update app preferences stored in settings.json.

Run this utility with task2 as the working directory. Running the file directly
requests theme "dark" and font size 14.
"""

import json


def update_settings(new_theme, new_font_size):
    """Save the requested preferences while preserving all other settings.

    Existing callers use update_settings(new_theme, new_font_size).
    new_theme: "light" or "dark".
    new_font_size: an integer from 10 to 24, inclusive.
    Callers supply valid arguments and an existing, valid settings.json file.
    Other settings retain their values and types; JSON layout may change.
    """
    config_path = "settings.json"
    with open(config_path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    settings["theme"] = new_theme
    settings["font_size"] = new_font_size
    updated_json = json.dumps(settings, indent=2)

    print("Settings updated!")
    return updated_json


if __name__ == "__main__":
    update_settings(new_theme="dark", new_font_size=14)
