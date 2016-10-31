#-------------------------------------------------------------------------------
# File:         more_function_decorators.py
#
# Description:  A more complex example of how to write your own decorators in 
#               Python. 
#               Uses Python v3.0.
#
# (C) 2009 by Ariel Ortiz, Tecnologico de Monterrey, Campus Estado de Mexico.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#-------------------------------------------------------------------------------
        
class swallow_ver1:
    
    class helper:
        
        def __init__(self, outer, fun):
            self.outer = outer
            self.fun = fun            
            
        def __call__(self, *args, **kwargs):
            try:
                return self.fun(*args, **kwargs)
            except self.outer.exceptions:
                return self.outer.default
    
    def __init__(self, default=None, exceptions=BaseException):
        self.default = default
        self.exceptions = exceptions
        
    def __call__(self, fun):                            
        return swallow.helper(self, fun)

#-------------------------------------------------------------------------------

def swallow_ver2(default=None, exceptions=BaseException):
    def helper1(fun):
        def helper2(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            except exceptions:
                return default
        return helper2
    return helper1

#-------------------------------------------------------------------------------
# Specify here what version of the swallow decorator you want to use:
# swallow = swallow_ver1
swallow = swallow_ver2

@swallow(exceptions=TypeError, default='Huh?')
@swallow(exceptions=ZeroDivisionError, default=0)
def divide(dividend=0, divisor=1):
    return dividend / divisor

