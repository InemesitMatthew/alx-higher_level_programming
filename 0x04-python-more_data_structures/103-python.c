#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);

    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (strcmp(Py_TYPE(item)->tp_name, "bytes") == 0) {
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_Size(item));
            printf("  trying string: %s\n", PyBytes_AsString(item));
            printf("  first 10 bytes: ");
            for (int j = 0; j < 10; j++) {
                printf("%02x ", (unsigned char)PyBytes_AsString(item)[j]);
            }
            printf("\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (int i = 0; i < 10; i++) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[i]);
    }
    printf("\n");
}
