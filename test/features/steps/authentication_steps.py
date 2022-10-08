from behave import given, when, then
from src.conf.config import Settings
import requests
from jose import jwt

USERS_URI = 'http://service-users:35002/api/v1/users'


@given(u'A user with email "{email}" and password "{password}" exists')
def step_create_user(context, email, password):
    user = {
        "username": email,
        "first_name": "fname",
        "last_name": "lname",
        "email": email,
        "password": password,
        "wallet": "wallet"
    }
    response = requests.post(USERS_URI, json=user)
    assert response.status_code == 201


@when(u'I try to authenticate with email "{email}" and password "{password}"')
def step_do_authentication(context, email, password):
    response = context.client.post(
        Settings().API_V1_STR + '/auth/token',
        json={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 201
    context.vars['token'] = response.json()['token']


@then(u'The authentication is successful for email "{email}"')
def step_impl(context, email):
    # TODO: Decode JWT here with secret. ¿Model class or plain jose?
    decoded = jwt.decode(context.vars['token'], Settings().JWT_SECRET)
    obtained_subject = decoded['sub']
    assert obtained_subject == email
