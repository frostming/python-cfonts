.. python-cfonts documentation master file, created by
   sphinx-quickstart on Sat Jun 23 12:44:15 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CFonts: Sexy fonts for the console
==================================

.. image:: https://img.shields.io/pypi/v/python-cfonts.svg
    :target: https://pypi.python.org/pypi/python-cfonts

.. image:: https://img.shields.io/pypi/l/python-cfonts.svg
    :target: https://pypi.python.org/pypi/python-cfonts

.. image:: https://img.shields.io/pypi/pyversions/python-cfonts.svg
    :target: https://pypi.python.org/pypi/python-cfonts

.. image:: /_static/images/example.png
    :target: _static/images/example.png

This is a Python port of `@dominikwilkowski's cfonts <https://github.com/dominikwilkowski/cfonts>`_. Thanks for the original code and beautiful console fonts!

    *This project supports Python >= 3.6 ONLY.*

Installation
------------

**Recommended way:** use `pipsi <https://pypi.org/project/pipsi/>`_::

  pipsi install python-cfonts

Or alternatively, install using Pip::

  pip install python-cfonts


Command Line Interface
----------------------

.. click:: cfonts.cli:cli
    :prog: cfonts

Examples
++++++++

.. image:: /_static/images/demos.png
    :target: _static/images/demos.png

API References
--------------

.. module:: cfonts

.. autofunction:: render
.. autofunction:: say
