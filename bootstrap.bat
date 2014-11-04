@echo off
setlocal EnableDelayedExpansion

if 1==0 (
echo When the msys shell appears do:
echo.
echo movelink 
echo So the correct link is used
echo.
echo fconfigure
echo This takes some time without any output
echo.
echo make
echo Once done building
echo.
echo movelinkback
echo To make link the regular link again
echo.
echo Utils
echo movealib
echo moveliba
echo To rename a to lib and vice versa
echo.
echo For 64bit builds using vs express 2010 install:
echo http://www.microsoft.com/en-us/download/details.aspx?id=8279
echo and
echo http://www.microsoft.com/en-us/download/details.aspx?id=4422
echo.

)

rem -------------------------------------------------------------------------
rem To build clang if needed
if 1==0 (
  rem 1==0 off 1==1 on
  git clone https://github.com/llvm-mirror/llvm.git llvm
  pushd llvm\tools
  git clone https://github.com/llvm-mirror/clang.git clang
  popd
  
  call :DownloadFile http://www.cmake.org/files/v3.0/cmake-3.0.2-win32-x86.exe cmake-3.0.2-win32-x86.exe
  cmake-3.0.2-win32-x86.exe
  
  md build
  cd build
  cmake -G "Visual Studio 11" ..\llvm
)

rem Build c99 to c89 if needed, but found some binaries below :)
rem -------------------------------------------------------------------------

if 1==1 (

  rem 1==0 off 1==1 on

  if not exist "c99-to-c89\." (
    call :DownloadFile https://github.com/libav/c99-to-c89/releases/download/release-1.0.2/c99-to-c89-1.0.2.zip c99-to-c89.zip
    call :UnzipFile c99-to-c89.zip c99-to-c89
    del c99-to-c89.zip
  )

  if not exist "msinttypes\." (
    call :DownloadFile https://msinttypes.googlecode.com/files/msinttypes-r26.zip msinttypes.zip
    call :UnzipFile msinttypes.zip msinttypes
    del msinttypes.zip
  )

  if not exist "yasm32\." (
    call :DownloadFile http://www.tortall.net/projects/yasm/releases/yasm-1.3.0-win32.exe yasm.exe
    md yasm32
    move yasm.exe yasm32\yasm.exe > nul
  )

  if not exist "yasm64\." (
    call :DownloadFile http://www.tortall.net/projects/yasm/releases/yasm-1.3.0-win64.exe yasm.exe
    md yasm64
    move yasm.exe yasm64\yasm.exe > nul
  )
  
  if not exist "zlib\." (
    call :DownloadFile http://zlib.net/zlib128.zip zlib128.zip
    call :UnzipFile zlib128.zip zlib
    del zlib128.zip
  )

  if not exist "ffmpeg\." (
    git clone https://github.com/FFmpeg/FFmpeg.git ffmpeg
  )

  set /P c="Install MinGW (y/n)? "
  
  if /I "!c!" EQU "Y" (
    call :DownloadFile http://cznic.dl.sourceforge.net/project/mingw/Installer/mingw-get-setup.exe mingw-get-setup.exe
    mingw-get-setup.exe
    del mingw-get-setup.exe  
  ) 

)

set /p MinGWPath="Enter MinGW path (enter for default C:\MinGW\): "

if not defined MinGWPath (
   set MinGWPath=C:\MinGW\
)

for /r %MinGWPath% %%a in (*) do if "%%~nxa"=="msys.bat" set MsysPath=%%~dpnxa

if defined MsysPath (
  echo msys.bat found at %MsysPath%
  echo.
) else (
  echo msys.bat not found in %MinGWPath% make sure the directory is correct and MinWG is installed
  echo.
)

set /P ARCH="64 or 32 bit build? (64/32) "

if /I "!ARCH!" EQU "32" (
   goto ARCH32
)
if /I "!ARCH!" EQU "64" (
   goto ARCH64
)
goto :EOF
  
