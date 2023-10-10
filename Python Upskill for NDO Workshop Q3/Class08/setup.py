from setuptools import setup, find_packages

with open('requirements.txt', 'r') as req:
    requirements = req.readlines()
requirements = [req.replace('\n', '') for req in requirements]
#print(requirements)
setup(name='ericsson_pkg',
      version='0.0.1',
      description = "This is my package",
      author = "Paul Kevin Rengifo Sandoval",
      author_email = "paul.rengifo.sandoval@ericsson.com",
      packages = find_packages(),
      install_requires=requirements
)