from modules.module import Module
from slack import post_to_slack_channel
from private_channels import test_channel_webhook_url
import pyowm
from private_keys import OPEN_WEATHER_MAP_API_KEY


class DailyWeather(Module):

    recurring_in_seconds = 60 * 60 * 24

    def action(self):
        owm = pyowm.OWM(OPEN_WEATHER_MAP_API_KEY)
        observation = owm.weather_at_place('Copenhagen,DK')
        w = observation.get_weather()
        temps = w.get_temperature('celsius')
        del temps['temp_kf']
        message = 'Temperature in Copenhagen: {}'.format(temps)
        post_to_slack_channel(
            test_channel_webhook_url, message)