:ARCH32
    if defined VS100COMNTOOLS (
      echo Microsft Visual Studio 2010 found at:
      echo "%VS100COMNTOOLS%"
      echo.
      set /P cmn10="Use Microsft Visual Studio 2010 compile and link? (y/n) "
      
      if /I "!cmn10!" EQU "Y" (
        echo Using Microsft Visual Studio 2010
        echo.
        set "COMNTOOLS=%VS100COMNTOOLS%"
      )  
    )
    if defined VS110COMNTOOLS (
      echo Microsft Visual Studio 2012 found at:
      echo "%VS110COMNTOOLS%"
      echo.
      set /P cmn11="Use Microsft Visual Studio 2012 compile and link? (y/n) "
      
      if /I "!cmn11!" EQU "Y" (
        echo Using Microsft Visual Studio 2012
        echo.
        set "COMNTOOLS=%VS110COMNTOOLS%"
      )   
    )
   
    if defined COMNTOOLS (
      endlocal
      echo "Calling %COMNTOOLS%vsvars32.bat"
      call "%COMNTOOLS%vsvars32.bat" > nul'
      setlocal
      echo.
    ) else (
      echo Microsft Visual Studio not found
      echo.
      pause > nul
    )
    set TARGETOS=win32
    set TARGETARCH=i386
    
goto STARTMSYS

:ARCH64
  if not exist "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" (
    echo Windows SDK not found
    echo.
    pause > nul
  )
  echo "Calling C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd /x64"
  endlocal
  call "C:\Program Files\Microsoft SDKs\Windows\v7.1\Bin\SetEnv.cmd" /x64 > nul
  setlocal
  echo.
  set TARGETOS=win64
  set TARGETARCH=i686
    
goto STARTMSYS
  
:STARTMSYS

echo alias fconfigure="./configure --toolchain=msvc --arch=%TARGETARCH% --target-os=%TARGETOS% --prefix=`pwd`/build --enable-static --disable-shared" > ffmpeg\.profile
echo alias movelink="mv /usr/bin/link /usr/bin/oldlink" >> ffmpeg\.profile
echo alias movelinkback="mv /usr/bin/oldlink /usr/bin/link" >> ffmpeg\.profile
echo alias movealib="find . -name *.a | sed -e 'p;s/\.a$/.lib/' | xargs -n2 mv" >> ffmpeg\.profile
echo alias moveliba="find . -name *.lib | sed -e 'p;s/\.lib$/.a/' | xargs -n2 mv" >> ffmpeg\.profile

set INCLUDE=%CD%\msinttypes;%CD%\ffmpeg;%INCLUDE%
set PATH=%PATH%;%CD%\yasm%ARCH%;%CD%\c99-to-c89

Setlocal

set /P msysstart="Start msys shell? (y/n) "

if /I "!msysstart!" EQU "Y" (
  set HOME=.\ffmpeg\
  echo "Calling %MsysPath%"
  call "%MsysPath%"
)   
endlocal

goto :EOF

:UnZipFile <ZipFile> <ExtractTo>
rem Windows has no built-in unzip, so generate a VBS script to do it:
rem -------------------------------------------------------------------------
set UZIP_SCRIPT=unzip.vbs
if exist %UZIP_SCRIPT% del /f /q %UZIP_SCRIPT%
echo Option Explicit                                                     > %UZIP_SCRIPT%
echo Dim args, fso, ExtractTo, FilesInZip, objShell, Zipfile            >> %UZIP_SCRIPT%
echo.                                                                   >> %UZIP_SCRIPT%
echo Set args = Wscript.Arguments                                       >> %UZIP_SCRIPT%
echo Set fso = CreateObject("Scripting.FileSystemObject")               >> %UZIP_SCRIPT%
echo ZipFile = fso.GetAbsolutePathName(args(0))                         >> %UZIP_SCRIPT%
echo ExtractTo = fso.GetAbsolutePathName(args(1))                       >> %UZIP_SCRIPT%
echo If NOT fso.FolderExists(ExtractTo) Then                            >> %UZIP_SCRIPT%
echo    fso.CreateFolder(ExtractTo)                                     >> %UZIP_SCRIPT%
echo End If                                                             >> %UZIP_SCRIPT%
echo Set objShell = CreateObject("Shell.Application")                   >> %UZIP_SCRIPT%
echo Set FilesInZip = objShell.NameSpace(ZipFile).items                 >> %UZIP_SCRIPT%
echo objShell.NameSpace(ExtractTo).CopyHere(FilesInZip)                 >> %UZIP_SCRIPT%
echo Set fso = Nothing                                                  >> %UZIP_SCRIPT%
echo Set objShell = Nothing                                             >> %UZIP_SCRIPT%
rem -------------------------------------------------------------------------

