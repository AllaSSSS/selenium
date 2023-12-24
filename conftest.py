import pytest
import yaml
from module import Site

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def select_input_login():
    return '''//*[@id="login"]/div[1]/label/input'''


@pytest.fixture()
def select_input_password():
    return '''//*[@id="login"]/div[2]/label/input'''


@pytest.fixture()
def select_input_button():
    return 'button'


@pytest.fixture()
def select_error():
    return '''//*[@id="app"]/main/div/div/div[2]/h2'''


@pytest.fixture()
def check_hello_user():
    return '''//*[@id="app"]/main/nav/ul/li[3]/a'''


@pytest.fixture()
def create_post_button():
    return '''//*[@id="create-btn"]'''


@pytest.fixture()
def enter_title_field():
    return '''//*[@id="create-item"]/div/div/div[1]/div/label'''


@pytest.fixture()
def enter_desc_field():
    return '''//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'''


@pytest.fixture()
def enter_content_field():
    return '''//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'''


@pytest.fixture()
def save_post_button():
    return '''// *[ @ id = "create-item"] / div / div / div[7] / div / button / span'''


@pytest.fixture()
def post_title():
    return '''//*[@id="app"]/main/div/div[1]/h1'''


@pytest.fixture()
def site():
    site_class = Site(testdata['address'])
    yield site_class
    site_class.close()

