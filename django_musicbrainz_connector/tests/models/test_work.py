import pytest

from django_musicbrainz_connector.models import Recording, Work


@pytest.mark.django_db
def test_work_str():
    work = Work.objects.get(id=11432290)
    assert str(work) == "Η αχάριστη"


@pytest.mark.django_db
def test_work_musicbrainz_url():
    work = Work.objects.get(id=11432290)
    assert work.musicbrainz_url == "https://musicbrainz.org/work/fe4f5295-4d0f-32bd-8029-743f740d31f1"


@pytest.mark.django_db
def test_work_recordings():
    work = Work.objects.get(id=11432290)
    recording = Recording.objects.get(id=13679939)

    assert work.recordings == [recording]
