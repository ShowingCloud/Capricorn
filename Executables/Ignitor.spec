srcdir = 'C:\\Work\\Capricorn\\Device'


# -*- mode: python -*-
a = Analysis([os.path.join (srcdir, 'fireNow.py')],
             pathex=['C:\\Python27\\pyinstaller'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts + [('O', '', 'OPTION')],
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\FireNow', 'FireNow.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'FireNow'))

exe2 = EXE(pyz,
           a.scripts + [('O', '', 'OPTION')],
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           debug=False,
           console=False,
           name=os.path.join('dist', 'FireNow.exe'))

exe3 = EXE(pyz,
           a.scripts + [('O', '', 'OPTION')],
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           debug=True,
           console=True,
           name=os.path.join('dist', 'FireNow.debug.exe'))


b = Analysis([os.path.join (srcdir, 'fireDelayed.py')],
             pathex=['C:\\Python27\\pyinstaller'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(b.pure)
exe = EXE(pyz,
          b.scripts + [('O', '', 'OPTION')],
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\FireDelayed', 'FireDelayed.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True)
coll = COLLECT(exe,
               b.binaries,
               b.zipfiles,
               b.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'FireDelayed'))

exe2 = EXE(pyz,
           b.scripts + [('O', '', 'OPTION')],
           b.binaries,
           b.zipfiles,
           b.datas,
           strip=None,
           upx=True,
           debug=False,
           console=False,
           name=os.path.join('dist', 'FireDelayed.exe'))

exe3 = EXE(pyz,
           b.scripts + [('O', '', 'OPTION')],
           b.binaries,
           b.zipfiles,
           b.datas,
           strip=None,
           upx=True,
           debug=True,
           console=True,
           name=os.path.join('dist', 'FireDelayed.debug.exe'))


c = Analysis([os.path.join (srcdir, 'connectTest.py')],
             pathex=['C:\\Python27\\pyinstaller'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(c.pure)
exe = EXE(pyz,
          c.scripts + [('O', '', 'OPTION')],
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\ConnectTest', 'ConnectTest.exe'),
          debug=True,
          strip=None,
          upx=True,
          console=True)
coll = COLLECT(exe,
               c.binaries,
               c.zipfiles,
               c.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'ConnectTest'))

exe2 = EXE(pyz,
           c.scripts + [('O', '', 'OPTION')],
           c.binaries,
           c.zipfiles,
           c.datas,
           strip=None,
           upx=True,
           debug=False,
           console=False,
           name=os.path.join('dist', 'ConnectTest.exe'))

exe3 = EXE(pyz,
           c.scripts + [('O', '', 'OPTION')],
           c.binaries,
           c.zipfiles,
           c.datas,
           strip=None,
           upx=True,
           debug=True,
           console=True,
           name=os.path.join('dist', 'ConnectTest.debug.exe'))
