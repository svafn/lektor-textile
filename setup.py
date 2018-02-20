from setuptools import setup

setup(
    name='lektor-textile',
    description='Adds Textile markup support to Lektor (as standalone files).',
    version='0.2',
    author=u'Viktor Semenyuk',
    author_email='svafn1@gmail.com',
    url='http://github.com/svafn/lektor-textile',
    license='MIT',
    install_requires=[
        'textile'],
    py_modules=['lektor_textile'],
    entry_points={
        'lektor.plugins': [
            'textile = lektor_textile:TextilePlugin',
        ]
    }
)
