#include "lists.h"
/**
 * insert_node - This is a function that inserts a number into a sorted singly
 * linked list.
 * @head: This is an argument that reprsent the head of the listint_t struct
 * @number: This is an argument that reprsent the index of the node
 *
 * Return: This function woll return a new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *node, *tmp2;

	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);

	/* Store the data */
	node->n = number;

	if (!(*head))
	{
		node->next = NULL;
		*head = node;
		return (node);
	}
	if (tmp->n >= number)
	{
		tmp2 = *head;
		*head = node;
		node->next = tmp2;
		return (node);
	}

	while (tmp->next)
	{
		if (tmp->next->n >= number)
		{
			tmp2 = tmp->next;
			tmp->next = node;
			node->next = tmp2;
			return (node);
		}
		tmp = tmp->next;
	}

	tmp->next = node;
	node->next = NULL;

	return (node);
}
