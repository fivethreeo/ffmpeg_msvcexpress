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

    fconfigure # to run configure with the correct flags, this takes time
    
    make 

Open a cmd shell in the mypeg dir
