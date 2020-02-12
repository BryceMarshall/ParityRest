import factory

from homes.models import House


class HouseFactory(factory.django.DjangoModelFactory):
    """
    City factory to create cities for tests.
    """

    class Meta:
        model = House
        django_get_or_create = ('name',)

    name = 'TestHouse'
