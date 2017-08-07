from setuptools import setup

setup(name='gtkpass',
      version='0.1.1',
      description='A GTK+ 3 program for the standard unix password manager',
      url='http://github.com/raghavsub/gtkpass',
      auther='Raghav Subramaniam',
      author_email='raghavs511@gmail.com',
      license='MIT',
      packages=['gtkpass'],
      entry_points={'console_scripts': ['gtkpass=gtkpass.main:main']},
      install_requires=[])
