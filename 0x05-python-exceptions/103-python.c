#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *item;

    size = Py_SIZE(p);
    allocated = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; ++i)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    size = Py_SIZE(p);
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", PyBytes_AS_STRING(p));
    printf("  first %ld bytes:", size + 1 < 10 ? size + 1 : 10);

    string = PyBytes_AS_STRING(p);
    for (i = 0; i < size + 1 && i < 10; ++i)
        printf(" %02x", string[i] & 0xFF);
    printf("\n");
}

/**
 * print_python_float - Prints information about Python float
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;

    printf("[.] float object info\n");
    if (PyFloat_Check(p))
        printf("  value: %f\n", f->ob_fval);
    else
        printf("  [ERROR] Invalid Float Object\n");
}
