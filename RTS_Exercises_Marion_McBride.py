class Exercises:
    
    def aboveBelow(unsorted_list, comparison_value):
        '''
        (list, int) -> (dict)

        Returns a dictionary with the keys "above" and "below" along with the amount
        of integers from the list that are above or below the comparison integer.

        > [1, 5, 2,  1, 10], 6
        { 'above': 1,  'below': 4 }

        > [2, 2, 3, 4, 5, 1], 2
        { 'above': 3, 'below': 1 }
        '''

        below_count = 0
        above_count = 0

        for i in unsorted_list:
            if i > comparison_value:
                above_count = above_count + 1
            if i < comparison_value:
                below_count = below_count + 1

        value_key_map =  {"above":above_count, "below":below_count}

        return value_key_map

    
    def stringRotation(unrotated_string, rotation_integer):
        '''
        (str, int) -> (str)

        PRECONDITION: Rotation amount must be a positive integer.

        Rotates the characters in the original string to the right by the
        rotation amount and places the overflow at the beginning of the string.

        >  "MyString", 2
        'ngMyStri'

        >  "ApplesAreGood!", 7
        'reGood!ApplesA'

        > "Good night!", 6
        'night!Good '
        '''

        first = unrotated_string[0 : len(unrotated_string) - rotation_integer]
        second = unrotated_string[len(unrotated_string) - rotation_integer : ]

        rotated_string = second + first

        return rotated_string

    


    
