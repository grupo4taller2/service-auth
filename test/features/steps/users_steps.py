from behave import given, when, then
from src.conf.config import Settings


@given(u'There are {:d} tipitos')
def step_add_n_tipitos(context, n_tipitos):
    for i in range(n_tipitos):
        context.client.post(
            Settings().API_V1_STR + '/tipitos',
            json={
                "name": f'tipito_{i}'
                }
        )


@when(u'I create the tipito "{}"')
def step_create_tipito(context, name):
    context.client.post(
        Settings().API_V1_STR + '/tipitos',
        json={
            "name": f'{name}'
            }
    )


@then(u'The tipito "{}" exists in the platform')
def step_impl(context, name):
    response = context.client.get(
        f'{Settings().API_V1_STR}/tipitos/{name}'
    )
    assert response.json()['name'] == name
