import uuid
from typing import Literal


def get_musicbrainz_identifier_type(identifier: str | int) -> Literal["gid", "name", "id"]:
    """
    MusicBrainz entities can be identified by their ID, which is typically an integer. Entities that also have GIDs,
    which are UUIDs, can be identified by those as well. Some entities can also identified by their names, such as
    Area Types, Artist Types, Work Types.

    This function tries to determine the type of the identifier. It makes no guarantee that you will be able to get
    an object. For example, if you try to identify a Release by name, you will most likely get multiple results, which
    is not what you want. Use wisely.
    """
    try:
        uuid.UUID(identifier)  # is it a UUID?
    except (ValueError, AttributeError):
        pass  # it's not a UUID
    else:
        return "gid"  # it's a UUID

    try:
        int(identifier)  # is it an integer?
    except ValueError:
        return "name"  # it's not an integer
    else:
        return "id"  # it's an integer
