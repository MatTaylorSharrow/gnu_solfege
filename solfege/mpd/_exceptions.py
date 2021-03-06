# Solfege - free ear training software
# Copyright (C) 2004, 2007, 2008, 2011, 2016  Tom Cato Amundsen
# License is GPL, see file COPYING


class MpdException(Exception):
    """
    I think all exceptions that are raised from
    mpd.parser.parse_to_score_object should inherit from this. They will
    all be handled by abstract.Gui.standard_exception_handler.
    """
    pass
