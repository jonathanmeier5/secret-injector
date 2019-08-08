import os
import yaml

import yamlenv


def inject(input_file: str = None, output_file: str = None, secrets: dict = None) -> None:
    """
    Function that takes an input template, injects secrets into it,
    and writes the interpolated result to an output file.
    """

    for k, v in secrets.items():
        os.environ[k] = v
    with open(input_file, 'r') as f_in:
        interpolated_template = yamlenv.load(f_in.read())
        with open(output_file, 'w') as f_out:
            f_out.write(yaml.dump(interpolated_template))
