import logging
import sys

from . import clean, init, serve

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    match sys.argv:
        case [_, "clean", *args]:
            dir = args[0] if args else "site"
            clean(dir)
            sys.exit(0)
        case [_, "init", *_]:
            init()
        case [_, "serve", *args]:
            arg_iter = iter(args)
            port = int(next(arg_iter, 8000))
            build_script = next(arg_iter, "build.py")
            site_dir = next(arg_iter, "site")
            serve(port, build_script, site_dir, list(arg_iter))
        case _:
            logger.info("Usage: markupdown clean | init | serve")
            sys.exit(1)
