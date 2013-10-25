# Codename, should be changed when released
APPNAME = "Fireworks"

import sys, os, shutil


# Use different APPDATA path in different platforms
if sys.platform == 'darwin':
	from AppKit import NSSearchPatchForDirectoriesInDomains
	appdata = os.path.join (NSSearchPathForDirectoriesInDomains (14, 1, True)[0], APPNAME)

elif sys.platform == 'win32':
	appdata = os.path.join (os.environ['APPDATA'], APPNAME)

else:
	appdata = os.path.expanduser (os.path.join ("~", "." + APPNAME))


# Check if we're running in a pyinstaller bundle
if getattr (sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname (__file__)


# Make the APPDATA directory, if necessary
if os.path.exists (appdata):
	if not os.path.isdir (appdata):
		os.remove (appdata)
		os.mkdir (appdata)
else:
	os.mkdir (appdata)


# Make subdirectories in APPDATA directory
for directory in ['local', 'proj', 'pdf']:
	subdir = os.path.join (appdata, directory)
	
	if os.path.exists (subdir):
		if not os.path.isdir (subdir):
			os.remove (subdir)
			os.mkdir (subdir)
	else:
		os.mkdir (subdir)


# Copy local database file only if it doesn't exist
if not os.path.exists (os.path.join (appdata, 'local', 'local.db')):
	shutil.copy2 (os.path.join (basedir, 'Resource', 'local.db'), os.path.join (appdata, 'local'))
