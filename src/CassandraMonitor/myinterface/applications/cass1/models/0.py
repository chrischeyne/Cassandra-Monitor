from gluon.storage import Storage
# FIXME: include myconfig/config.py
settings = Storage()
settings.migrate = True
settings.title = 'Cassandra Manager 0.0.14'
settings.subtitle = URL('static','logo.gif')
settings.author = 'chris'
settings.author_email = 'chris@cheynes.org'
settings.keywords = 'cassandra,bigdata,nosql'
settings.description = 'Test application 1'
settings.layout_theme = 'Oxidation'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '01930112-1abf-4fd9-a372-a318585ed8c7'
settings.email_server = 'localhost'
settings.email_sender = 'fp@games105linux.doomstuff.local'
settings.email_login = 'fp@doomstuff.local'
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
