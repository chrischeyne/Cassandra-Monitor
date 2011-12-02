response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [

(T('Cassandra Manager'),URL('cass_mgr','index')==URL(),URL('cass_mgr','index'),[]),
(T('Cassandra Performance'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Cassandra Internals'),URL('cass_internals','index')==URL(),URL('cass_internals','index'),[]),
(T('MySQL Manager'),URL('internals','index')==URL(),URL('internals','index'),[]),
(T('MySQL Performance'),URL('internals','index')==URL(),URL('internals','index'),[]),

]
