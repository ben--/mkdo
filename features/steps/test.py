from behave import given

@given(u'we have behave installed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have behave installed')

@when(u'we implement 5 tests')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we implement 5 tests')

@then(u'behave will test them for us!')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then behave will test them for us!')
