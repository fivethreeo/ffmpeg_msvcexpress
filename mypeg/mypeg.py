toolsets = vs2012;

vs2012.option.ClCompile.RuntimeLibrary = MultiThreaded;

win32-subsystem=windows;

env = dict(
    CC="c99wrap cl",
    CXX="CC="c99wrap cl",
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
    AR_O="-out:%1",
    RANLIB=":",
    CPPFLAGS=" -D_ISOC99_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE -D_WIN32_WINNT=0x0502 -Dstrtod=avpriv_strtod -Dsnprintf=avpriv_snprintf -D_snprintf=avpriv_snprintf -Dvsnprintf=avpriv_vsnprintf",
    CFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64    -Z7 -W4 -wd4244 -wd4127 -wd4018 -wd4389 -wd4146 -wd4057 -wd4204 -wd4706 -wd4305 -wd4152 -wd4324 -we4013 -wd4100 -wd4214 -wd4554 -wd4273 -wd4701 -O2   -Oy-",
    CXXFLAGS="  -D__STDC_CONSTANT_MACROS",
    ASFLAGS=" -nologo -D_USE_MATH_DEFINES -D_CRT_SECURE_NO_WARNINGS -Dinline=__inline -FIstdlib.h -Dstrtoll=_strtoi64  -Z7",
    AS_C="-c",
    AS_O="-Fo%1",
    CC_C="-c",
    CC_E="-P -Fi%1",
    CC_O="-Fo%1",
    CXX_C="-c",
    CXX_O="-o %1",
    LD_O="-out:%1",
    LD_LIB="lib%1.a",
    LD_PATH="-libpath:"
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

