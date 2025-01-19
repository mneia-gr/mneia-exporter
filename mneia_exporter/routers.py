from mneia_exporter.apps import MneiaExporterConfig


class MneiaExporterDatabaseRouter:
    """
    We export some data from the Mneia database, which is the default one in our Django project, but we also export some
    data from the MusicBrainz database using the Django MusicBrainz Connector. This database query router sends database
    queries to the appropriate database.
    """

    def db_for_read(self, model, **hints):
        return (
            "musicbrainz_db"
            if model._meta.app_label == MneiaExporterConfig.name and model.__name__.startswith("MusicBrainz")
            else None
        )

    def db_for_write(self, model, **hints):
        """
        Return the database that will be used for write operations. We protect the database from write operations
        elsewhere in the code, but not here. Returning anything except the actual database name here breaks the Admin
        interface.
        """
        return (
            "musicbrainz_db"
            if model._meta.app_label == MneiaExporterConfig.name and model.__name__.startswith("MusicBrainz")
            else None
        )

    def allow_relation(self, obj1, obj2, **hints):
        """
        There are no relations to or from the exporter models, they are all proxy models.
        """
        if obj1._meta.app_label == MneiaExporterConfig.name or obj2._meta.app_label == MneiaExporterConfig.name:
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == MneiaExporterConfig.name:  # no migrations needed for mneia_exporter
            return False
        return None
