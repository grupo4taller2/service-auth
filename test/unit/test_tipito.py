from src.domain.tipito import Tipito


def test_tipito_creation():
    tipito = Tipito(name='mateo')
    assert tipito.name == 'mateo'


def test_tipito_creation_with_empty_list_of_events():
    tipito = Tipito(name='mateo',
                    events=[])
    assert tipito.name == 'mateo'
