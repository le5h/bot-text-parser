# tests

import command

test_queries = [
    "DO magic", # abstract job
    "wiki dogo", # wiki
    "вики собака", # wiki
    "найди дереВо", # search
    "hoW is the weather", # weather
    "сколько будет 2x2", # ru wa
    "how much is 2x2" # en wa
]

def all():
    for query in test_queries:
        test(query)

def test(query):
    query = command.prepare(query)
    commands = command.parse_commands(query)
    top = command.top_command(commands)
    value = command.clear_commands(query)
    answer = command.service_query(top, value)
    print("\"" + query + "\" -> " + top + "(" + value + ") -> " + answer)
