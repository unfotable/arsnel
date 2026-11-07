"""The logging module: loggers, levels, handlers and formatters."""

import io
import logging
import logging.config

stream = io.StringIO()
handler = logging.StreamHandler(stream)
handler.setFormatter(logging.Formatter("%(levelname)-8s %(name)s: %(message)s"))

log = logging.getLogger("arsnel.demo")
log.setLevel(logging.INFO)
log.addHandler(handler)
log.propagate = False

log.debug("hidden: below INFO")
log.info("starting %s", "job")  # lazy %-style args
log.warning("disk at %d%%", 91)
try:
    _ = 1 / 0
except ZeroDivisionError:
    log.exception("failed")  # includes the traceback
print(stream.getvalue().splitlines()[0:3])

# dictConfig: configure everything declaratively.
out = io.StringIO()
logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"plain": {"format": "%(levelname)s|%(message)s"}},
        "handlers": {
            "mem": {
                "class": "logging.StreamHandler",
                "stream": out,
                "formatter": "plain",
            }
        },
        "loggers": {
            "arsnel.cfg": {"handlers": ["mem"], "level": "DEBUG", "propagate": False}
        },
    }
)
logging.getLogger("arsnel.cfg").debug("configured")
print(out.getvalue().strip())
