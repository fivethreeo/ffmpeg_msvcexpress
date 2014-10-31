toolsets = vs2012;

vs2012.option.ClCompile.RuntimeLibrary = MultiThreaded;

win32-subsystem=windows;

env = dict(
    ARCH="x86",
    CC="c99wrap cl",
    CXX="c99wrap cl",
    AS="c99wrap cl",
    LD="link",
    DEPCC="c99wrap cl",
    DEPCCFLAGS="-nologo %(CPPFLAGS)s",
    DEPAS="c99wrap cl",
    DEPASFLAGS="-nologo %(CPPFLAGS)s,
    YASM="yasm",
    DEPYASM="yasm",
    AR="lib",
    ARFLAGS="-nologo",
    AR_O="-out:%s",
    RANLIB=":",
    CPPFLAGS=" -D_ISOC99_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_WIN32_WINNT=0x0502 -Dstrtod=avpriv_strtod -Dsnprintf=avpriv_snprintf -D_snprintf=avpriv_snprintf -Dvsnprintf=avpriv_vsnprintf",
    CFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64    -Z7 -W4 -wd4244 -wd4127 -wd4018 -wd4389 -wd4146 -wd4057 -wd4204 -wd4706 -wd4305 -wd4152 -wd4324 -we4013 -wd4100 -wd4214 -wd4554 -wd4273 -wd4701 -O2   -Oy-",
    CXXFLAGS="  -D__STDC_CONSTANT_MACROS",
    ASFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64  -Z7",
    AS_C="-c",
    AS_O="-Fo%s",
    CC_C="-c",
    CC_E="-P -Fi%s",
    CC_O="-Fo%s",
    CXX_C="-c",
    CXX_O="-o %s",
    LD_O="-out:%s",
    LD_LIB="lib%s.a",
    LD_PATH="-libpath:",
    LDFLAGS=" -nologo -debug",
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
    CCDEP="%%(DEP%s)s %%(DEP%sFLAGS)s %%(%sDEP_FLAGS)s %%%s",
    CXXDEP="",
    CCDEP_FLAGS="%(CPPFLAGS)s %(CFLAGS)s -showIncludes -Zs",
    ASDEP="%%(DEP%s)s %%(DEP%sFLAGS)s %%(%sDEP_FLAGS)s %%%s",
    ASDEP_FLAGS="%(CPPFLAGS)s %(CFLAGS)s -showIncludes -Zs",
    CC_DEPFLAGS="",
    AS_DEPFLAGS="",
    HOSTCC="c99wrap cl",
    HOSTLD="link",
    HOSTCFLAGS=" ",
    HOSTCPPFLAGS=" -D_ISOC99_SOURCE",
    HOSTEXESUF=".exe",
    HOSTLDFLAGS=" ",
    HOSTLIBS="-lm",
    DEPHOSTCC="c99wrap cl",
    DEPHOSTCCFLAGS=" %(HOSTCCFLAGS)s",
    HOSTCCDEP="%%(DEP%s)s %%(DEP%sFLAGS)s %%(%sDEP_FLAGS)s %%%s",
    HOSTCCDEP_FLAGS="-MM",
    HOSTCC_DEPFLAGS="",
    HOSTCC_C="-c",
    HOSTCC_O="-o %s",
    HOSTLD_O="-o %s"
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

