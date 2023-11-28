#include <Python.h>

void print_python_string(PyObject *p) {
    printf("[.] string object info\n");

    if (PyUnicode_Check(p)) {
        if (PyUnicode_IS_COMPACT_ASCII(p)) {
            printf("  type: compact ascii\n");
        } else if (PyUnicode_IS_COMPACT(p)) {
            printf("  type: compact unicode object\n");
        } else {
            printf("  type: compact unknown\n");
        }

        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        printf("  length: %zd\n", length);

        const char *value = PyUnicode_AsUTF8(p);
        printf("  value: %s\n", value);
    } else {
        printf("  [ERROR] Invalid String Object\n");
    }
}

int main(void) {
    Py_Initialize();

    PyObject *p1 = PyUnicode_DecodeASCII("The spoon does not exist", 24, NULL);
    PyObject *p2 = PyUnicode_DecodeUTF8("ложка не существует", 19, NULL);
    PyObject *p3 = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, NULL);
    PyObject *p4 = PyUnicode_DecodeUTF8("勺子不存在", 5, NULL);
    PyObject *p5 = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, NULL);
    PyObject *p6 = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, NULL);
    PyObject *p7 = PyBytes_FromString("The spoon does not exist");

    print_python_string(p1);
    print_python_string(p2);
    print_python_string(p3);
    print_python_string(p4);
    print_python_string(p5);
    print_python_string(p6);
    print_python_string(p7);

    Py_XDECREF(p1);
    Py_XDECREF(p2);
    Py_XDECREF(p3);
    Py_XDECREF(p4);
    Py_XDECREF(p5);
    Py_XDECREF(p6);
    Py_XDECREF(p7);

    Py_Finalize();

    return 0;
}
