import os
from secret_injector import local_backend
from secret_injector import yamlenv_engine


DEFAULT_INPUT_FILENAME='docker-compose.yml'
DEFAULT_OUTPUT_FILENAME='docker-compose-secret.yml'
DEFAULT_PROJECT_NAME=os.path.basename(os.getcwd())


def run_secret_injector(*args, input_file: str = None, output_file: str = None, **kwargs) -> None:
    """Inject secrets into a given template file."""
    input_file = input_file or DEFAULT_INPUT_FILENAME
    output_file = output_file or DEFAULT_OUTPUT_FILENAME
    secrets = local_backend.retrieve_secrets(project_name=DEFAULT_PROJECT_NAME)
    yamlenv_engine.inject(
                        input_file=input_file,
                        output_file=output_file,
                        secrets=secrets,
                    )

