#include <io.h>
#include <fcntl.h>
#include <stdio.h>

extern "C" void redirect_stdout_to_file(const char* filepath) {
    int file_fd = _open(filepath, _O_WRONLY | _O_CREAT | _O_TRUNC | _O_BINARY, 0666);
    if (file_fd == -1) {
        fprintf(stderr, "Failed to open file\n");
        return;
    }

    if (_dup2(file_fd, 1) == -1) {
        _close(file_fd);
        fprintf(stderr, "Failed to redirect stdout\n");
        return;
    }

    printf("[C++] stdout redirected via C++\\n");
    _close(file_fd);
}
