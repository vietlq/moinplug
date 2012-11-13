"""
    MoinMoin - IncludePage Macro

    You can use this macro to include a page through an <iframe>.

    Usage:
    <<IncludePage(FrontPage, 800, 600)>>
    <<IncludePage(MoinMoin:FrontPage, 800, 600)>>
    <<IncludePage(http://moinmo.in, 90%, 30%)>>

    You need to specify at least the page to inline and the width and the height of the iframe.

    Optionally you can customize ouput by using the following parameters:
    align=left/rigth: Aligns the frame to the left or right, text will float around [Default: no align and float]
    scrolling=yes/no: Turn on/off scrolling bars [Default: auto]
    marginwith=0: Set margin with [Default: 0]
    marginheight=0: Set margin height [Default: 0]
    frameborder=0: Set frameboarder [Default: 0]
    longdesc="Your text..": Give a sensible description for screenreader users [Default:""]
    
    Warning:
    Using <iframe> is not compliant with HTML strict standard. Therefore a common
    markup validation service will display an "invalid html" error message for a
    wiki page using this macro.

    @copyright: 2008 Oliver Siemoneit, 2012 Le Quoc Viet
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin import wikiutil
from MoinMoin.Page import Page

def _is_url(text):
    return '://' in text

def _is_interwiki(text):
    return ':' in text

def macro_IncludePage(macro, src=str, width=str, height=str, **kwargs):
    request = macro.request
    formatter = macro.formatter
    _ = request.getText
    named_params = dict(kwargs)
    
    # Prepare URL
    src = wikiutil.escape(src)
    if _is_url(src):
        pass
    elif _is_interwiki(src):
        wiki, page = wikiutil.split_interwiki(src)
        wikitag, wikiurl, wikitail, err = wikiutil.resolve_interwiki(request, wiki, page)
        src = wikiutil.join_wiki(wikiurl, wikitail)
    else:
        src = Page(request, src).url(request)
    
    # Escape other parameters and set defaults
    width = wikiutil.escape(width)
    height = wikiutil.escape(height)
    align = wikiutil.escape(named_params.get("align", ""))
    scrolling = wikiutil.escape(named_params.get("scrolling", "auto"))
    marginheight= wikiutil.escape(named_params.get("marginheight","0"))
    marginwidth = wikiutil.escape(named_params.get("marginwidth", "0"))
    frameborder = wikiutil.escape(named_params.get("frameborder","0"))
    longdesc = wikiutil.escape(named_params.get("longdesc",""))
    
    # Output stuff
    result = """
<iframe src="%(src)s" width="%(width)s" height="%(height)s" align="%(align)s" scrolling="%(scrolling)s" marginheight="%(marginheight)s" marginwidth="%(marginwidth)s" frameborder="%(frameborder)s" longdesc="%(longdesc)s">
    <p>%(error_msg)s <a href="%(src)s">%(src)s</a> </p>
</iframe>
""" % { 'src': src,
                 'width': width,
                 'height': height,
                 'align': align,
                 'scrolling': scrolling,
                 'marginheight': marginheight,
                 'marginwidth': marginwidth,
                 'frameborder': frameborder,
                 'longdesc': longdesc,
                 'error_msg': _("Your browser cannot display inlined frames. You can call the inlined page through the following link:") }
    
    return formatter.rawHTML(result)

