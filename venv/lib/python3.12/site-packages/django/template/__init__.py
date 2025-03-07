"""
Django's support for templates.

The django.templates namespace contains two independent subsystems:

1. Multiple Template Engines: support for pluggable templates backends,
   built-in backends and backend-independent APIs
2. Django Template Language: Django's own templates engine, including its
   built-in loaders, context processors, tags and filters.

Ideally these subsystems would be implemented in distinct packages. However
keeping them together made the implementation of Multiple Template Engines
less disruptive .

Here's a breakdown of which modules belong to which subsystem.

Multiple Template Engines:

- django.templates.backends.*
- django.templates.loader
- django.templates.response

Django Template Language:

- django.templates.base
- django.templates.context
- django.templates.context_processors
- django.templates.loaders.*
- django.templates.debug
- django.templates.defaultfilters
- django.templates.defaulttags
- django.templates.engine
- django.templates.loader_tags
- django.templates.smartif

Shared:

- django.templates.utils

"""

# Multiple Template Engines

from .engine import Engine
from .utils import EngineHandler

engines = EngineHandler()

__all__ = ("Engine", "engines")


# Django Template Language

# Public exceptions
from .base import VariableDoesNotExist  # NOQA isort:skip
from .context import Context, ContextPopException, RequestContext  # NOQA isort:skip
from .exceptions import TemplateDoesNotExist, TemplateSyntaxError  # NOQA isort:skip

# Template parts
from .base import (  # NOQA isort:skip
    Node,
    NodeList,
    Origin,
    Template,
    Variable,
)

# Library management
from .library import Library  # NOQA isort:skip

# Import the .autoreload module to trigger the registrations of signals.
from . import autoreload  # NOQA isort:skip


__all__ += ("Template", "Context", "RequestContext")
