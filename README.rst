Web de Alberto Vara
-------------------
.. image:: https://travis-ci.org/avara1986/avara.svg?branch=master
    :target: https://travis-ci.org/avara1986/avara

Proyecto con Django y Google App Engine.

Puedes contactar conmigo en a.vara.1986@gmail.com


Installation
============

    sudo apt-get install dpkg-dev virtualbox-dkms

    wget http://files.vagrantup.com/packages/0219bb87725aac28a97c0e924c310cc97831fd9d/vagrant_1.2.4_i686.deb

    agrant box add hashicorp/precise64

    vagrant init

    git clone https://github.com/avara1986/avara .s

    vagrant up

## Setting up the virtual machine development environment

SSH into the virtual machine:

	vagrant ssh

The source code is shared with the virtual machine in this directory:

	cd avara

Always run the following command to use the proper python virtual environment:

	workon vavara

Install the required python packages:

	./install_deps.py (this will pip install requirements, and download the App Engine SDK)

You can now start the development web server:

	./manage.py runserver 192.168.100.3:8000

Access this URL:

* [http://192.168.100.3:8000](http://192.168.100.3:8000)