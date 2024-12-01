try:
    from mycropython import const
except ImportError:
    def const(value):
        return value

__NANOS_IN_MS = const(1_000_000)
__MS_IN_SECOND = const(1_000)

try:
    from time import time_ns


    def time_ms() -> int:
        return time_ns() // __NANOS_IN_MS
except (ImportError, NotImplementedError):
    from time import time


    def time_ms() -> int:
        return time() * __MS_IN_SECOND
