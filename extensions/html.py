# -*- coding: utf-8 -*-
# [MOSAICODE PROJECT]
#
"""
This module contains the JavascriptTemplate class.
"""
from mosaicode.model.codetemplate import CodeTemplate

class Html(CodeTemplate):
    """
    This class contains methods related the JavascriptTemplate class.
    """
    # ----------------------------------------------------------------------

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "webaudio"
        self.language = "javascript"
        self.description = "Javascript / webaudio code template"
        self.extension = ".html"
        self.command = "chromium-browser $dir_name$$filename$$extension$\n"
        self.code = r"""<html>
<head>
<meta http-equiv="Cache-Control" content="no-store" />
<title>Generated by Mosaicode</title>
</head>
<body>
<script>
var context = new (window.AudioContext || window.webkitAudioContext)();
$single_code[0]$
//declaration block
$code[1]$
//connections
$connections$
//function calls
$code[2]$
</script>
<! deallocation block --!>
$code[3]$
$code[4]$
</body>
</html>
"""

# -------------------------------------------------------------------------
