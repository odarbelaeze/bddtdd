from behave import when, then


@when(u'i visit the homepage')
def i_visit_the_homepage(context):
    context.browser.get('http://localhost:8000/')


@then(u'i should see "{text}" in the title')
def i_see_text_in_title(context, text):
    assert text in context.browser.title
