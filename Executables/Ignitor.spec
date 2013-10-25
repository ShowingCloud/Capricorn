srcdir = '..'


# -*- mode: python -*-
a = Analysis([os.path.join (srcdir, 'FireworksMain.py')],
             pathex=['C:\\Python27\\pyinstaller'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts + [('O', '', 'OPTION')],
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Capricorn', 'Capricorn.exe'),
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
               name=os.path.join('dist', 'Capricorn'))

exe2 = EXE(pyz,
           a.scripts + [('O', '', 'OPTION')],
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           debug=False,
           console=False,
           name=os.path.join('dist', 'Capricorn.exe'))

exe3 = EXE(pyz,
           a.scripts + [('O', '', 'OPTION')],
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           debug=True,
           console=True,
           name=os.path.join('dist', 'Capricorn.debug.exe'))
