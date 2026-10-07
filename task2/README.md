# App settings utility

`config_writer.py` provides `update_settings(new_theme, new_font_size)` for an
app that keeps its preferences in `settings.json` beside the script.

Existing callers use themes `light` and `dark` and integer font sizes from 10 to
24. The file already exists and contains a JSON object. Other preference values
and their types must be retained; indentation and key order are not important.

From this folder, the existing command-line entry requests theme `dark` and
font size `14`:

```sh
python config_writer.py
```

The same function is also called directly by the app with its requested values.
