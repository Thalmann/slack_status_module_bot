from datetime import datetime
import simplejson
from httplib2 import Http, ServerNotFoundError

from private_channels import test_channel_webhook_url


def post_to_slack_channel(channel_webhook_url, message):
    http = Http()

    post_data = {'text': message}
    headers = {'Content-type': 'application/json'}

    try:
        response, content = http.request(
            channel_webhook_url,
            'POST',
            simplejson.dumps(post_data),
            headers=headers,
        )
    except ServerNotFoundError:
        # Network Error - try again
        response, content = post_to_slack_channel(channel_webhook_url, message)

    # handle if fails?
    print(response)
    print(content)

    return response, content


class Module():

    recurring_in_seconds = NotImplementedError
    action = NotImplementedError

    def __init__(self):
        self.last_run = datetime.min

    def run(self):
        self.action()
        self.last_run = datetime.now()

    def should_run(self):
        since_last_run = datetime.now() - module.last_run
        return since_last_run.total_seconds() > self.recurring_in_seconds


class HelloWorld(Module):

    recurring_in_seconds = 10

    def action(self):
        post_to_slack_channel(test_channel_webhook_url, 'Hello World!')


modules = [HelloWorld()]
try:
    while True:
        for module in modules:
            if module.should_run():
                module.run()
except Exception as error:
    print('Failed due to: ', error)
