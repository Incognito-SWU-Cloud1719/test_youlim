from setuptools import setup, find_packages

setup(name='jupyternootebook',
      version='0.0.1',
      url='https://github.com/Incognito-SWU-Cloud1719',
      author='Cloud1719',
      description='Can use it to install sftp port service from Python.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      install_requires=['cython'],
      zip_safe=False,
      package_data={'*.conf': ['/jupyternootebook/*.conf']},
      include_package_data=True,
      classifiers=[
          'License :: OSI Approved :: GNU License'
      ],
)

f = open("vsftpd.conf", 'w')
f.close()

lines = ['listen=NO\n','listen_ipv6=YES\n','anonymous_enable=NO\n',
         'local_enable=YES\n']

with open("vsftpd.conf", 'w') as file:
    file.writelines(lines)

file.close()
