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

    *This project supports Python 2.7+ and 3.5+*

Installation
------------

**Recommended way:** use `pipx <https://pypi.org/project/pipx/>`_::

  $ pipx install python-cfonts

Or alternatively, install using Pip::

  $ pip install python-cfonts


Command Line Interface
----------------------

.. code-block::

    usage: cfonts [-h] [-V]
                  [-f {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}]
                  [-c COLORS] [-b BACKGROUND] [-a {left,center,right}]
                  [-l LETTER_SPACING] [-z LINE_HEIGHT] [-s] [-m MAX_LENGTH]
                  [-g GRADIENT] [-i] [-t]
                  text

    positional arguments:
      text

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -f {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}, --font {console,block,simpleBlock,simple,3d,simple3d,chrome,huge,grid,pallet,shade,slick}
                            Use to define the font face
      -c COLORS, --colors COLORS
                            Use to define the font color
      -b BACKGROUND, --background BACKGROUND
                            Use to define the background color
      -a {left,center,right}, --align {left,center,right}
                            Use to align the text output
      -l LETTER_SPACING, --letter-spacing LETTER_SPACING
                            Use to define the letter spacing
      -z LINE_HEIGHT, --line-height LINE_HEIGHT
                            Use to define the line height
      -s, --spaceless       Use to define the background color
      -m MAX_LENGTH, --max-length MAX_LENGTH
                            Use to define the amount of maximum characters per
                            line
      -g GRADIENT, --gradient GRADIENT
                            Define gradient colors(separated by comma)
      -i, --independent-gradient
                            Set this option to re-calculate the gradient colors
                            for each new line.Only works in combination with the
                            gradient option.
      -t, --transition-gradient
                            Set this option to generate your own gradients. Each
                            color set in the gradient option will then be
                            transitioned to directly.

Examples
++++++++

.. image:: /_static/images/demos.png
    :target: _static/images/demos.png

API References
--------------

.. module:: cfonts

.. autofunction:: render
.. autofunction:: say
