#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - delete a node at a given index
 * @head: double pointer to head of list
 * @index: index of node to delete
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
    dlistint_t *node;
    unsigned int i;

    if (head == NULL || *head == NULL)
        return (-1);

    node = *head;
    for (i = 0; node != NULL && i < index; i++)
        node = node->next;

    if (node == NULL) /* index out of range */
        return (-1);

    if (node->prev)
        node->prev->next = node->next;
    else
        *head = node->next; /* deleting the head */

    if (node->next)
        node->next->prev = node->prev;

    free(node);
    return (1);
}
