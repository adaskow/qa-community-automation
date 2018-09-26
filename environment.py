from datetime import datetime

from selenium import webdriver


def setup_browser(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--no-sandbox')

    context.browser = webdriver.Chrome(options=chrome_options)


def before_feature(context, feature):
    setup_browser(context)


def after_step(context, step):
    if step.status == 'failed':
        now = datetime.now().strftime('%A_%H:%M:%S')
        context.browser.get_screenshot_as_file(
            'screenshots/{date}_{file_name}_line_{line}-{name}.png'.format(
                file_name=step.filename.split('/')[-1],
                line=step.line,
                date=now,
                name=step.name
            )
        )
        context.feature.skip()


def after_feature(context, feature):
    context.browser.quit()
