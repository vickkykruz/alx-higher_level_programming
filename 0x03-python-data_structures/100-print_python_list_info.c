#include "lists.h"
#include <Python.h>
/**
 * print_python_list_info - This is a function tha prints the basic info of
 * the list
 * @p: This is an argument that reprsent the python object
 *
 * Return: This function return a void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, idx = 0, allocated;
	PyObject *element;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", list->allocated);

	while (idx < size)
	{
		element = PyList_GET_ITEM(p, idx);
		printf("Element %ld: %s\n", idx, element->ob_type->tp_name);
		idx++;
	}
}
