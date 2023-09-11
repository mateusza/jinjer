# Jinjer

Jinjer is a command-line tool that allows you to generate text or Markdown documents using Jinja2 templates. It provides a flexible way to populate templates with data from various sources, including command-line arguments, JSON input, files, and environment variables.

## Installation

You can install Jinjer using pip:

```bash
pip install jinjer
```

## Usage

To use Jinjer, you need to create a Jinja2 template file with placeholders for data. You can then provide data from various sources to fill in those placeholders.

Here's a basic example of how to use Jinjer:

```bash
jinjer template.j2 -s name John -n age 30 -o output.txt
```

In this example:

- `template.j2` is the Jinja2 template file.
- `-s` or `--str` is used to provide string data (`name`).
- `-n` or `--number` is used to provide numeric data (`age`).
- `-o` or `--output` specifies the output file (`output.txt`).

## Options

Jinjer supports the following options:

- `-s`, `--str`: Provide string data in the format `NAME VALUE`.
- `-n`, `--number`: Provide numeric data in the format `NAME NUMBER`.
- `-j`, `--argjson`: Provide JSON data in the format `NAME JSON_VALUE`.
- `-J`, `--json`: Provide a single JSON dictionary with all variables.
- `-f`, `--argfile`: Load data from a file in JSON, YAML, or TOML format.
- `-e`, `--envarg`: Load data from environment variables in the format `NAME ENV_VAR_NAME`.
- `-o`, `--output`: Specify the output file.

## Examples

### Fill in a Jinja2 template with string and numeric data:

```bash
jinjer template.j2 -s name John -n age 30 -o output.txt
```

### Use JSON input to fill in a template:

```bash
jinjer template.j2 -J '{"name": "Alice", "age": 25}' -o output.txt
```

### Load data from a JSON file:

```bash
jinjer template.j2 -f data.json -o output.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)

## Acknowledgments

This tool was developed with the valuable assistance of ChatGPT by OpenAI, which provided guidance and code suggestions.

## Authors

- Mateusz Adamowski
