# -*- coding: utf-8
# pylint: disable=C0401
# pragma pylint: disable=R0401
# disables pylint cyclic import check for this module.
"""
    Copyright © 2017 - Alexandre Machado <axmachado@gmail.com>

    This file is part of Simple POS Compiler.

    Simnple POS Compiler is free software: you can redistribute it
    and/or modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, either version 3
    of the License, or (at your option) any later version.

    Simple POS Compiler is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Simple POS Compiler. If not, see <http://www.gnu.org/licenses/>.


    @author: Alexandre Machado <axmachado@gmail.com>

    Façade to code generation objects
"""

from .base import POSXMLStatement, CodeGenerationError
from .code import POSXMLCode

__all__ = ['POSXMLCode', 'POSXMLStatement', 'CodeGenerationError']
