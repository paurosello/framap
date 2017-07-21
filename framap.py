import fnmatch
import os
import json
from graphviz import Digraph
import click

from styles import apply_styles, get_styles

excludes = ["test_", "chart_of_account"]

@click.command()
@click.argument('module_path')
@click.argument('output_path')
def gen_graph(module_path, output_path):
    matches = []
    for root, dirnames, filenames in os.walk(module_path):
        if "doctype" in root:
            for filename in fnmatch.filter(filenames, '*.json'):
                path = os.path.join(root, filename)
                if not any(x in path for x in excludes):
                    matches.append(path)

    graph = Digraph(format='pdf', comment='')

    for file in matches:
        with open(file, 'r') as json_file:
            json_doctype = json.loads(json_file.read())
            graph.node(json_doctype['name'])
            for field in json_doctype['fields']:
                if field["fieldtype"] in ['Table','Link']:
                    graph.edge(json_doctype['name'], field["options"], label=field["fieldname"])

    apply_styles(graph, get_styles()).render(output_path)

if __name__ == '__main__':
    gen_graph()