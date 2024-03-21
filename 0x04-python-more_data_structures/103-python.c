#include <Python.h>
#include <studio.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid Python list\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Python bytes object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    Py_ssize_t size = PyBytes_Size(p);
    if (size > 10)
        size = 10;
    unsigned char *str = (unsigned char *)PyBytes_AsString(p);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02hhx", str[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

