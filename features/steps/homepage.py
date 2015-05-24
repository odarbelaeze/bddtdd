from behave import when, then


def get_url(name=None):
    return 'http://localhost:8000' + (name or '/')


@when(u'i visit the homepage')
def i_visit_the_homepage(context):
    context.browser.get(get_url())


@then(u'i should see "{text}" in the title')
def i_see_text_in_title(context, text):
    assert text in context.browser.title


@then(u'i should see a pink title')
def step_impl(context):
    title = context.browser.find_element_by_tag_name('h1')
    assert 'rgba(200, 50, 255, 1)' == title.value_of_css_property('color')
