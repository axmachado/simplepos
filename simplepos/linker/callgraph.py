# -*- coding: utf-8
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

    Function call graph - used for variable allocation optimizations
"""


class CallGraph(object):
    """
    Function call graph for variable allocation analysis
    """
    def __init__(self, name):
        self.name = name
        self.called = set()
        self.caller = set()

    def addCall(self, node):
        """
        Add a call to the node
        """
        if node not in self.called:
            self.called.add(node)
            node.addCaller(self)

    def addCaller(self, node):
        """
        add a caller to the node
        """
        if node not in self.caller:
            self.caller.add(node)
            node.addCall(self)

    def findNode(self, name, visited=None):
        """
        find a node by name
        """
        if not visited:
            visited = set()
        if name == self.name:
            return self
        visited.add(self)
        for node in self.called:
            if node not in visited:
                result = node.findNode(name, visited)
                if result:
                    return result
        for node in self.caller:
            if node not in visited:
                result = node.findNode(name, visited)
                if result:
                    return result
        return None
