#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-02-06 11:44:41
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from io import BytesIO
from PIL import Image
from fastapi import UploadFile
from pillow_heif import register_heif_opener

register_heif_opener()


def convert_heif(
    image: UploadFile
):
    img = Image.open(image.file)
    in_memory = BytesIO()
    img.save(in_memory, 'PNG')
    in_memory.seek(0)
    return in_memory

