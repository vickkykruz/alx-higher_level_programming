#include <stdio.h>
#include <Python.h>
#include <string.h>
/**
 * print_python_string - This is a function that print the string information
 * @p: This is an argument that reprsent the Python Object
 *
 * Return: This function return a void (nothing)
 */
void print_python_string(PyObject *p)
{
	PyObject *rep, *str;

	(void) rep;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	rep = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");

	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %ld\n", PyBytes_AsString(str))
}
