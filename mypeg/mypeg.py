#toolsets = vs2012;

#vs2012.option.ClCompile.RuntimeLibrary = MultiThreaded;

#win32-subsystem=windows;

env = dict(
    LIBDIR="%(DESTDIR)s%(prefix)s/lib",
    SHLIBDIR="%(DESTDIR)s%(prefix)s/bin",
    INCDIR="%(DESTDIR)s%(prefix)s/include",
    BINDIR="%(DESTDIR)s%(prefix)s/bin",
    DATADIR="%(DESTDIR)s%(prefix)s/share/ffmpeg",
    DOCDIR="%(DESTDIR)s%(prefix)s/share/doc/ffmpeg",
    MANDIR="%(DESTDIR)s%(prefix)s/share/man",
    CC_IDENT="Microsoft (R) C/C++ Optimizing Compiler Version 17.00.50727.1 for x86",
    ARCH="x86",
    INTRINSICS="none",
    CC="c99wrap cl",
    CXX="c99wrap cl",
    AS="c99wrap cl",
    LD="link",
    DEPCC="c99wrap cl",
    DEPCCFLAGS="-nologo %(CPPFLAGS)s",
    DEPAS="c99wrap cl",
    DEPASFLAGS="-nologo %(CPPFLAGS)s",
    YASM="yasm",
    DEPYASM="yasm",
    AR="lib",
    ARFLAGS="-nologo",
    AR_O="-out:$@",
    RANLIB=":",
    STRIP="echo skipping strip",
    CP="cp -p",
    LN_S="ln -s -f",
    CPPFLAGS=" -D_ISOC99_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_WIN32_WINNT=0x0502 -Dstrtod=avpriv_strtod -Dsnprintf=avpriv_snprintf -D_snprintf=avpriv_snprintf -Dvsnprintf=avpriv_vsnprintf",
    CFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64    -Z7 -W4 -wd4244 -wd4127 -wd4018 -wd4389 -wd4146 -wd4057 -wd4204 -wd4706 -wd4305 -wd4152 -wd4324 -we4013 -wd4100 -wd4214 -wd4554 -wd4273 -wd4701 -O2   -Oy-",
    CCFLAGS="",
    CXXFLAGS="  -D__STDC_CONSTANT_MACROS",
    ASFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64  -Z7",
    AS_C="-c",
    AS_O="-Fo%(ARCHIVE)s",
    CC_C="-c",
    CC_E="-P -Fi%(ARCHIVE)s",
    CC_O="-Fo%(ARCHIVE)s",
    CXX_C="-c",
    CXX_O="-o %(ARCHIVE)s",
    LD_O="-out:%(ARCHIVE)s",
    LD_LIB="lib%.a",
    LD_PATH="-libpath:",
    DLLTOOL="",
    WINDRES="windres",
    DEPWINDRES="c99wrap cl",
    DOXYGEN="doxygen",
    LDFLAGS=" -nologo -debug",
    LDEXEFLAGS="",
    SHFLAGS="-dll -def:$%(@:%(SLIBSUF)=.def) -implib:%(SUBDIR)s%(SLIBNAME:%(SLIBSUF)s=.lib)",
    ASMSTRIPFLAGS="",
    YASMFLAGS="-f win32  -DPREFIX",
    BUILDSUF="",
    PROGSSUF="",
    FULLNAME="%(NAME)s%(BUILDSUF)s",
    LIBPREF="lib",
    LIBSUF=".a",
    LIBNAME="%(LIBPREF)s%(FULLNAME)s%(LIBSUF)s",
    SLIBPREF="",
    SLIBSUF=".dll",
    EXESUF=".exe",
    EXTRA_VERSION="",
    CCDEP="%%(DEP%(TOOL)s)s %%(DEP%(TOOL)sFLAGS)s %%(%(TOOL)sDEP_FLAGS)s %%%%%%%%(SOURCE)s",
    CXXDEP="",
    CCDEP_FLAGS="%(CFLAGS)s -showIncludes -Zs",
    ASDEP="%(DEP%(TOOL)s)s %(DEP%(TOOL)sFLAGS)s %(%(TOOL)sDEP_FLAGS)s",
    ASDEP_FLAGS="%(CPPFLAGS)s %(CFLAGS)s -showIncludes -Zs",
    CC_DEPFLAGS="",
    AS_DEPFLAGS="",
    HOSTCC="c99wrap cl",
    HOSTLD="c99wrap cl",
    HOSTCFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64 -Dsnprintf=_snprintf  -W4 -wd4244 -wd4127 -wd4018 -wd4389 -wd4146 -wd4057 -wd4204 -wd4706 -wd4305 -wd4152 -wd4324 -we4013 -wd4100 -wd4214 -wd4554 -wd4273 -wd4701 -O3",
    HOSTCPPFLAGS=" -D_ISOC99_SOURCE -D_WIN32_WINNT=0x0502",
    HOSTEXESUF=".exe",
    HOSTLDFLAGS=" -nologo",
    HOSTLIBS="-lm",
    DEPHOSTCC="c99wrap cl",
    DEPHOSTCCFLAGS="-nologo %(HOSTCCFLAGS)s",
    HOSTCCDEP="%%(DEP%(TOOL)s)s %%(DEP%(TOOL)sFLAGS)s %%(%(TOOL)sDEP_FLAGS)s %%%%%%%%(SOURCE)s",
    HOSTCCDEP_FLAGS="%(CPPFLAGS)s %(CFLAGS)s -showIncludes -Zs",
    HOSTCC_DEPFLAGS="",
    HOSTCC_C="-c",
    HOSTCC_O="-Fo%(ARCHIVE)s",
    HOSTLD_O="-Fe%(ARCHIVE)s",
    TARGET_EXEC=" ",
    TARGET_PATH="%(CURDIR)s",
    TARGET_SAMPLES="%(SAMPLES)s",
    CFLAGSffplay="",
    ZLIB="zlib.lib",
    LIB_INSTALL_EXTRA_CMD='$%(RANLIB)s "%(LIBDIR)s/%(LIBNAME)s"',
    EXTRALIBS="vfw32.lib user32.lib gdi32.lib psapi.lib ole32.lib strmiids.lib uuid.lib ws2_32.lib psapi.lib advapi32.lib shell32.lib ",
    COMPAT_OBJS=" strtod.o msvcrt/snprintf.o",
    EXEOBJS="",
    INSTALL="install",
    LIBTARGET="",
    SLIBNAME="%(SLIBPREF)s%(FULLNAME)s%(SLIBSUF)s",
    SLIBNAME_WITH_VERSION="%(SLIBPREF)s%(FULLNAME)s-%(LIBVERSION)s%(SLIBSUF)s",
    SLIBNAME_WITH_MAJOR="%(SLIBPREF)s%(FULLNAME)s-%(LIBMAJOR)s%(SLIBSUF)s",
    SLIB_CREATE_DEF_CMD="%(SRC_PATH)s/compat/windows/makedef %(SUBDIR)slib%(NAME)s.ver %(OBJS)s > $%(@:%(SLIBSUF)s=.def)",
    SLIB_EXTRA_CMD="",
    SLIB_INSTALL_NAME="%(SLIBNAME_WITH_MAJOR)s",
    SLIB_INSTALL_LINKS="",
    SLIB_INSTALL_EXTRA_LIB="%(SLIBNAME_WITH_MAJOR:%(SLIBSUF)s=.def)",
    SLIB_INSTALL_EXTRA_SHLIB="%(SLIBNAME:%(SLIBSUF)s=.lib)",
    SAMPLES="%(FATE_SAMPLES)s",
    NOREDZONE_FLAGS="-mno-red-zone"
)

