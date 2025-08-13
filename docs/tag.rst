Tag
===

All primary entities but the genre and URL (i.e. area, artist, event, instrument, label, place, recording, release, release group, series and work) have ``*_tag`` and ``*_tag_raw`` tables, with the same structure.
These tables contain two foreign keys, linked to the associated entity and to the tag table.
The ``*_tag_raw`` tables contain a foreign key, editor, which specifies who added the tag, while the ``*_tag`` tables instead contain a count of how many times a tag is applied to a particular entity, and a last_updated timestamp.
For privacy reasons, the ``*_tag_raw`` tables aren't included in the database dumps. The tag table contains the actual names of the tags, and a ``ref_count`` indicating how often the tag has been used.

.. automodule:: django_musicbrainz_connector.models.tag
   :noindex:

Model Documentation
-------------------

.. autoclass:: django_musicbrainz_connector.models.tag::Tag

.. autoclass:: django_musicbrainz_connector.models.base_tag_model::TagModel

Model Source
------------

Tag
***

.. literalinclude:: ../django_musicbrainz_connector/models/tag.py
   :pyobject: Tag
..    :caption: The `tag` Model

TagModel
********

.. literalinclude:: ../django_musicbrainz_connector/models/base_tag_model.py
   :pyobject: TagModel
..    :caption: The `tagmodel` Model


Dynamic model creation for tagged table
***************************************

.. literalinclude:: ../django_musicbrainz_connector/apps.py
..    :caption: Dynamic model creation for tagged table
