import pytest
import yaml

from click.testing import CliRunner

import secret_injector

from secret_injector.cli import secret_injector_cli


@pytest.fixture
def input_yaml_docker_compose():
    with open('tests/files/docker-compose.yml', 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture
def output_yaml_docker_compose():
    with open('tests/files/docker-compose-secret.yml', 'r') as f:
        return yaml.safe_load(f)

@pytest.fixture
def configure_local_secret(tmpdir, monkeypatch):
    project_name = 'test_project_name'
    local_secret_dir = tmpdir.mkdir('test_secret_dir')
    local_secret_dir_path = str(local_secret_dir)

    secret_file = local_secret_dir.join(project_name)

    secrets = ['SECRET_1=FIRST_VALUE\nSECRET_2=SECOND_VALUE']
    for secret in secrets:
        secret_file.write_text(secret, encoding='utf-8')

    monkeypatch.setattr(
        secret_injector.runner,
        'DEFAULT_PROJECT_NAME',
        project_name,
    )

    monkeypatch.setattr(
        secret_injector.local_backend,
        'DEFAULT_SECRET_DIR',
        local_secret_dir_path,
    )

    return secret_file

def test_e2e_cli_secret_injector(input_yaml_docker_compose, output_yaml_docker_compose, tmpdir, configure_local_secret):
    """Ensure that the output generated by the CLI matches our desired."""
    test_dir = tmpdir.mkdir('cli_test')
    f_input = test_dir.join('docker-compose.yml')
    f_input.write(input_yaml_docker_compose)
    f_output = test_dir.join('docker-compose-secret.yml')
    test_dir.chdir()

    runner = CliRunner()
    cli_args = []
    result = runner.invoke(secret_injector_cli, cli_args)
    assert result.exit_code == 0, result.exc_info
    assert result.output == 'Hello World!\n'
    assert yaml.safe_load(f_output.read_text(encoding='utf-8')) == output_yaml_docker_compose