sources = [
  "src/mypeg.cpp"
]

includedirs = [
  "../ffmpeg",
  "../ffmpeg/libavcodec",
  "../ffmpeg/libavdevice",
  "../ffmpeg/libavfilter",
  "../ffmpeg/libavformat",
  "../ffmpeg/libavresample",
  "../ffmpeg/libavutil",
  "../ffmpeg/libpostproc",
  "../ffmpeg/libswresample",
  "../ffmpeg/libswscale"
]
    
includedirs += [
  "../msinttypes"
]

libdirs = [
  "../ffmpeg/libavcodec",
  "../ffmpeg/libavdevice",
  "../ffmpeg/libavfilter",
  "../ffmpeg/libavformat",
  "../ffmpeg/libavresample",
  "../ffmpeg/libavutil",
  "../ffmpeg/libpostproc",
  "../ffmpeg/libswresample",
  "../ffmpeg/libswscale"
]
    
libs = [
  "libavcodec",
  "libavdevice",
  "libavfilter",
  "libavformat",
  "libavutil",
  "libswresample",
  "libswscale"
]

def make_dep_cmd(TOOL):
  tool_cmd = env['%sDEP' % TOOL] % dict(TOOL=TOOL)
  tool_cmd = tool_cmd % env
  tool_cmd = tool_cmd % env
  return tool_cmd
  
def make_compile_cmd(TOOL):
  tool_cmd = "%%(%(TOOL)s)s %%(%(TOOL)sFLAGS)s %%(%(TOOL)s_DEPFLAGS)s %%(%(TOOL)s_C)s %%(%(TOOL)s_O)s %%%%(SOURCE)s" % dict(TOOL=TOOL)
  tool_cmd = tool_cmd % env
  return tool_cmd

#CMDS = 
print make_dep_cmd('CC')
print make_compile_cmd('CC')