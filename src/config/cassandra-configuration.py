import yaml

FIXME: place in cassandra-manager.yaml

document = """

    tornadoport:8181
    cassandrarpc:9160
    cassandrajmx:7199
    cassandrastorage:7000
    cassandra4x4j:7197


"""
configurationfile='cassandra-manager.yaml'

yaml.load(document)


