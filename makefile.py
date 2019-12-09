# -*- coding: utf-8 -*-

"""

WENV-KERNEL
Jupyter kernel for Python on Wine
https://github.com/pleiszenburg/wenv-kernel

	makefile.py: Packaging

	Copyright (C) 2017-2019 Sebastian M. Ernst <ernst@pleiszenburg.de>

<LICENSE_BLOCK>
The contents of this file are subject to the GNU Lesser General Public License
Version 2.1 ("LGPL" or "License"). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://www.gnu.org/licenses/old-licenses/lgpl-2.1.txt
https://github.com/pleiszenburg/wenv-kernel/blob/master/LICENSE

Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>

"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import base64
import os

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CONST
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

LOGO_PY = os.path.join('src', 'wenvkernel', '_logos.py')
RESOURCES_FLD = 'res'
LOGO_FN = 'logo-{SIZE:d}x{SIZE:d}_{BITS:d}.png'
SIZES = (32, 64)
BITS = (32, 64)
LINE_LEN = 72

TEMPLATE_FILE = """# -*- coding: utf-8 -*-
# This file is part of WENV-KERNEL.
# Do not change it manually. Changes will be lost on next re-build.

LOGO_SIZES = (32, 64)

LOGOS = {{

{CONTENT}

}}
"""
TEMPLATE_VAR = '({SIZE:d}, {BITS:d}): """\n{IMAGE:s}\n""",'

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ROUTINES
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def resources():

	images = {(bits, size): _get_image(bits, size) for size in SIZES for bits in BITS}

	content = [
		TEMPLATE_VAR.format(BITS = bits, SIZE = size, IMAGE = image)
		for (bits, size), image in images.items()
		]

	with open(LOGO_PY, 'w', encoding = 'utf-8') as f:
		f.write(TEMPLATE_FILE.format(CONTENT = '\n\n'.join(content)))

def _get_image(bits, size):

	fn = LOGO_FN.format(BITS = bits, SIZE = size)
	with open(os.path.join(RESOURCES_FLD, fn), 'rb') as f:
		data = f.read()

	data = base64.b64encode(data).decode('utf-8')

	return '\n'.join(data[pos:(pos + LINE_LEN)] for pos in range(0, len(data), LINE_LEN))
