## Kernels en IPython

### Añadir kernel Javascript a IPython
```sh
cd /usr/local/share/jupyter/kernels
sudo git clone https://github.com/minrk/jskernel
```

>Fuente: https://github.com/minrk/jskernel

### Añadir kernel Golang a IPython
```sh
go get golang.org/x/tools/cmd/goimports
sudo apt-get install libzmq3-dev
go get -tags zmq_4_x github.com/gopherds/gophernotes
mkdir -p ~/.local/share/jupyter/kernels/gophernotes
cp -r $GOPATH/src/github.com/gopherds/gophernotes/kernel/* ~/.local/share/jupyter/kernels/gophernotes
```

>Fuente: https://github.com/gopherdata/gophernotes

_________________________________

### Acceso a los kernels de IPython (en Linux)

`cd /usr/local/share/jupyter/kernels`

>Fuente: http://jupyter.readthedocs.io/en/latest/projects/jupyter-directories.html