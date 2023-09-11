#!/usr/bin/env python3

import argparse
from decimal import Decimal
import jinja2
import json
import toml
import yaml
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Argument Parser")

    parser.add_argument("template",
                        help="Required template argument")
    parser.add_argument("-o", "--output",
                        metavar="OUTPUT_FILE",
                        help="Output filename")
    parser.add_argument("-s", "--str",
                        nargs=2, action="append",
                        metavar=("NAME", "VALUE"),
                        help="Name-value pairs for -s or --str")
    parser.add_argument("-n", "--number",
                        nargs=2, action="append",
                        metavar=("NAME", "NUMBER"),
                        help="Name-number pairs for -n or --number")
    parser.add_argument("-j", "--argjson",
                        nargs=2, action="append",
                        metavar=("NAME", "JSON_VALUE"),
                        help="Name-JSON value pairs for -j or --argjson")
    parser.add_argument("-J", "--json",
                        metavar="JSON_DICT",
                        help="Single JSON dictionary with all variables")
    parser.add_argument("-f", "--argfile",
                        action="append",
                        metavar="FILENAME",
                        help="Filenames for -f or --argfile")
    parser.add_argument("-e", "--envarg",
                        nargs=2, action="append",
                        metavar=("NAME", "ENV_VAR_NAME"),
                        help="Name-Env Var Name pairs for -e or --envarg")
    args = parser.parse_args()
    return args

def decimal_type(value):
    try:
        return Decimal(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid Decimal value: {value}")


def load_data_from_args(parsed_args):
    data = {}
    
    arguments = parsed_args.str
    if arguments:
        for name, value in arguments:
            data[name] = value

    arguments = parsed_args.number
    if arguments:
        for name, value in arguments:
            data[name] = decimal_type(value)

    # Process the 'argjson' arguments
    json_arguments = parsed_args.argjson
    if json_arguments:
        for name, json_value in json_arguments:
            data[name] = json.loads(json_value)

    # Process the 'json' argument
    if parsed_args.json:
        data.update(json.loads(parsed_args.json))

    # Process the 'argfile' arguments
    file_arguments = parsed_args.argfile
    if file_arguments:
        for filename in file_arguments:
            data.update(load_data_from_file(filename))

    # Process the 'envarg' arguments
    env_arguments = parsed_args.envarg
    if env_arguments:
        for name, env_var_name in env_arguments:
            data[name] = os.environ.get(env_var_name, "")

    return data

def load_data_from_file(filename):
    _, file_extension = os.path.splitext(filename)

    load_functions = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
        '.toml': toml.load,
    }
    
    load_function = load_functions.get(file_extension, yaml.safe_load)
    
    with open(filename, 'r') as file:
        return load_function(file)

def render_template(template, data):
    try:
        rendered_template = template.render(data)
        return rendered_template
    except jinja2.exceptions.UndefinedError as e:
        print(e)
        sys.exit(1)

def main():
    parsed_args = parse_args()
    data = load_data_from_args(parsed_args)

    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(parsed_args.template)

    rendered_template = render_template(template, data)

    output_filename = parsed_args.output
    if output_filename:
        with open(output_filename, 'w') as output_file:
            output_file.write(rendered_template)
    else:
        print(rendered_template)

if __name__ == "__main__":
    main()
