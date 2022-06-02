"""Piccolo database engine configuration."""
from piccolo.engine import SQLiteEngine

from casper7_plugin_meatball_day.settings import settings

DB = SQLiteEngine(str(settings.database))
