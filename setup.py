from setuptools import setup, find_packages
setup(
    name='freeai-shell',
    version='0.1',
    description='No token limit, no waitlist, Free AI shell',
    author='piDack',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'websocket-client',
        'requests',
        'tls-client',
        'pypasser',
        'names',
        'colorama',
        'curl_cffi',
        'rich',
        'pydantic',
        'pyyaml',
        'typer[all]',
    ],
    dependency_links=[
        'file:aishell/ora#egg=ora'
        'file:aishell/quora#egg=quora'
    ],
    entry_points={
        'console_scripts': [
            'aia=aishell.__main__:cli_app'
        ]
    }
)