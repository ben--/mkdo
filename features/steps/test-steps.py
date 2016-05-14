from behave import given

@given(u'an empty source directory')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a prompt in a source directory')

@when(u'the user runs "mkdo create build"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user runs "mkdo create build"')

@then(u'a "do/build" script is created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a "do/build" script is created')
