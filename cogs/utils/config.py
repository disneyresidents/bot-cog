import json
import asyncio


class Config:
    def __init__(self, name):
        self.name = name
        self.loop = asyncio.get_event_loop()
        self.lock = asyncio.Lock()

        try:
            with open(self.name, 'r') as f:
                self._file = json.load(f)
        except Exception:
            self._file = {}

    async def _dump(self):
        with open(self.name, 'w', encoding='utf-8') as f:
            json.dump(self._file.copy(), f, ensure_ascii=True, separators=(',', ':'))

    async def put(self, key, value, sub_key=None):
        if sub_key is None:
            self._file[str(key)] = value
        else:
            if str(key) not in self._file.keys():
                self._file[str(key)] = {}
            self._file[str(key)][str(sub_key)] = value
        await self._dump()

    async def remove(self, key, sub_key=None):
        if sub_key is None:
            value = self._file.pop(str(key))
        else:
            value = self._file[str(key)].pop(str(sub_key))
        await self._dump()
        return value

    def get(self, key, args, sub_key=None):
        if sub_key is None:
            return self._file.get(str(key), args)
        return self._file[str(key)].get(str(sub_key), args)

    def keys(self, key=None):
        if key is None:
            return self._file.keys()
        else:
            if str(key) not in self._file.keys():
                return {}
            return self._file[str(key)].keys()
