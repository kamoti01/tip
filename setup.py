from setuptools import setup

setup(name='UsingSQLAlchemy', version='1.0',
      description='Code example demonstrating how to use SQLAlchemy in Python using Flask',
      author='cs group', author_email='ad09tkam@uwcad.it',
      url='http://www.github.com/kamoti01/tip',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask', 'flask-sqlalchemy',
                        #  'MySQL-python',
                        #  'pymongo',
                         # 'psycopg2',
      ],
     )
