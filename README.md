[![Build Status](https://travis-ci.com/pmav99/ansible-role-install_grass.svg?branch=master)](https://travis-ci.com/pmav99/ansible-role-install_grass)

install_grass
=============

An ansible role for installing GRASS GIS on Ubuntu 16.04 & 18.04 and Fedora 28 & 29

The role also installs the latest Python 2 version and R

Quickstart
----------

    ansible-galaxy install pmav99.install_grass
    curl https://raw.githubusercontent.com/pmav99/ansible-role-install_grass/master/sample_playbook.yml -o install_grass.yml
    ansible-playbook install_grass.yml --ask-become

Install the role
----------------

You can install the role by using:

    ansible-galaxy install pmav99.install_grass

Example Playbook
----------------

If you want to install grass locally you can use the following playbook:

    - hosts: 127.0.0.1
      connection: local
      roles:
         - role: pmav99.install_grass
         
You can also download it with:

    wget https://raw.githubusercontent.com/pmav99/ansible-role-install_grass/master/sample_playbook.yml -O playbook.yml

License
-------

MIT
