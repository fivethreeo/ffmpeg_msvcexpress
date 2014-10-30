/*

*/
#include "windows.h"

#include "avcodec.h"
#include "avformat.h"

#ifdef __cplusplus
extern "C" {
#endif

    INT WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR strCmdLine, INT)

    {

        av_register_all();
        MessageBoxA(NULL, "An exception has occured!", "An exception has occured!", MB_OK | MB_ICONERROR | MB_TASKMODAL);

        return 0;
    }

#ifdef __cplusplus
}
#endif