from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

setup(
    name='sphinx-stackoverflowsearch',
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[],
    package_data={
        'sphinx-stackoverflowsearch': [
            'static/sphinx-stackoverflowsearch.js',
            'templates/search.html'
        ]
    }
)
