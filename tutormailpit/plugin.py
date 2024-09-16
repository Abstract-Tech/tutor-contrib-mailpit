import os
import typing as t
from glob import glob

import importlib_resources
from tutor import hooks as tutor_hooks

config: dict[str, dict[str, t.Any]] = {
    "overrides": {
        "SMTP_HOST": "mailpit",
        "SMTP_PORT": "1025",
    },
}

# Add configuration entries
tutor_hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)

# Load patches from files
for path in glob(str(importlib_resources.files("tutormailpit") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read())
        )
