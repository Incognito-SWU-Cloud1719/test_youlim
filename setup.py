from setuptools import setup, find_packages

f = open("vsftpd.conf", 'w')
f.write('listen=NO\n')
f.write('listen_ipv6=YES\n')
f.write('anonymous_enable=NO\n')
f.write('local_enable=YES\n')
f.write('dirmessage_enable=YES\n')
f.write('use_localtime=YES\n')
f.write('xferlog_enable=YES\n')
f.write('connect_from_port_20=YES\n')
f.write('secure_chroot_dir=/var/run/vsftpd/empty\n')
f.write('pam_service_name=vsftpd\n')
f.write('rsa_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem\n')
f.write('rsa_private_key_file=/etc/ssl/private/ssl-cert-snakeoil.key\n')
f.write('ssl_enable=NO\n')       
f.close()

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
      classifiers=[
          'License :: OSI Approved :: GNU License'
      ]
)

