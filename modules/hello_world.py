from private_channels import test_channel_webhook_url
from slack import post_to_slack_channel
from modules.module import Module


class HelloWorld(Module):

    recurring_in_seconds = 10

    def action(self):
        post_to_slack_channel(test_channel_webhook_url, 'Hello World!')
