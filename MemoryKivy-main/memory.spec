from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['memory.py'],
             pathex=['C:\\lotery'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='memory',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )

a.datas += [('Code\memory.kv', 'C:\\lotery\\memory.kv', 'DATA')]

coll = COLLECT(exe,
               Tree('C:\\lotery\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='memory')
