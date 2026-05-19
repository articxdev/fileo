# Knox/utils/custom_dl.py

import asyncio
import time
from typing import Any, AsyncGenerator, Dict

from pyrogram import Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from Knox.server.exceptions import FileNotFound
from Knox.utils.file_properties import get_media
from Knox.utils.logger import logger
from Knox.vars import Var


class ByteStreamer:
    __slots__ = ('client', 'chat_id', '_message_cache', '_message_events', '_cache_lock')

    def __init__(self, client: Client) -> None:
        self.client = client
        self.chat_id = int(Var.BIN_CHANNEL)
        self._message_cache = {}
        self._message_events = {}
        self._cache_lock = asyncio.Lock()

    async def get_message(self, message_id: int) -> Message:
        now = time.time()
        
        async with self._cache_lock:
            if message_id in self._message_cache:
                msg, timestamp = self._message_cache[message_id]
                if now - timestamp < 3600:
                    return msg
                else:
                    del self._message_cache[message_id]
            
            if message_id in self._message_events:
                event = self._message_events[message_id]
                wait = True
            else:
                event = asyncio.Event()
                self._message_events[message_id] = event
                wait = False
                
        if wait:
            await event.wait()
            async with self._cache_lock:
                if message_id in self._message_cache:
                    msg, timestamp = self._message_cache[message_id]
                    if time.time() - timestamp < 3600:
                        return msg

        while True:
            try:
                message = await self.client.get_messages(self.chat_id, message_id)
                break
            except FloodWait as e:
                logger.debug(f"FloodWait: get_message, sleep {e.value}s")
                await asyncio.sleep(e.value)
            except Exception as e:
                logger.debug(f"Error fetching message {message_id}: {e}", exc_info=True)
                async with self._cache_lock:
                    if message_id in self._message_events:
                        self._message_events[message_id].set()
                        del self._message_events[message_id]
                raise FileNotFound(f"Message {message_id} not found") from e

        if not message or not message.media:
            async with self._cache_lock:
                if message_id in self._message_events:
                    self._message_events[message_id].set()
                    del self._message_events[message_id]
            raise FileNotFound(f"Message {message_id} not found")
            
        async with self._cache_lock:
            if len(self._message_cache) >= 1000:
                self._message_cache.pop(next(iter(self._message_cache)))
            self._message_cache[message_id] = (message, time.time())
            if message_id in self._message_events:
                self._message_events[message_id].set()
                del self._message_events[message_id]
                
        return message

    async def stream_file(
        self, message_id: int, offset: int = 0, limit: int = 0
    ) -> AsyncGenerator[bytes, None]:
        message = await self.get_message(message_id)

        chunk_offset = offset // (1024 * 1024)

        chunk_limit = 0
        if limit > 0:
            chunk_limit = ((limit + (1024 * 1024) - 1) // (1024 * 1024)) + 1

        while True:
            try:
                async for chunk in self.client.stream_media(
                    message, offset=chunk_offset, limit=chunk_limit
                ):
                    yield chunk
                break
            except FloodWait as e:
                logger.debug(f"FloodWait: stream_file, sleep {e.value}s")
                await asyncio.sleep(e.value)

    def get_file_info_sync(self, message: Message) -> Dict[str, Any]:
        media = get_media(message)
        if not media:
            return {"message_id": message.id, "error": "No media"}

        media_type = type(media).__name__.lower()
        file_name = getattr(media, 'file_name', None)
        mime_type = getattr(media, 'mime_type', None)

        if not file_name:
            ext_map = {
                "photo": "jpg",
                "audio": "mp3",
                "voice": "ogg",
                "video": "mp4",
                "animation": "mp4",
                "videonote": "mp4",
                "sticker": "webp",
            }
            ext = ext_map.get(media_type, "bin")
            file_name = f"F2L_{message.id}.{ext}"

        if not mime_type:
            mime_map = {
                "photo": "image/jpeg",
                "voice": "audio/ogg",
                "videonote": "video/mp4",
            }
            mime_type = mime_map.get(media_type)

        return {
            "message_id": message.id,
            "file_size": getattr(media, 'file_size', 0) or 0,
            "file_name": file_name,
            "mime_type": mime_type,
            "unique_id": getattr(media, 'file_unique_id', None),
            "media_type": media_type
        }

    async def get_file_info(self, message_id: int) -> Dict[str, Any]:
        try:
            message = await self.get_message(message_id)
            return self.get_file_info_sync(message)
        except Exception as e:
            logger.debug(f"Error getting file info for {message_id}: {e}", exc_info=True)
            return {"message_id": message_id, "error": str(e)}
