# -*- coding: utf-8 -*-

import rpyc

if __name__ == "__main__":
    # Necesitas correr el servidor en la siguiente dirección y puerto
    c = rpyc.connect("192.168.1.12", 18861)
    print(dir(c.root))

    # Podemos acceder a los métodos y propiedades expuestos:
    print(c.root.get_answer())            # 42
    print(c.root.the_real_answer_though)  # 43
    
    # Debemos empezar la propiedad o método con `exposed_` o no
    #   se expondrán ni podremos acceder:
    # print(c.root.get_question()) 
    """
    ======= Remote traceback =======
    ...
      File "/home/tomer/workspace/rpyc/core/protocol.py", line 298, in sync_request
        raise obj
    AttributeError: cannot access 'get_question'
    """

