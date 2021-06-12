# importスタイル
import os
import sys

# fromの場合はOK
from subprocess import Popen, PIPE

# 順番
# 1. Standard library (time, sys)
# 2. Third party (numpy, pandas)
# 3. Our library
# 4. Local library
# それぞれ一行あける

# absolute import
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

from package.subpackage1.subpackage2.subpackage3.module4 import function