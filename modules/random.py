from modules.module import Module
from slack import post_to_slack_channel
from private_channels import test_channel_webhook_url
import requests


class Random(Module):

    recurring_in_seconds = 60 * 60 * 9

    def action(self):
        response = requests.get('http://numbersapi.com/random/date')
        post_to_slack_channel(test_channel_webhook_url, response.content)
