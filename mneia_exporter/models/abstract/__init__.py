import datetime
from pathlib import Path

from django import template
from django.db import models
from django.utils.text import slugify


class ExportableManager(models.Manager):
    """
    Django model manager that adds some export functionality. This is meant to be used for exporting data from the
    MusicBrainz database, using the Django MusicBrainz Connector.
    """

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

        instances = self.all().order_by("id")
        if hasattr(self.model, "LIMIT_INSTANCES"):
            instances = instances[:self.model.LIMIT_INSTANCES]

        docs_export_file = self._get_docs_export_file()
        docs_export_file.write_text(
            docs_template.render(
                {
                    "today": datetime.datetime.now().strftime("%Y-%m-%d"),
                    "num_instances": self.count(),
                    "instances": instances,
                }
            )
        )


class Exportable(models.Model):
    """
    Abstract model that adds export functionality to models. This is meant to be used as a mix-in class.
    """

    exporter = ExportableManager()

    class Meta:
        abstract = True


class SampleExportable(models.Model):
    LIMIT_INSTANCES: int = 20
    exporter = ExportableManager()

    class Meta:
        abstract = True
