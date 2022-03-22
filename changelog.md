# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [1.5.5] - 2020-03-22
(Poikilos; based on the upstream version 1.5.4: The wayback machine copy from https://web.archive.org/web/20040331032128/home.t-online.de/home/Ulrich.Herold/pydebug.py internally dated "1997/1998")

### Added
- Add a preliminary setup.py (only usable for tracking dependencies and for other self-documentation for now).
- Describe the `__disclaimer__` in a comment for clarification of the origin and name of the license.
  - The license name has also been added as a title in the new license.txt.

### Fixed
- Fix inconsistent use of tabs and spaces.
- Remove an invalid character (non-Latin accented `i`).
- Change the encoding to UTF-8 from none (none according to python2, default ISO-8859-1 according to Geany).
- Make Python 3 compatibility fixes:
  - Run 2to3.
  - Manually change Python 2 string exceptions to Python 3 exceptions.
  - Use of ListType changed to list, IntType changed to int, etc. (See the `BasicTypes` list).
    - Remove `LongType` since `long` was merged with `int` in Python 3.
  - Make an atoi and atof function to fix Python 1 code :(.
  - Change uses of build-in methods `locals` and `globals` as variable names to `theLocals` and `theGlobals`, respectively.
  - Change `execfile(...)` (as string in a `run` command :( ) to `exec(open(...).read())`.
