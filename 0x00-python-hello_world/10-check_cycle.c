#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to start of linked list
 * desc: this function says if a list is a circle
 * Return: 0 in fail 1 in true
 */
int check_cycle(listint_t *list)
{
	listint_t *now = list;
	listint_t *next = list;

	if (list == NULL)
		return (0);
	while (now != NULL && next != NULL && next->next != NULL)
	{
		now = now->next;
		next = next->next->next;
		if (now == next)
			return (1);
	}
	return (0);
}
