# -*- coding: utf-8 -*-

"""

WENV-KERNEL
Jupyter kernel for Python on Wine
https://github.com/pleiszenburg/wenv-kernel

	src/wenvkernel/_core.py: Package core

	Copyright (C) 2017-2020 Sebastian M. Ernst <ernst@pleiszenburg.de>

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

DEFAULT_TIMEOUT = 600
LOGO_FN = 'logo-{SIZE:d}x{SIZE:d}.png'
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

import base64
import json
import os
import subprocess
import sys

from ._logos import LOGOS, LOGO_SIZES

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def setup_kernels():

	for bits in (32, 64):
		setup_kernel(bits)

def setup_kernel(bits):

	kernel_name = _get_name(bits)
	kernel_path = _get_path(kernel_name)
	_ensure_path(kernel_path)
	_write_config(kernel_path, bits)
	for size in LOGO_SIZES:
		_write_image(kernel_path, bits, size)
	_wenv_init(bits)
	_wenv_pip(bits, 'install', 'ipykernel')

def _ensure_path(kernel_path):

	os.makedirs(kernel_path, exist_ok = True)

def _get_name(bits):

	return KERNEL_NAME + '_{BITS:d}bit'.format(BITS = bits)

def _get_path(kernel_name):

	return os.path.join(sys.prefix, 'share', 'jupyter', 'kernels', kernel_name)

def _run_process(cmd_list, env = None, timeout = DEFAULT_TIMEOUT):

	if env is None:
		env = {}
	envvar_dict = {k: os.environ[k] for k in os.environ.keys()}
	envvar_dict.update(env)

	proc = subprocess.Popen(
		cmd_list,
		stdout = subprocess.PIPE,
		stderr = subprocess.PIPE,
		env = envvar_dict
		)
	try:
		outs, errs = proc.communicate(timeout = timeout)
	except subprocess.TimeoutExpired:
		os.kill(proc.pid, signal.SIGINT)
		outs, errs = proc.communicate()

	return (
		outs.decode('utf-8'),
		errs.decode('utf-8'),
		proc.returncode
		)

def _wenv_init(bits):

	out, err, code = _run_process(
		['wenv', 'init'],
		env = {'WENV_ARCH': 'win{BITS:d}'.format(BITS = bits)}
		)
	if code != 0:
		raise SystemError('wenv init failed', out, err)

def _wenv_pip(bits, *args):

	out, err, code = _run_process(
		['wenv', 'pip'] + list(args),
		env = {'WENV_ARCH': 'win{BITS:d}'.format(BITS = bits)}
		)
	if code != 0:
		raise SystemError('wenv pip failed', out, err)

def _write_config(kernel_path, bits):

	kernel = KERNEL_TEMPLATE.copy()
	kernel['display_name'] += ' {BITS:d}bit'.format(BITS = bits)
	kernel['env'] = {'WENV_ARCH': 'win{BITS:d}'.format(BITS = bits)}

	with open(os.path.join(kernel_path, KERNEL_FN), 'w', encoding = 'utf-8') as f:
		f.write(json.dumps(kernel, indent = 4, sort_keys = False))

def _write_image(kernel_path, bits, size):

	with open(os.path.join(kernel_path, LOGO_FN.format(SIZE = size)), 'wb') as f:
		f.write(base64.b64decode(LOGOS[(size, bits)].strip().replace('\n', '')))
