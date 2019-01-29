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


post_to_slack_channel(test_channel_webhook_url, 'hey')
