import yaml
import time

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(site, select_input_login, select_input_password, select_input_button, select_error):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_input_button)
    btn.click()
    err_label = site.find_element('xpath', select_error)
    print(err_label.text)
    assert err_label.text == '401'


def test_step2(site, select_input_login, select_input_password, select_input_button, check_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()
    hello_message = site.find_element('xpath', check_hello_user)
    assert hello_message.text == f'Hello, {testdata["login"]}'


def test_step3(site, select_input_login, select_input_password, select_input_button, check_hello_user,
               create_post_button, enter_title_field, enter_desc_field, enter_content_field, save_post_button,
               post_title):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(testdata['login'])
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(testdata['password'])
    btn = site.find_element('css', select_input_button)
    btn.click()

    btn2 = site.find_element('xpath', create_post_button)
    btn2.click()
    time.sleep(testdata['sleep_time'])

    input_title = site.find_element("xpath", enter_title_field)
    input_title.send_keys(testdata['title'])
    input_description = site.find_element("xpath", enter_desc_field)
    input_description.send_keys(testdata['description'])
    input_content = site.find_element("xpath", enter_content_field)
    input_content.send_keys(testdata['content'])

    btn3 = site.find_element('xpath', save_post_button)
    btn3.click()
    time.sleep(testdata['sleep_time'])

    check_post = site.find_element('xpath', post_title)
    #print(check_post.text)
    assert check_post.text == f'{testdata["title"]}'

