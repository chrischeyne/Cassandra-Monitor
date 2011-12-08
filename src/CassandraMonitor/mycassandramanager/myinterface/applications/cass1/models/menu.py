response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [

(T('Cass Mgr'),URL('cass_mgr','index')==URL(),URL('cass_mgr','index'),[]),
(T('Cass Perf'),URL('default','index')==URL(),URL('cass_perf','index'),[]),
(T('Cass Stat'),URL('cass_internals','index')==URL(),URL('cass_internals','index'),[]),
(T('MySQL Mgr'),URL('internals','index')==URL(),URL('mysql_mgr','index'),[]),
(T('MySQL Int'),URL('internals','index')==URL(),URL('mysql_perf','index'),[]),
(T('Hadoop'),URL('internals','index')==URL(),URL('hadoop','index'),[]),
(T('STORM'),URL('internals','index')==URL(),URL('storm','index'),[]),
]
