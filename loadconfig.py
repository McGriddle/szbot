try:
    from config.config import __token__, __prefix__, __guild_name__, __imgflip_username__, __imgflip_password__
except ImportError:
    import os
    __token__ = os.environ.get('DISCORD_TOKEN')
    __prefix__ = os.environ.get('DISCORD_PREFIX')
    __guild_name__ = os.environ.get('DISCORD_GUILD_NAME')
    __imgflip_username__ = os.environ.get('IMGFLIP_USERNAME')
    __imgflip_password__ = os.environ.get('IMGFLIP_PASSWORD')

