#include <stdlib.h>
#include "lists.h"

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
    dlistint_t *new, *l;

    new = malloc(sizeof(dlistint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
    {
        new->prev = NULL;
        *head = new;
        return (new);
    }

    l = *head;
    while (l->next != NULL)
        l = l->next;

    l->next = new;
    new->prev = l;
    return (new);
}
