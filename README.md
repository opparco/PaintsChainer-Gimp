# PaintsChainer-Gimp
PaintsChainer GIMP 2.8 plug-in

## Demo
[30 sec. firm on twitter](https://twitter.com/parco_opaai/status/828032261551316992)

## Requirement
- [PaintsChainer](https://github.com/pfnet/PaintsChainer)
- [GIMP 2.8](https://www.gimp.org/)

## Installation
This plug-in write main.pid file in run directory on PaintsChainer root.

    $ cd $HOME/src/PaintsChainer
    $ mkdir run

Move painter.py in the same directory as cgi-exe.py.

    $ mv painter.py cgi-bin/paint_x2_unet/

Edit setting in paints-chainer.py:

    PAINTS_CHAINER_ROOT = os.environ['HOME'] + '/src/PaintsChainer'

Move paints-chainer.py in GIMP plug-ins directory (not scripts directory).

    $ mv paints-chainer.py $HOME/.gimp-2.8/plug-ins/

GIMP plug-in must be executable (on Unix).

    $ chmod +x $HOME/.gimp-2.8/plug-ins/paints-chainer.py

## Usage
Run painter.py on PaintsChainer root.

    $ cd $HOME/src/PaintsChainer
    $ python painter.py
    start
    load model

Launch GIMP (Options for debug):

    $ gimp-2.8 -c --verbose

On GIMP, open your line image (as line layer).
Add a transparent layer (as color hint layer) above the line layer.
Select the color hint layer, and run plug-in through menu: Filters/Artistic/_Paints Chainer

## Licence
[MIT](https://github.com/opaai/PaintsChainer-Gimp/blob/master/LICENSE)

## Author
[Parco Opaai](https://github.com/opaai)
