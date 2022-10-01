from behave import given, when, then


@given(u'La app esta iniciada')
def step_app_iniciada(context):
    pass


@when(u'Realizo un Ping')
def step_do_ping(context):
    context.response = context.client.get('/ap1/v1/ping')


@then(u'Recibo un mensaje "{}"')
def step_assert_message_contains(context, message_content):
    assert message_content in context.response.json()['message']
