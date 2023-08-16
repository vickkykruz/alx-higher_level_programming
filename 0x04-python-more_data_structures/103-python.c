#include <stdio.h>
#include <Python.h>
/**
 * print_python_bytes - This is a function that print bytes information
 * @p: This is an argument that represent the python object
 *
 * Return: This function return a void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("   [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("   size: %ld\n", size);
	printf("   trying string: %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("   first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (str[i] >= 0)
			printf("  %02x", str[i]);
		else
			printf("  %02x", 256 + str[i]);
	printf("\n");
}
/**
 * print_python_list - This is a function that print the list information
 * @p: This is an argument the Python Objetct
 *
 * Return: This function return a void
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	long int i, size;
	PyObject *obj;

	list = (PyListObject *)p;
	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