cscript //nologo %UZIP_SCRIPT% %1 %2
if exist %UZIP_SCRIPT% del /f /q %UZIP_SCRIPT%
goto :EOF

:DownloadFile <DownloadFrom> <SaveTo> <HexBase>
rem Windows has no built-in wget or curl, so generate a VBS script to do it:
rem -------------------------------------------------------------------------
set DLOAD_SCRIPT=download.vbs
if exist %DLOAD_SCRIPT% del /f /q %DLOAD_SCRIPT%
echo Option Explicit                                                     > %DLOAD_SCRIPT%
echo Dim args, http, fileSystem, adoStream, url, target, status         >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo Set args = Wscript.Arguments                                       >> %DLOAD_SCRIPT%
echo Set http = CreateObject("WinHttp.WinHttpRequest.5.1")              >> %DLOAD_SCRIPT%
echo If args.Count=3 Then                                               >> %DLOAD_SCRIPT%
echo    url = ToAscii(args(0))                                          >> %DLOAD_SCRIPT%
echo Else                                                               >> %DLOAD_SCRIPT%
echo    url = args(0)                                                   >> %DLOAD_SCRIPT%
echo End If                                                             >> %DLOAD_SCRIPT%  
echo target = args(1)                                                   >> %DLOAD_SCRIPT%
echo WScript.Echo "Getting '" ^& target ^& "' from '" ^& url ^& "'..."  >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo http.Open "GET", url, False                                        >> %DLOAD_SCRIPT%
echo http.Send                                                          >> %DLOAD_SCRIPT%
echo status = http.Status                                               >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo If status ^<^> 200 Then                                            >> %DLOAD_SCRIPT%
echo 	WScript.Echo "FAILED to download: HTTP Status " ^& status         >> %DLOAD_SCRIPT%
echo 	WScript.Quit 1                                                    >> %DLOAD_SCRIPT%
echo End If                                                             >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo Set adoStream = CreateObject("ADODB.Stream")                       >> %DLOAD_SCRIPT%
echo adoStream.Open                                                     >> %DLOAD_SCRIPT%
echo adoStream.Type = 1                                                 >> %DLOAD_SCRIPT%
echo adoStream.Write http.ResponseBody                                  >> %DLOAD_SCRIPT%
echo adoStream.Position = 0                                             >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo Set fileSystem = CreateObject("Scripting.FileSystemObject")        >> %DLOAD_SCRIPT%
echo If fileSystem.FileExists(target) Then fileSystem.DeleteFile target >> %DLOAD_SCRIPT%
echo adoStream.SaveToFile target                                        >> %DLOAD_SCRIPT%
echo adoStream.Close                                                    >> %DLOAD_SCRIPT%
echo.                                                                   >> %DLOAD_SCRIPT%
echo Function ToAscii(hextext)                                          >> %DLOAD_SCRIPT%
echo   Dim y, asciiOUT                                                  >> %DLOAD_SCRIPT%
echo   asciiOUT = ""                                                    >> %DLOAD_SCRIPT%
echo   For y = 1 To Len(hextext)                                        >> %DLOAD_SCRIPT%
echo     asciiOUT = asciiOUT ^& Chr("&H" ^& Mid(hextext, y, 2))         >> %DLOAD_SCRIPT%
echo     y = y + 1                                                      >> %DLOAD_SCRIPT%
echo   Next                                                             >> %DLOAD_SCRIPT%
echo   ToAscii = asciiOUT                                               >> %DLOAD_SCRIPT%
echo End Function                                                       >> %DLOAD_SCRIPT%
rem -------------------------------------------------------------------------

cscript //nologo %DLOAD_SCRIPT% %1 %2 %3
if exist %DLOAD_SCRIPT% del /f /q %DLOAD_SCRIPT%
goto :EOF
