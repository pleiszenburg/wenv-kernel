# -*- coding: utf-8 -*-

"""

WENV-KERNEL
Jupyter kernel for Python on Wine
https://github.com/pleiszenburg/wenv-kernel

	src/wenvkernel/_core.py: Package core

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
# CONST
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

KERNEL_FN = 'kernel.json'
KERNEL_NAME = 'wenv_python3'
KERNEL_TEMPLATE = {
	'argv': [
		'wenv',
		'python',
		'-m',
		'ipykernel_launcher',
		'-f',
		'{connection_file}'
		],
	'display_name': 'wenv python',
	'language': 'python',
	}

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import json
import os
import sys

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def setup_kernel():

	for bits in (32, 64):
		kernel_name = _get_name(bits)
		kernel_path = _get_path(kernel_name)
		_ensure_path(kernel_path)
		_write_config(kernel_path, bits)

def _ensure_path(kernel_path):

	os.makedirs(kernel_path, exist_ok = True)

def _get_name(bits):

	return KERNEL_NAME + '_{BITS:d}bit'.format(BITS = bits)

def _get_path(kernel_name):

	return os.path.join(sys.prefix, 'shared', 'kernels', kernel_name)

def _write_config(kernel_path, bits):

	kernel = KERNEL_TEMPLATE.copy()
	kernel['display_name'] += ' {BITS:d}bit'.format(BITS = bits)
	kernel['env'] = {'WENV_ARCH': 'win{BITS:d}'.format(BITS = bits)}

	with open(os.path.join(kernel_path, KERNEL_FN), 'w', encoding = 'utf-8') as f:
		f.write(json.dumps(kernel), indent = 4, sort_keys = False)
