#!/bin/sh

nodetool -h localhost compact templates
nodetool -h localhost compact articles

