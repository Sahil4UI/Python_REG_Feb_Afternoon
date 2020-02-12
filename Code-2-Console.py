Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a+b
15
>>> a-b
-5
>>> a*b
50
>>> a/b
0.5
>>> a//b
0
>>> 111/2
55.5
>>> 111//2
55
>>> 2**3
8
>>> sqrt(5)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sqrt(5)
NameError: name 'sqrt' is not defined
>>> import math
>>> math.sqrt(25)
5.0
>>> math.sqrt(10)
3.1622776601683795
>>> math.log(10)
2.302585092994046
>>> math.log10(10)
1.0
>>> math.log10(1)
0.0
>>> math.pi()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    math.pi()
TypeError: 'float' object is not callable
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
>>> help(math)
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.7/library/math
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so


>>> a = 3 - 5j
>>> a = 3-5i
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> a
(3-5j)
>>> type(a)
<class 'complex'>
>>> a.real
3.0
>>> a.imag
-5.0
>>> c = a.real
>>> d = a.imag
>>> c
3.0
>>> d
-5.0
>>> 10/7
1.4285714285714286
>>> 10//7
1
>>> a = 2+5j
>>> b = 3-4j
>>> a+b
(5+1j)
>>> a-b
(-1+9j)
>>> a/b
(-0.56+0.92j)
>>> a*b
(26+7j)
>>> import cmath
>>> cmath.pi
3.141592653589793
>>> cmath.log(10)
(2.302585092994046+0j)
>>> 
>>> #string
>>> string = "This is String"
>>> type(string)
<class 'str'>
>>> a = "this is string"
>>> type(a)
<class 'str'>
>>> a = str(123)
>>> a
'123'
>>> a= 5
>>> type(a)
<class 'int'>
>>> a = str(a)
>>> type(a)
<class 'str'>
>>> a
'5'
>>> a = "This is A String"
>>> a[0]
'T'
>>> a[4]
' '
>>> len(a)
16
>>> a[len(a)-1]
'g'
>>> a[-1]
'g'
>>> a[-2]
'n'
>>> #String SLicing
>>> a
'This is A String'
>>> a[0:3]
'Thi'
>>> a[0:4]
'This'
>>> a[0:4:1]
'This'
>>> a[0:4:2]
'Ti'
>>> a[0::2]
'Ti sASrn'
>>> a[2:]
'is is A String'
>>> a[:]
'This is A String'
>>> a[-1:]
'g'
>>> a[-1::-1]
'gnirtS A si sihT'
>>> a[-3]
'i'
>>> a[-1:0:-1]
'gnirtS A si sih'
>>> a[-1::-1]
'gnirtS A si sihT'
>>> a
'This is A String'
>>> a.lower()
'this is a string'
>>> a.upper()
'THIS IS A STRING'
>>> a.capitalize()
'This is a string'
>>> a.title()
'This Is A String'
>>> #capitalize is used to convert every first Character of sentence into upper case
>>> #title is used to convert every first alphabet of every word into upper case
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.count()
TypeError: count() takes at least 1 argument (0 given)
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined
>>> a = "HeLLLO"
>>> a.count("L")
3
>>> a.index("L")
2
>>> a.find("L")
2
>>> a.rfind("L")
4
>>> a.find("L",0)
2
>>> a.find("L",2)
2
>>> a.find("L",3)
3
>>> a[-1]
'O'
>>> a.center(10)
'  HeLLLO  '
>>> a.center(3)
'HeLLLO'
>>> a.center(5)
'HeLLLO'
>>> a.center(6)
'HeLLLO'
>>> a.center(7)
' HeLLLO'
>>> a.center(8)
' HeLLLO '
>>> a.center(100)
'                                               HeLLLO                                               '
>>> a.center(100,"*")
'***********************************************HeLLLO***********************************************'
>>> a.center(100, )
'                                               HeLLLO                                               '
>>> a = a.center(50,"*")
>>> a
'**********************HeLLLO**********************'
>>> a.strip("*")
'HeLLLO'
>>> a
'**********************HeLLLO**********************'
>>> a = "hello this is replace method in string"
>>> a.replace("e","A")
'hAllo this is rAplacA mAthod in string'
>>> a
'hello this is replace method in string'
>>> a.replace("in","of")
'hello this is replace method of strofg'
>>> a
'hello this is replace method in string'
>>> a[0]=1
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a[0]=1
TypeError: 'str' object does not support item assignment
>>> a[0] = "Hey"
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a[0] = "Hey"
TypeError: 'str' object does not support item assignment
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(self, format_spec, /)
 |      Return a formatted version of the string as described by format_spec.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the string in memory, in bytes.
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(self, /)
 |      Return a capitalized version of the string.
 |      
 |      More specifically, make the first character have upper case and the rest lower
 |      case.
 |  
 |  casefold(self, /)
 |      Return a version of the string suitable for caseless comparisons.
 |  
 |  center(self, width, fillchar=' ', /)
 |      Return a centered string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(self, /, encoding='utf-8', errors='strict')
 |      Encode the string using the codec registered for encoding.
 |      
 |      encoding
 |        The encoding in which to encode the string.
 |      errors
 |        The error handling scheme to use for encoding errors.
 |        The default is 'strict' meaning that encoding errors raise a
 |        UnicodeEncodeError.  Other possible values are 'ignore', 'replace' and
 |        'xmlcharrefreplace' as well as any other name registered with
 |        codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(self, /, tabsize=8)
 |      Return a copy where all tab characters are expanded using spaces.
 |      
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found, 
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  isalnum(self, /)
 |      Return True if the string is an alpha-numeric string, False otherwise.
 |      
 |      A string is alpha-numeric if all characters in the string are alpha-numeric and
 |      there is at least one character in the string.
 |  
 |  isalpha(self, /)
 |      Return True if the string is an alphabetic string, False otherwise.
 |      
 |      A string is alphabetic if all characters in the string are alphabetic and there
 |      is at least one character in the string.
 |  
 |  isascii(self, /)
 |      Return True if all characters in the string are ASCII, False otherwise.
 |      
 |      ASCII characters have code points in the range U+0000-U+007F.
 |      Empty string is ASCII too.
 |  
 |  isdecimal(self, /)
 |      Return True if the string is a decimal string, False otherwise.
 |      
 |      A string is a decimal string if all characters in the string are decimal and
 |      there is at least one character in the string.
 |  
 |  isdigit(self, /)
 |      Return True if the string is a digit string, False otherwise.
 |      
 |      A string is a digit string if all characters in the string are digits and there
 |      is at least one character in the string.
 |  
 |  isidentifier(self, /)
 |      Return True if the string is a valid Python identifier, False otherwise.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers such as "def" and
 |      "class".
 |  
 |  islower(self, /)
 |      Return True if the string is a lowercase string, False otherwise.
 |      
 |      A string is lowercase if all cased characters in the string are lowercase and
 |      there is at least one cased character in the string.
 |  
 |  isnumeric(self, /)
 |      Return True if the string is a numeric string, False otherwise.
 |      
 |      A string is numeric if all characters in the string are numeric and there is at
 |      least one character in the string.
 |  
 |  isprintable(self, /)
 |      Return True if the string is printable, False otherwise.
 |      
 |      A string is printable if all of its characters are considered printable in
 |      repr() or if it is empty.
 |  
 |  isspace(self, /)
 |      Return True if the string is a whitespace string, False otherwise.
 |      
 |      A string is whitespace if all characters in the string are whitespace and there
 |      is at least one character in the string.
 |  
 |  istitle(self, /)
 |      Return True if the string is a title-cased string, False otherwise.
 |      
 |      In a title-cased string, upper- and title-case characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |  
 |  isupper(self, /)
 |      Return True if the string is an uppercase string, False otherwise.
 |      
 |      A string is uppercase if all cased characters in the string are uppercase and
 |      there is at least one cased character in the string.
 |  
 |  join(self, iterable, /)
 |      Concatenate any number of strings.
 |      
 |      The string whose method is called is inserted in between each given string.
 |      The result is returned as a new string.
 |      
 |      Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
 |  
 |  ljust(self, width, fillchar=' ', /)
 |      Return a left-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  lower(self, /)
 |      Return a copy of the string converted to lowercase.
 |  
 |  lstrip(self, chars=None, /)
 |      Return a copy of the string with leading whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string.  If the separator is found,
 |      returns a 3-tuple containing the part before the separator, the separator
 |      itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing the original string
 |      and two empty strings.
 |  
 |  replace(self, old, new, count=-1, /)
 |      Return a copy with all occurrences of substring old replaced by new.
 |      
 |        count
 |          Maximum number of occurrences to replace.
 |          -1 (the default value) means replace all occurrences.
 |      
 |      If the optional argument count is given, only the first count occurrences are
 |      replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Raises ValueError when the substring is not found.
 |  
 |  rjust(self, width, fillchar=' ', /)
 |      Return a right-justified string of length width.
 |      
 |      Padding is done using the specified fill character (default is a space).
 |  
 |  rpartition(self, sep, /)
 |      Partition the string into three parts using the given separator.
 |      
 |      This will search for the separator in the string, starting at the end. If
 |      the separator is found, returns a 3-tuple containing the part before the
 |      separator, the separator itself, and the part after it.
 |      
 |      If the separator is not found, returns a 3-tuple containing two empty strings
 |      and the original string.
 |  
 |  rsplit(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |        sep
 |          The delimiter according which to split the string.
 |          None (the default value) means split according to any whitespace,
 |          and discard empty strings from the result.
 |        maxsplit
 |          Maximum number of splits to do.
 |          -1 (the default value) means no limit.
 |      
 |      Splits are done starting at the end of the string and working to the front.
 |  
 |  rstrip(self, chars=None, /)
 |      Return a copy of the string with trailing whitespace removed.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(self, /, sep=None, maxsplit=-1)
 |      Return a list of the words in the string, using sep as the delimiter string.
 |      
 |      sep
 |        The delimiter according which to split the string.
 |        None (the default value) means split according to any whitespace,
 |        and discard empty strings from the result.
 |      maxsplit
 |        Maximum number of splits to do.
 |        -1 (the default value) means no limit.
 |  
 |  splitlines(self, /, keepends=False)
 |      Return a list of the lines in the string, breaking at line boundaries.
 |      
 |      Line breaks are not included in the resulting list unless keepends is given and
 |      true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(self, chars=None, /)
 |      Return a copy of the string with leading and trailing whitespace remove.
 |      
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(self, /)
 |      Convert uppercase characters to lowercase and lowercase characters to uppercase.
 |  
 |  title(self, /)
 |      Return a version of the string where each word is titlecased.
 |      
 |      More specifically, words start with uppercased characters and all remaining
 |      cased characters have lower case.
 |  
 |  translate(self, table, /)
 |      Replace each character in the string using the given translation table.
 |      
 |        table
 |          Translation table, which must be a mapping of Unicode ordinals to
 |          Unicode ordinals, strings, or None.
 |      
 |      The table must implement lookup/indexing via __getitem__, for instance a
 |      dictionary or list.  If this operation raises LookupError, the character is
 |      left untouched.  Characters mapped to None are deleted.
 |  
 |  upper(self, /)
 |      Return a copy of the string converted to uppercase.
 |  
 |  zfill(self, width, /)
 |      Pad a numeric string with zeros on the left, to fill a field of the given width.
 |      
 |      The string is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> 
>>> a
'hello this is replace method in string'
>>> a.rindex(g)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    a.rindex(g)
NameError: name 'g' is not defined
>>> a.index("g")
37
>>> a.rindex("g")
37
>>> a
'hello this is replace method in string'
>>> a = a.center("50","-")
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a = a.center("50","-")
TypeError: 'str' object cannot be interpreted as an integer
>>> a=a.center(50,"-")
>>> a
'------hello this is replace method in string------'
>>> a.lstrip()
'------hello this is replace method in string------'
>>> a.lstrip(5)
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    a.lstrip(5)
TypeError: lstrip arg must be None or str
>>> a.lstrip("-")
'hello this is replace method in string------'
>>> a
'------hello this is replace method in string------'
>>> a="hello"
>>> a.startswith()
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a.startswith()
TypeError: startswith() takes at least 1 argument (0 given)
>>> a.startswith("h")
True
>>> a.endswith("h")
False
>>> 
