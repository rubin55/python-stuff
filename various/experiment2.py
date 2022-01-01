# PulseAudio Source list:

import time
import sys
from ctypes import *
PA = CDLL('libpulse.so.0')
PA_CONTEXT_UNCONNECTED = 0
PA_CONTEXT_CONNECTING = 1
PA_CONTEXT_AUTHORIZING = 2
PA_CONTEXT_SETTING_NAME = 3
PA_CONTEXT_READY = 4
PA_CONTEXT_FAILED = 5
PA_CONTEXT_TERMINATED = 6
PA_OPERATION_RUNNING = 0
PA_OPERATION_DONE = 1
PA_OPERATION_CANCELLED = 2
STRING = c_char_p
size_t = c_ulong
uint32_t = c_uint32
uint8_t = c_uint8
class pa_mainloop_api(Structure):
    pass
class pa_threaded_mainloop(Structure):
    pass
pa_threaded_mainloop._fields_ = []
pa_threaded_mainloop_new = PA.pa_threaded_mainloop_new
pa_threaded_mainloop_new.restype = POINTER(pa_threaded_mainloop)
pa_threaded_mainloop_new.argtypes = []
pa_threaded_mainloop_free = PA.pa_threaded_mainloop_free
pa_threaded_mainloop_free.restype = None
pa_threaded_mainloop_free.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_start = PA.pa_threaded_mainloop_start
pa_threaded_mainloop_start.restype = c_int
pa_threaded_mainloop_start.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_stop = PA.pa_threaded_mainloop_stop
pa_threaded_mainloop_stop.restype = None
pa_threaded_mainloop_stop.argtypes = [POINTER(pa_threaded_mainloop)]
pa_threaded_mainloop_get_api = PA.pa_threaded_mainloop_get_api
pa_threaded_mainloop_get_api.restype = POINTER(pa_mainloop_api)
pa_threaded_mainloop_get_api.argtypes = [POINTER(pa_threaded_mainloop)]
class pa_context(Structure):
    pass
pa_context._fields_ = []
class pa_spawn_api(Structure):
    pass
class pa_stream(Structure):
    pass
pa_stream._fields_ = []
class pa_operation(Structure):
        pass
class pa_source_info(Structure):
    pass
pa_source_info._fields_ = [
    ('name', STRING),
    ('index', uint32_t),
    ('description', STRING),
]
pa_context_flags = c_int
pa_context_flags_t = pa_context_flags
pa_context_state = c_int
pa_context_state_t = pa_context_state
pa_context_notify_cb_t = CFUNCTYPE(None, POINTER(pa_context), c_void_p)
pa_context_success_cb_t = CFUNCTYPE(None, POINTER(pa_context), c_int, c_void_p)
pa_stream_success_cb_t = CFUNCTYPE(None, POINTER(pa_stream), c_int, c_void_p)
pa_stream_request_cb_t = CFUNCTYPE(None, POINTER(pa_stream), size_t, c_void_p)
pa_stream_notify_cb_t = CFUNCTYPE(None, POINTER(pa_stream), c_void_p)
pa_source_info_cb_t = CFUNCTYPE(None, POINTER(pa_context), POINTER(pa_source_info), c_int, c_void_p)

pa_context_new = PA.pa_context_new
pa_context_new.restype = POINTER(pa_context)
pa_context_new.argtypes = [POINTER(pa_mainloop_api), STRING]
pa_context_connect = PA.pa_context_connect
pa_context_connect.restype = c_int
pa_context_connect.argtypes = [POINTER(pa_context), STRING, pa_context_flags_t, POINTER(pa_spawn_api)]
pa_context_set_state_callback = PA.pa_context_set_state_callback
pa_context_set_state_callback.restype = None
pa_context_set_state_callback.argtypes = [POINTER(pa_context), pa_context_notify_cb_t, c_void_p]
pa_context_get_state = PA.pa_context_get_state
pa_context_get_state.restype = pa_context_state_t
pa_context_get_state.argtypes = [POINTER(pa_context)]
pa_stream_set_state_callback = PA.pa_stream_set_state_callback
pa_stream_set_state_callback.restype = None
pa_stream_set_state_callback.argtypes = [POINTER(pa_stream), pa_stream_notify_cb_t, c_void_p]

pa_context_get_source_info_list = PA.pa_context_get_source_info_list
pa_context_get_source_info_list.restype = POINTER(pa_operation)
pa_context_get_source_info_list.argtypes = [POINTER(pa_context), pa_source_info_cb_t, c_void_p]

def pa_state_cb(context, userdata):
    global pa_state
    state = pa_context_get_state(context)
    if state in [PA_CONTEXT_UNCONNECTED, PA_CONTEXT_CONNECTING, PA_CONTEXT_AUTHORIZING,
        PA_CONTEXT_SETTING_NAME]:
        pa_state = 0
    elif state == PA_CONTEXT_FAILED:
        pa_state = 2
    elif state == PA_CONTEXT_READY:
        pa_state = 1
    return  0

def pa_sourcelist_cb(context, source_info, eol, userdata):
    if eol==0:
        print("IDX:", source_info.contents.index, " ", source_info.contents.name, "--", source_info.contents.description)
    return  0

pa_ml = pa_threaded_mainloop_new()
pa_mlapi = pa_threaded_mainloop_get_api(pa_ml)

pa_ctx = pa_context_new(pa_mlapi, b"kazam-pulse")

error = -1
pa_state = 0
if pa_context_connect(pa_ctx, None, 0, None)!=0:
    print("cannot connect..")
    sys.exit(1)

pa_context_set_state_callback(pa_ctx, pa_context_notify_cb_t(pa_state_cb), None)
ret = pa_threaded_mainloop_start(pa_ml)

ctc = pa_context_get_state(pa_ctx)

time.sleep(1)
pa_context_get_source_info_list(pa_ctx, pa_source_info_cb_t(pa_sourcelist_cb), None);
time.sleep(1)
