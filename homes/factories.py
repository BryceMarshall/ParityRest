import factory

from homes.models import House, Room


class HouseFactory(factory.django.DjangoModelFactory):
    """
    City factory to create cities for tests.
    """

    class Meta:
        model = House
        django_get_or_create = ('name',)

    name = 'TestHouse'
    id = factory.Sequence(lambda n: n)

class RoomFactory(factory.django.DjangoModelFactory):
    """
    City factory to create cities for tests.
    """

    class Meta:
        model = Room
        django_get_or_create = ('name',)

    name = 'TestRoom'
    id = factory.Sequence(lambda n: n)
    house = HouseFactory()
    current_temperature = 28
