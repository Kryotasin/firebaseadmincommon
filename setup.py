from distutils.core import setup
setup(
  name = 'firebaseadmincommon',         # How you named your package folder (MyLib)
  #packages = ['djangofirebaseadmin'],   # Chose the same as "name"
  version = '0.5.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Package to wrap Firebase Admin with Python.',   # Give a short description about your library
  author = 'Kshitij Sinha',                   # Type in your name
  author_email = 'kshitij.sinha94@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Kryotasin/firebaseadmincommon',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Kryotasin/firebaseadmincommon/archive/0.5.1.tar.gz',    # I explain this later on
  keywords = ['Python', 'firebase', 'admin'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'firebase_admin',
          'google-cloud',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.5',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)