import setuptools

setuptools.setup(name='mmb_test_helpers',
      version='0.2',
      description='mapmybook test helpers',
      url='http://github.com/zimmicz/map-my-book-test-helpers',
      author='Michal Zimmermann',
      author_email='zimmi@tutanota.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=['flask', 'requests', 'psycopg2'],
      zip_safe=False)

