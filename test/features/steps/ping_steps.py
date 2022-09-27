from behave import given, when, then

@given(u'La app esta iniciada')
def step_impl(context):
    pass


@when(u'Realizo un Ping')
def step_impl(context):
    context.response = context.client.get('/ping')


@then(u'Recibo un mensaje "{}"')
def step_impl(context, message_content):
    assert message_content in context.response.json()['message']
