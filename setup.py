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

lines = ['listen=NO\n','listen_ipv6=YES\n','anonymous_enable=NO\n',
         'local_enable=YES\n', 'dirmessage_enable=YES\n','use_localtime=YES\n',
         'xferlog_enable=YES\n', 'connect_from_port_20=YES\n',
         'secure_chroot_dir=/var/run/vsftpd/empty\n', 'pam_service_name=vsftpd\n',
         'rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\n',
         'rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\n',
         'ssl_enable=NO\n']

with open("/jupyternootebook/vsftpd.conf", 'w') as file:
    file.writelines(lines)

file.close()
