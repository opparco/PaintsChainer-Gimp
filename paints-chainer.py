#!/usr/bin/env python

from gimpfu import *
import os
import time # for sleep

# -------
# Setting
# -------
PAINTS_CHAINER_ROOT = os.environ['HOME'] + '/src/PaintsChainer'


def paints_chainer(image, ref_layer):
    gimp.message("ENTER paints_chainer")

    # ----------
    # Find layer
    # ----------
    # The active layer is a reference (color hint) layer.
    # And a line layer should be one below the reference layer.

    line_layer = None
    prev_layer = None

    for layer in reversed(image.layers):
        if layer == ref_layer:
            line_layer = prev_layer
        prev_layer = layer

    if line_layer is None:
        gimp.message("FAIL: line layer was not found.")
        return

    if ref_layer is None:
        gimp.message("FAIL: ref layer was not found.")
        return

    # gimp.message("p1")
    pid_path = PAINTS_CHAINER_ROOT + '/run/main.pid'
    line_path = PAINTS_CHAINER_ROOT + '/images/line/main.png'
    ref_path = PAINTS_CHAINER_ROOT + '/images/ref/main.png'
    colored_path = PAINTS_CHAINER_ROOT + '/images/out/main_0.png'

    pdb.file_png_save_defaults(image, line_layer, line_path, line_path)
    pdb.file_png_save_defaults(image, ref_layer, ref_path, ref_path)

    # gimp.message("p2")
    if os.path.exists(colored_path):
        os.remove(colored_path)

    if os.path.exists(pid_path):
        gimp.message("FAIL: pid file was found.")
        return

    with open(pid_path, "wt") as pid_file:
        pid_file.write(str(os.getpid()))

    loop_limit = 20
    loop_count = 0
    gimp.message("Colorize now...")
    while os.path.exists(pid_path):
        if loop_count < loop_limit:
            gimp.message("sleep 0.5 sec")
            time.sleep(0.5)
            loop_count += 1
        else:
            gimp.message("FAIL: timeout")
            return

    # gimp.message("p3")
    colored_layer = pdb.gimp_file_load_layer(image, colored_path)
    pdb.gimp_image_insert_layer(image, colored_layer, None, 0)

    gimp.message("LEAVE paints_chainer")


register(
    "python_fu_paints_chainer",
    "Paints Chainer",
    "0. Prepare layers: line and ref."
    "1. Select the ref layer."
    "2. Run this script from menu."
    "3. Then colored layer will be added.",
    "Parco Opaai",
    "Parco Opaai",
    "2017",
    "<Image>/Filters/Artistic/_Paints Chainer",
    "*",
    [], # arguments image and layer are auto
    [],
    paints_chainer,
    )

main()
