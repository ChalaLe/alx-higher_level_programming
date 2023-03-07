#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *know = list;
	listint_t *later = list;

	if (!list)
		return (0);

	while (know && later && later->next)
	{
		know = know->next;
		later = later->next->next;
		if (know == later)
			return (1);
	}

	return (0);
}

