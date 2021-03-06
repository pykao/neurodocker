"""Tests for neurodocker.interfaces.SPM"""

from neurodocker.interfaces.tests import utils


class TestSPM(object):

    def test_docker(self):
        specs = {
            'pkg_manager': 'apt',
            'instructions': [
                ('base', 'ubuntu:18.04'),
                ('spm12', {'version': 'dev'}),
                ('user', 'neuro'),
            ],
        }

        bash_test_file = "test_spm12.sh"
        utils.test_docker_container_from_specs(
            specs=specs, bash_test_file=bash_test_file)

    def test_singularity(self):
        specs = {
            'pkg_manager': 'apt',
            'instructions': [
                ('base', 'docker://ubuntu:16.04'),
                ('spm12', {'version': 'r7219'}),
                ('user', 'neuro'),
            ],
        }

        bash_test_file = "test_spm12.sh"
        utils.test_singularity_container_from_specs(
            specs=specs, bash_test_file=bash_test_file)
