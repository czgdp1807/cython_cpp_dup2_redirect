#cython: language_level=3

cdef extern from "redirect_cpp.h":
    void redirect_stdout_to_file(const char* filepath)

def redirect(str filepath):
    redirect_stdout_to_file(filepath.encode('utf-8'))
