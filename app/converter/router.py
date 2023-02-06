#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2023-02-06 11:09:32
# @Author  : Dahir Muhammad Dahir (dahirmuhammad3@gmail.com)
# @Link    : link
# @Version : 1.0.0


from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from app.converter import cruds

converter_router = APIRouter(
    prefix="/converter",
    tags=["Image Converter Router"]
)


@converter_router.post(
    "",
)
async def convert(
    image: UploadFile = File(),
):
    in_memory_file = cruds.convert_heif(image)

    return StreamingResponse(in_memory_file, media_type="image/png")


