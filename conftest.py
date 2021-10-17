import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose languages'
    )


@pytest.fixture(scope="session")
def browser(request):
    options = Options()
    user_language = request.config.getoption('language')
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(
        executable_path='/Users/antonzimaev/Downloads/chromedriver-1',
        options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.close()
    browser.quit()