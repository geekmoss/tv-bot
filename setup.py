from setuptools import setup


with open("README.md", 'r') as f:
    long_description = f.read()


setup(
    name='TvBot',
    version='1.0.1',
    description='TVBot resolves bookmark rotation, through Selenium, for presentation on television.',
    author='Jakub Janeček',
    author_email='jakub.janecek@fw-fw.cz',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/geekmoss/tv-bot',
    install_requires=['Click', 'selenium', 'Flask', 'Flask-SocketIO', 'eventlet'],
    scripts=['scripts/tvbot-cli', 'scripts/tvbot-tv', 'scripts/tvbot-socket-server'],
    packages=['TvBot'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
