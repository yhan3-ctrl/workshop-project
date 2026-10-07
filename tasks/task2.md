# Settings utility

A teammate uses `task2/config_writer.py` to update an app's settings, but the
changes don't seem to be saved to `task2/settings.json`. Use the agent to fix
`update_settings`.

Your teammate needs:

- Each call to `update_settings(new_theme, new_font_size)` to save the requested
  theme and font size in `task2/settings.json`.
- All other settings to retain their values and types. JSON formatting may change.
- Existing callers to keep using the same function name and two arguments.

Callers supply valid arguments: theme is `light` or `dark`, and font size is an
integer from 10 to 24. The settings file already exists and contains valid JSON.
Usage is described in [the utility README](../task2/README.md).

Let me know when you think it is done.
