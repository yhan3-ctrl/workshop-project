#!/usr/bin/env bash
set -euo pipefail

npm install -g @google/gemini-cli@0.62.0

# Keep the installed CLI version stable when it starts interactively.
# System settings are outside the activity files; retain any existing settings.
sudo install -d /etc/gemini-cli
sudo python3 - <<'PY'
import json
import os
from pathlib import Path
import tempfile

path = Path('/etc/gemini-cli/settings.json')
settings = json.loads(path.read_text()) if path.exists() else {}
if not isinstance(settings, dict):
    raise ValueError('Gemini system settings must be a JSON object.')
general = settings.setdefault('general', {})
if not isinstance(general, dict):
    raise ValueError('Gemini general settings must be a JSON object.')
general['enableAutoUpdate'] = False
general['enableAutoUpdateNotification'] = False
fd, temporary = tempfile.mkstemp(dir=path.parent, prefix='.settings-')
try:
    with os.fdopen(fd, 'w') as handle:
        json.dump(settings, handle, indent=2)
        handle.write('\n')
    os.chmod(temporary, 0o644)
    os.replace(temporary, path)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)
PY

test "$(gemini --version)" = "0.62.0"
