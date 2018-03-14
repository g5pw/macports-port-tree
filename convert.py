#!/usr/bin/env python3

from json import load as json_load
from argparse import ArgumentParser, FileType
import re

import jinja2

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("portindex", help="Path to the portindex.json file.",
                        type=FileType())
    parser.add_argument("--port", help="Only specify a single port to generate.",
                        type=str)

    args = parser.parse_args()

    ports = json_load(args.portindex)

    # create Jinja2 template environment with the link to the current directory
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(searchpath="templates/"),
        trim_blocks=True,
        lstrip_blocks=True)

    port_template = env.get_template("port.html")

    for port in ports:
        if args.port and args.port != port["name"]:
            continue

        port["maintainers"] = re.findall(r"{.*}|\w+", port["maintainers"])

        port_filename = "_output/{}.html".format(port["name"].lower())

        print("Generating " + port_filename)

        with open(port_filename, mode="w") as port_html_file:
            port_html_file.write(port_template.render(port=port))
