"""Example Load Platform integration -2."""
import voluptuous as vol

DOMAIN = 'example_load_platform2'

# 对configuration.yaml文件中该集成的配置格式要求
CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional('sensor'): vol.Schema(
                    {
                        # “name”在配置文件中是必须存在的（Required），否则报错，它的类型是字符串
                        vol.Required('name'): str,
                        # “value”在配置文件中可以没有（Optional），如果没有缺省值为28.88
                        vol.Optional('value', default=28.88): float
                    }),
            }),
    },
    extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Your setup of the integrate."""

    if config.get(DOMAIN):
        info = config[DOMAIN].get('sensor')
        if info:
            hass.helpers.discovery.load_platform('sensor', DOMAIN, info, config)

    return True