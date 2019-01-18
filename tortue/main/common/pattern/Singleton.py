# coding: utf-8


class Singleton(object):
    __singleton_instance = None

    @classmethod
    def instance(cls):
        if not cls.__singleton_instance:
            cls.__singleton_instance = cls()
        return cls.__singleton_instance
