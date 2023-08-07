#include "lists.h"
/**
 * check_cycle - This is a function that checks if a singly linked list has a
 * cycle in it.
 * @list: This is an argumemt that reprsent listint structure
 *
 * Return: (0) if no cycle othwrwose (1) if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *prv;
	listint_t *tmp;

	prv = list;
	tmp = list;
	while (list && tmp && tmp->next)
	{
		list = list->next;
		tmp = tmp->next->next;

		if (list == tmp)
		{
			list = prv;
			prv = tmp;
			while (1)
			{
				tmp = prv;
				while (tmp->next != list && tmp->next != prv)
					tmp = tmp->next;
				if (tmp->next == list)
					break;
				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
