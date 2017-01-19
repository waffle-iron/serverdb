from setuptools import find_packages, setup



setup(
    name='serverdb',
    version='0.0.1',
    author='Andrew Waggy',
    author_email='jwaggy@endstech.com',
    description='Making a gui utility for what I normally have to stare into the void for',
    install_requires=[
	'tkinter',
	'pymysql',
        'codacy-coverage',
		     ],
    classifiers=[
        'Development Status :: Pre-Alpha',
        'Intended Audience :: Employees',
        'License :: OSI Approved :: GNU Affero General Public License v3 (GAGPLv3)',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/jwaggy/serverdb',
    license='GAGPL-3.0',
    packages=find_packages(),
)
