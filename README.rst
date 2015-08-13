RTL APT
=======

.. code:: bash

    convert -size 2080x2080 -depth 32 -define quantum:format=floating-point gray:test.wav.dat test.png

    ./toimg.py test.wav.dat test.pgm
