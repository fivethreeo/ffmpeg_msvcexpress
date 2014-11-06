/*

*/

#ifndef __STDC_CONSTANT_MACROS
  #define __STDC_CONSTANT_MACROS
#endif

#pragma comment(lib,"libswscale.a")
#pragma comment(lib,"libswresample.a")

#pragma comment(lib,"libavcodec.a")
#pragma comment(lib,"libavdevice.a")
#pragma comment(lib,"libavformat.a")
#pragma comment(lib,"libavutil.a")

#define WIN32_LEAN_AND_MEAN

#include "windows.h"

#ifdef __cplusplus

extern "C" {
    
#include <libavcodec/avcodec.h>
#include <libavformat/avformat.h>
    
#endif

    INT WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR strCmdLine, INT)

    {

        av_register_all();
        MessageBox(NULL, "An exception has occured!", "An exception has occured!", MB_OK | MB_ICONERROR | MB_TASKMODAL);

        return 0;
    }

#ifdef __cplusplus
}
#endif