import ConfigParser

config = ConfigParser.RawConfigParser()

'''
* Change xxxx with your own values
'''

CONFIG_FOLDER = "xxxx\\config.ini" # Config path

config.add_section('tautulli_settings') # Section Name
config.set('tautulli_settings', 'apikey', 'xxxx') # Your Tautulli API key / Get it here http://localhost:8181/settings#tab_tabs-web_interface
config.set('tautulli_settings', 'url', 'http://localhost:8181/') # Your Tautulli URL

config.add_section('plex_settings') # Section Name
config.set('plex_settings', 'token', 'xxxx') # Your Plex TOEKN / How to find it https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/
config.set('plex_settings', 'url', 'http://localhost:32400') # Your Plex URL

config.add_section('email_settings') # Section Name
config.set('email_settings', 'name', 'xxxx') # Your name
config.set('email_settings', 'sender', 'xxxx') # From email address
config.set('email_settings', 'email_server', 'smtp.gmail.com') # Email server (Gmail: smtp.gmail.com)
config.set('email_settings', 'email_port', '25') # Email port (Gmail: 587)
config.set('email_settings', 'email_username', 'xxxx') # Your email username
config.set('email_settings', 'email_password', 'xxxx') # Your email password

# Writing our configuration file to 'CONFIG_FOLDER'
with open(CONFIG_FOLDER, 'wb') as configfile:
    config.write(configfile)
