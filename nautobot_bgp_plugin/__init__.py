from extras.plugins import PluginConfig
from .version import __version__


class BGPConfig(PluginConfig):
    name = "nautobot_bgp_plugin"
    verbose_name = "BGP"
    description = "Subsystem for tracking bgp related objects"
    version = __version__
    author = "Nikolay Yuzefovich"
    author_email = "mgk.kolek@gmail.com"
    base_url = "bgp"
    required_settings = []
    min_version = "3.2.0"
    max_version = "3.2.99"
    default_settings = {"device_ext_page": "right", "asdot": False}


config = BGPConfig  # noqa
