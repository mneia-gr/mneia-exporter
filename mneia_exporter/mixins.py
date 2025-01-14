import json
from pathlib import Path
from typing import Dict

from django.utils.text import slugify


class Exportable:
    @property
    def export_dir(self) -> Path:
        return Path.home() / "Mneia" / "mneia-data" / f"{slugify(self._meta.verbose_name_plural)}"

    @property
    def export_file(self) -> Path:
        return self.export_dir / f"{self.id}.json"

    @property
    def _as_json(self) -> Dict:
        return {
            "id": str(self.id),
            "created_in_mneia": str(self.created_in_mneia),
            "updated_in_mneia": str(self.updated_in_mneia),
        }

    def export(self):
        self.export_dir.mkdir(parents=True, exist_ok=True)
        self.export_file.write_text(json.dumps(self.as_json, indent=2))
