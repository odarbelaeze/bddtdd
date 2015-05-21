from selenium.webdriver.phantomjs import webdriver


def before_all(context):
    context.browser = webdriver.WebDriver()


def after_all(context):
    context.browser.quit()
