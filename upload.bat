SET upload=%1
IF EXIST %upload%.csv ECHO Uploading %upload%.csv

PAUSE

@echo off

"C:\Program Files (x86)\WinSCP\WinSCP.com" ^
  /log="C:\Users\pbastien.CFGLOBAL\Dropbox\Squash Source\Docs\Programming\webscraper\upload.log" /ini=nul ^
  /command ^
    "open sftp://squash9:A%%7DH9nSJQCEoK@squashsource.com:2222/ -hostkey=""ssh-ed25519 255 /4ojnKIwhuAyvONfPWcK9mi8NOoydNFZcWIOl4uBcqk="" -privatekey=""C:\Program Files\PuTTY\keys\inmotion.ppk"" -rawsettings Cipher=""aes,chacha20,3des,WARN,des,blowfish,arcfour""" ^
    "lcd ""C:\Users\pbastien.CFGLOBAL\Dropbox\Squash Source\Docs\Programming\webscraper""" ^
    "cd /home/squash9/public_html/wp-content/uploads/wpallimport/files" ^
    "put %upload%.csv" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

PAUSE