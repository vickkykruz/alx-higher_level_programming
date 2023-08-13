#include <stdio.h>
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
	PyListObject *list;
	long int i, size;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
