def get_even_numbers(limit_number):
    '''
    This function return the even numbers
    - Examples:
        ```
        my_module.get_even_numbers(100)
        my_module.get_even_numbers(200)
        ```
    '''
    even_numbers = [i for i in range(limit_number) if i % 2 == 0]

    return even_numbers