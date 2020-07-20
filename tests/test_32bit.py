# -*- coding: utf-8 -*-

"""

WENV-KERNEL
Jupyter kernel for Python on Wine
https://github.com/pleiszenburg/wenv-kernel

    tests/test_32bit.py: Testing 32 bit kernel

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
# IMPORT
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import unittest
import jupyter_kernel_test

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# TESTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


class MyKernelTests(jupyter_kernel_test.KernelTests):
    # Required --------------------------------------

    # The name identifying an installed kernel to run the tests against
    kernel_name = "wenv_python3_32bit"

    # language_info.name in a kernel_info_reply should match this
    language_name = "python"

    # Optional --------------------------------------

    # Code in the kernel's language to write "hello, world" to stdout
    code_hello_world = "print('hello, world')"

    # Pager: code that should display something (anything) in the pager
    code_page_something = "help(print)"

    # Samples of code which generate a result value (ie, some text
    # displayed as Out[n])
    code_execute_result = [{"code": "6*7", "result": "42"}]

    # Samples of code which should generate a rich display output, and
    # the expected MIME type
    # code_display_data = [
    # 	{'code': 'show_image()', 'mime': 'image/png'}
    # ]

    # You can also write extra tests. We recommend putting your kernel name
    # in the method name, to avoid clashing with any tests that
    # jupyter_kernel_test adds in the future.
    # def test_wenv_python3_32bit_stderr(self):
    # 	reply, output_msgs = self.execute_helper(code='print_err "oops"')
    # 	self.assertEqual(output_msgs[0].header['msg_type'], 'stream')
    # 	self.assertEqual(output_msgs[0].content['name'], 'stderr')
    # 	self.assertEqual(output_msgs[0].content['text'], 'oops\n')
