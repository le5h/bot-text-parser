# default

import re

import config

import services.search as search
import services.wolframalpha as wa

def query(query):
    if re.findall(config.NUMERIC_EXPRESSION, query): # if starts is equation
        answer = wa.query(query)
    else: answer = search.query(query)
    return "..." if not answer else answer
