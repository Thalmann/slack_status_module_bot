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

    def __init__(self, recurring_in_seconds, action, kwargs):
        self.recurring_in_seconds = recurring_in_seconds
        self.action = action
        self.kwargs = kwargs
        self.last_run = datetime.min

    def run(self):
        self.action(**self.kwargs)
        self.last_run = datetime.now()

    def should_run(self):
        since_last_run = datetime.now() - module.last_run
        return since_last_run.total_seconds() > self.recurring_in_seconds


kwargs = dict(
    channel_webhook_url=test_channel_webhook_url,
    message='hey',
)
hey_module = Module(
    recurring_in_seconds=10, action=post_to_slack_channel, kwargs=kwargs)
modules = [hey_module]
try:
    while True:
        for module in modules:
            if module.should_run():
                module.run()
except Exception as error:
    print('Failed due to: ', error)
