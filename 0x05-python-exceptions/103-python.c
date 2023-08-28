#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - This is a function that return the printed float
 * information
 * @p: This is an argument that reprsent the Python Object
 *
 * Return: This function return void
 */
void print_python_float(PyObject *p)
{
	char *ch;
	double val;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	val = ((PyFloatObject *)(p))->ob_fval;
	ch = PyOS_double_to_string(val, 'r', 0, Py_DISF_ADD_DOT_0, Py_DIST_FINITE);

	printf("  value: %s\n", ch);
	setbuf(stdout, NULL);
}
/**
 * print_python_bytes - This is a function that return the printed bytes
 * information
 * @p: This is an argument that reprsent the Python Object
 *
 * Return: This function return a void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int i, limit, size;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size %ld\n", size);
	printf("  trying string %s\n", str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (str[i] >= 0)
			printf("  %02x", str[i]);
		else
			printf("  %02x", 256 + str[i]);

	printf("\n");
	setbuf(stdout, NULL);
}
/**
 * print_python_list - This is a function that return the printed list
 * information
 * @p: This is an argument that reprsent the Python Object
 *
 * Return: This function return a void
 */
void print_python_list(PyObject *p)
{
	PyObject *obj;
	long int i, size;
	PyListObject *list;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	list = (PyListObject *)p;
	size = ((PyVarObject *)(p))->ob_size;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = list->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		if (PyFloat_Check(obj))
			print_python_float(obj);
	}

	setbuf(stdout, NULL);
}
