try:
    from config.config import __token__, __prefix__, __guild_name__
except ImportError:
    import os
    __token__ = os.environ.get('DISCORD_TOKEN')
    __prefix__ = os.environ.get('DISCORD_PREFIX')
    __guild_name__ = os.environ.get('DISCORD_GUILD_NAME')

