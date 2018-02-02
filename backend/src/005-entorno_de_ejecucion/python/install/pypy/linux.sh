sudo apt-get install wget
echo "Installing Pypy3.5 in your system..."
wget https://bitbucket.org/squeaky/portable-pypy/downloads/pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
tar xvf pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
rm pypy3.5-5.10.1-linux_x86_64-portable.tar.bz2
sudo mv pypy3.5-5.10.1-linux_x86_64-portable /usr/lib/pypy3.5
sudo ln -s /usr/lib/pypy3.5/bin/pypy3.5 /usr/bin/pypy3.5
echo "Pypy3.5 was installed sucessfully. Execute pypy3.5 to inicialize it."