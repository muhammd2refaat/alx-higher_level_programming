#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 * You are allowed to use malloc and free only once
 * You are allowed to use helper functions
 * You can assume that the maximum number of nodes in the list is 5,000
 * The integer stored in each node will be a positive number
*/

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;

	if (!head || !*head || !(*head)->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
