#include "lists.h"
/**
 * is_palindrome - This is a function that check if a singly linked list is a
 * palindrome.
 * @head: This is an argument that reprsent the head of the listint_t list
 * structure
 *
 * Return: This function 1 if it's palindrome otherwise 0 if not
 */
int is_palindrome(listint_t **head)
{
	int len, i, *ptr;
	listint_t *tmp = *head;

	if (!(*head))
		return (1);

	for (len = 0; tmp; len++)
		tmp = tmp->next;

	ptr = malloc(sizeof(int) *  len);
	if (!ptr)
		exit(100);

	tmp = *head;
	for (i = 0; tmp; tmp = tmp->next, i++)
		ptr[i] = tmp->n;

	for (i = 0; i < (len / 2); i++)
	{
		if (ptr[i] != ptr[len - 1 - i])
		{
			free(ptr);
			return (0);
		}
	}

	free(ptr);
	return (1);
}
