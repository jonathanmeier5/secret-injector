import os

DEFAULT_SECRET_DIR=os.path.expanduser('~/.secret-injector')


def retrieve_secrets(project_name: str = None) -> dict:
    """Function to retrieve secrets from our local backend and return as dict."""
    secret_dir = DEFAULT_SECRET_DIR
    os.makedirs(secret_dir, exist_ok=True)

    secret_file_path = '/'.join([secret_dir, project_name])
    secrets = dict()
    with open(secret_file_path, 'r') as f:
        for line in f.readlines():
            k, v = line.split('=')
            secrets[k] = v
    return secrets
