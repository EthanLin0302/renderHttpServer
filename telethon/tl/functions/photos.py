"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeInputFile, TypeInputPhoto, TypeInputUser



class DeletePhotosRequest(TLRequest):
    CONSTRUCTOR_ID = 0x87cf7f2f
    SUBCLASS_OF_ID = 0x8918e168

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List['TypeInputPhoto']):
        """
        :returns Vector<long>: This type has no constructors.
        """
        self.id = id

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.id:
            _tmp.append(utils.get_input_photo(_x))

        self.id = _tmp

    def to_dict(self):
        return {
            '_': 'DeletePhotosRequest',
            'id': [] if self.id is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.id]
        }

    def _bytes(self):
        return b''.join((
            b'/\x7f\xcf\x87',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(x._bytes() for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _id.append(_x)

        return cls(id=_id)

    @staticmethod
    def read_result(reader):
        reader.read_int()  # Vector ID
        return [reader.read_long() for _ in range(reader.read_int())]


class GetUserPhotosRequest(TLRequest):
    CONSTRUCTOR_ID = 0x91cd32a8
    SUBCLASS_OF_ID = 0x27cfb967

    def __init__(self, user_id: 'TypeInputUser', offset: int, max_id: int, limit: int):
        """
        :returns photos.Photos: Instance of either Photos, PhotosSlice.
        """
        self.user_id = user_id
        self.offset = offset
        self.max_id = max_id
        self.limit = limit

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'GetUserPhotosRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'offset': self.offset,
            'max_id': self.max_id,
            'limit': self.limit
        }

    def _bytes(self):
        return b''.join((
            b'\xa82\xcd\x91',
            self.user_id._bytes(),
            struct.pack('<i', self.offset),
            struct.pack('<q', self.max_id),
            struct.pack('<i', self.limit),
        ))

    @classmethod
    def from_reader(cls, reader):
        _user_id = reader.tgread_object()
        _offset = reader.read_int()
        _max_id = reader.read_long()
        _limit = reader.read_int()
        return cls(user_id=_user_id, offset=_offset, max_id=_max_id, limit=_limit)


class UpdateProfilePhotoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x72d4742c
    SUBCLASS_OF_ID = 0xc292bd24

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputPhoto'):
        """
        :returns photos.Photo: Instance of Photo.
        """
        self.id = id

    async def resolve(self, client, utils):
        self.id = utils.get_input_photo(self.id)

    def to_dict(self):
        return {
            '_': 'UpdateProfilePhotoRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id
        }

    def _bytes(self):
        return b''.join((
            b',t\xd4r',
            self.id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        return cls(id=_id)


class UploadProfilePhotoRequest(TLRequest):
    CONSTRUCTOR_ID = 0x89f30f69
    SUBCLASS_OF_ID = 0xc292bd24

    def __init__(self, file: Optional['TypeInputFile']=None, video: Optional['TypeInputFile']=None, video_start_ts: Optional[float]=None):
        """
        :returns photos.Photo: Instance of Photo.
        """
        self.file = file
        self.video = video
        self.video_start_ts = video_start_ts

    def to_dict(self):
        return {
            '_': 'UploadProfilePhotoRequest',
            'file': self.file.to_dict() if isinstance(self.file, TLObject) else self.file,
            'video': self.video.to_dict() if isinstance(self.video, TLObject) else self.video,
            'video_start_ts': self.video_start_ts
        }

    def _bytes(self):
        return b''.join((
            b'i\x0f\xf3\x89',
            struct.pack('<I', (0 if self.file is None or self.file is False else 1) | (0 if self.video is None or self.video is False else 2) | (0 if self.video_start_ts is None or self.video_start_ts is False else 4)),
            b'' if self.file is None or self.file is False else (self.file._bytes()),
            b'' if self.video is None or self.video is False else (self.video._bytes()),
            b'' if self.video_start_ts is None or self.video_start_ts is False else (struct.pack('<d', self.video_start_ts)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        if flags & 1:
            _file = reader.tgread_object()
        else:
            _file = None
        if flags & 2:
            _video = reader.tgread_object()
        else:
            _video = None
        if flags & 4:
            _video_start_ts = reader.read_double()
        else:
            _video_start_ts = None
        return cls(file=_file, video=_video, video_start_ts=_video_start_ts)

