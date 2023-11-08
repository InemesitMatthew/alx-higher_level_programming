#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to a pointer to the head of the linked list
 * Return: 1 if it's a palindrome, 0 if it's not
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow, *fast, *second_half, *prev_of_slow;
    listint_t *mid_node = NULL;
    int result = 1;

    slow = *head;
    fast = *head;
    prev_of_slow = *head;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;

            prev_of_slow = slow;
            slow = slow->next;
        }

        if (fast != NULL)
        {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_of_slow->next = NULL;
        reverse_list(head);
        result = compare_list(*head, second_half);
        reverse_list(&second_half);

        if (mid_node != NULL)
        {
            prev_of_slow->next = mid_node;
            mid_node->next = second_half;
        }
        else
        {
            prev_of_slow->next = second_half;
        }
    }

    return result;
}
