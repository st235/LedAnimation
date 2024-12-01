try:
    from abc import ABC, abstractmethod
except ImportError:
    class ABC:
        pass


    def abstractmethod(func):
        return func
