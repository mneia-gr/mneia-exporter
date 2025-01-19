import datetime
from pathlib import Path

from django import template
from django.db import models
from django.utils.text import slugify
from django_musicbrainz_connector.models.area_type import AreaType as _MusicBrainzAreaType
from django_musicbrainz_connector.models.work_type import WorkType as _MusicBrainzWorkType


class ExportableManager(models.Manager):
    def _get_docs_export_file(self) -> Path:
        return (
            Path.home()
            / "Mneia"
            / "django-musicbrainz-connector"
            / "docs"
            / "includes"
            / f"{slugify(self.model._meta.verbose_name_plural)}.md"
        )

    def _get_docs_export_template_file(self) -> Path:
        return Path("mneia_exporter") / f"{slugify(self.model._meta.verbose_name_plural)}.md"

    def export_docs(self) -> None:
        docs_template_file = self._get_docs_export_template_file()
        docs_template = template.loader.get_template(docs_template_file)

        docs_export_file = self._get_docs_export_file()
        docs_export_file.write_text(
            docs_template.render(
                {
                    "today": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "num_instances": self.count(),
                    "instances": self.all().order_by("id"),
                }
            )
        )


class Exportable(models.Model):
    exporter = ExportableManager()

    class Meta:
        abstract = True


class MusicBrainzAreaType(_MusicBrainzAreaType, Exportable):
    class Meta:
        verbose_name_plural = "Area Types"
        proxy = True


class MusicBrainzWorkType(_MusicBrainzWorkType, Exportable):
    class Meta:
        verbose_name_plural = "Work Types"
        proxy = True
