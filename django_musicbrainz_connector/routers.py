class DjangoMusicBrainzConnectorDatabaseRouter:
    """
    Django database router that routes all database access requests to the MusicBrainz database.
    """

    APP_LABEL = "django_musicbrainz_connector"

    def db_for_read(self, model, **hints):
        return "musicbrainz_db" if model._meta.app_label == self.APP_LABEL else None

    def db_for_write(self, model, **hints):
        """
        Return the database that will be used for write operations. We protect the database from write operations
        elsewhere in the code, but not here. Returning anything except the actual database name here breaks the Admin
        interface.
        """
        return "musicbrainz_db" if model._meta.app_label == self.APP_LABEL else None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == self.APP_LABEL and obj2._meta.app_label == self.APP_LABEL:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.APP_LABEL:
            return False
        return None
