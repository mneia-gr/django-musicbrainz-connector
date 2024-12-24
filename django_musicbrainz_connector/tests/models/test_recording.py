import pytest

from django_musicbrainz_connector.models import Recording, Work


@pytest.mark.django_db
def test_recording_str():
    recording = Recording.objects.get(id=13679939)
    assert str(recording) == "Αχάριστη"


@pytest.mark.django_db
def test_recording_musicbrainz_url():
    recording = Recording.objects.get(id=13679939)
    assert recording.musicbrainz_url == "https://musicbrainz.org/recording/fdb9d6f4-73f2-41f2-ba57-a8dbb65433a2"


@pytest.mark.django_db
def test_recording_recording_of():
    recording = Recording.objects.get(id=13679939)
    work = Work.objects.get(id=11432290)

    assert recording.recording_of == [work]
