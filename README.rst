Build ffmpeg with visualc++ express and statically link with your own app
=========================================================================

Make sure you have visualc++ express git, python and bakefile

Open a cmd shell in this dir and run

.. code-block:: bash

    bootstrap.bat

Answer the questions given

Make sure you install MinGW with make

Once the msys shell is started

.. code-block:: bash

    alias # to see the provided utils

    movelink # to use the correct link

    fconfigure # to run configure with the correct flags, this takes time
    
    make 

To build the provided small app

In msys shell

.. code-block:: bash

    movealib
    
    c99convh

Open a cmd shell in the mypeg dir

.. code-block:: bash

    bkl mypeg.bkl

Open the sln in vs201xand build