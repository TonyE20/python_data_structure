#  1  Product

def product(a, b):
    return a * b
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """


#  2  Weekday Name

def weekday_name(day_of_week):
        #  """Return name of weekday.
    
        #     >>> weekday_name(1)
        #     'Sunday'
                    
        #     >>> weekday_name(7)
        #     'Saturday'
        
        #     For days not between 1 and 7, return None
    
        #     >>> weekday_name(9)
        #     >>> weekday_name(0)
        # """
            if day_of_week == 1:
                return "Sunday"
            elif day_of_week == 2:
                return "Monday"
            elif day_of_week == 3:
                return "Tuesday"
            elif day_of_week == 4:
                return "Wednesday"
            elif day_of_week == 5:
                return "Thursday"
            elif day_of_week == 6:
                return "Friday"
            elif day_of_week == 7:
                return "Saturday"
            else: return None


#  3  Last Element

def last_element(lst):
    idx = len(lst) - 1
    return None if lst == [] else lst[idx:]
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """


#  4  Nuber Compare

def number_compare(a, b):
    if a == b:
        return 'Numbers are equal'
    elif a > b:
        return 'First is greater'
    else: return 'Second is greater'
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """


#  5  Reverse String

def reverse_string(phrase):
    lst_phrase =[char for char in phrase]
    lst_phrase.reverse()
    return ''.join(lst_phrase)

    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """


#  6  Single Letter Count

def single_letter_count(word, letter):
    return word.lower().count(letter)
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """


#  7  Multiple Letter Count

def multiple_letter_count(phrase):
    ltr_cnt = {ltr: phrase.count(ltr) for ltr in phrase}
    return ltr_cnt
        
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """    


#  8  List Manipulation

def list_manipulation(lst, command, location, value=None):

    if command == 'remove' and location == 'beginning':
        return lst.pop(0)
    elif command == 'remove' and location == 'end':
        return lst.pop(len(lst) - 1)
    elif command == 'add' and location == 'beginning' and type(value) == int:
        lst.insert(0, value)
        return lst
    elif command == 'add' and location == 'end' and type(value) == int:
        lst.append(value)
        return lst
    else: return None

    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

#  9  Is Palindrome

def is_palindrome(phrase):
    
    phrase_list =[char for char in phrase.lower()]
    phrase_list.reverse()
    return "".join(phrase_list) == phrase.lower()


    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """


#  10  Frequency

def frequency(lst, search_term):
    return lst.count(search_term)
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """


#  11  Flip Case 

def flip_case(phrase, to_swap):
    string = ""
    for char in phrase:
        if char == to_swap:
            string+= char.upper()
        elif char == to_swap.upper():
            string+= char.lower()
        else: string+= char
    return string


    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """


#  12  Multiply Even Numbers

def multiply_even_numbers(nums):
    evenNum = 1
    for n in nums:
        if n % 2 == 0:
            evenNum *= n
    return evenNum

    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
        If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

#  13  Capitalize


def capitalize(phrase):
    return phrase.capitalize()
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """


#  14  Compact


def compact(lst):
    compact_list = [elm for elm in lst if bool(elm)]
    return compact_list

    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """


#  15  Intersection

def intersection(l1, l2):
    return list(set(l1).intersection(set(l2)))

    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """


#  16  Partition  

def partition(lst, fn):
    true_lst = []
    false_lst = []
    for elm in lst:
        if fn(lst):
            true_lst.append(elm)
        else: false_lst.append(elm)
        return [true_lst, false_lst]



    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """


#  17  MODE

def mode(nums):
    di_nums ={n: nums.count(n) for n in nums}
    max_val = max(list(di_nums.values())) 
    key_max = [key for key in di_nums if di_nums[key] == max_val]
    return key_max[0]

    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """


#  18  Calculate

def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == 'add':
       opt = a + b 
    elif operation == 'subtract':
       opt = a - b 
    elif operation == 'multiply':
       opt = a * b 
    elif operation == 'divide':
       opt = a / b 
    else: return

    if make_int:
        return f"{message} {int(opt)}"

    else: return f"{message} {opt}"

    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """

#  19  Friend Date  

def friend_date(a, b):
    a_hb = set(a[2])
    b_hb = set(b[2])
    if not a_hb & b_hb:
        return False
    else: return True

    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """


#  20  Triple and FIlter

def triple_and_filter(nums):
    n = [n * 3 for n in nums if n % 4 == 0]
    return n 
    """Return new list of tripled nums  for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """


#  21  Extract Full Name   

def extract_full_names(people):
    values = [val.values() for val in people]
    str_val = " ".join(values[0]), " ".join(values[1])
    return list(str_val)


    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """


#  22 Sum Floats

def sum_floats(nums):
    sum = 0
    for n in nums:
        if type(n) == float:
            sum += n
    return sum
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """


#  23  List Check

def list_check(lst):
    for l in lst:
        if type(l) != list:
            return False
    return True

    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """


#  24  Remove Every Other

def remove_every_other(lst):
    return lst[0::2]
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """


#  25  Sum Pairs   

def sum_pairs(nums, goal):
    l_goal = []
    for n in nums:
        for i in range(1, len(nums)):
            if n + nums[i] == goal:
                if n not in l_goal:
                    l_goal.append(nums.index(nums[i]))
    if l_goal == []:
        return ()
    else:
        l_goal.sort()
        idx = l_goal[0]
        return (nums[idx], goal - nums[idx])
    
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """


#  26  Vowel Count

def vowel_count(phrase):
    phrase = phrase.lower()
    return {v: phrase.count(v) for v in phrase if v in ['a', 'e', 'i', 'o', 'u']}
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """


#  27  Titleize

def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """


#  28  Find Factors

def titleize(phrase):
    phrase = phrase.split()
    return " ".join([wrd.capitalize() for wrd in phrase])

    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """


#  29  Includes  

def includes(collection, sought, start=None):
    
    if type(collection) == dict:
        collection = collection.values()
        return sought in collection
    elif type(collection) == set:
        return sought in collection
    else: 
        if start == None:
            start = 0
        else: start
    new_collection =[collection[n] for n in range(start, len(collection))]
    return sought in new_collection
    

    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """


#  30  Repeat

def repeat(phrase, num):
    
    if type(num) == str:
        return None
    elif num == 0:
        return ""
    elif num < 0:
        return None
    else: return phrase * num
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """


#  31  Truncate

def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    elif len(phrase) >= n:
        string = ''
        for chr in range(0, n - 3):
            string += phrase[chr]
        return f"{string}..."
    else: return phrase

    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """


#  32  Two List Dictionary

def two_list_dictionary(keys, values):
    if len(keys) <= len(values):
       return { keys[key]: values[key] for key in range(len(keys))}
    elif len(keys) > len(values):
        element_1 = {keys[key]: values[key] for key in range(len(values))}
        element_2 = {keys[key]: None for key in range(len(values), len(keys))}
        element_1.update(element_2)
        return element_1
    
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """


#  33 Sum Range 

def sum_range(nums, start=0, end=None):
    sum = 0
    if end > len(nums):
        length = range(start, len(nums))
    elif end == None:
        length = range(start, len(nums))
    elif end != None:
        length = range(start, end + 1)

    for n in length: 
        sum += nums[n]
    return sum

    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """


#  34  Same Frequency

def same_frequency(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))
    num1.sort()
    num2.sort()
    return num1 == num2

    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """


#  35  Two Oldest Ages

def two_oldest_ages(ages):
    ages.sort()
    ages.reverse()
    l_ages = []
    for n in ages:
        if n not in l_ages:
            l_ages.append(n)
    return (l_ages[1], l_ages[0])

    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.


#  36  Find The Duplicate

def find_the_duplicate(nums):
    key = {n for n in nums if nums.count(n) >= 2}
    if len(key) == 0:
        return None
    else: return key
    
      
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """


#  37  Sum Up Diagonals

def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """


#  38  Min Max Key In Dictionary

def min_max_keys(d):
    lst_keys = [k for k in d]
    lst_keys.sort()
    return (lst_keys[0], lst_keys[len(lst_keys) - 1])
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """


#  39  Find Greater Numbers

def find_greater_numbers(nums):
    if len(nums) == 0:
        return 0
    else:
        idx_max = nums.index(max(nums))
    
        if idx_max == 0:
            return 0
        else:
            return idx_max + 1
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """


#  4  Three Odd Numbers

def three_odd_numbers(nums):
    for n in range(0, len(nums)):
        if len(nums) >= n + 3:
            add_n = nums[n] + nums[(n+1)] + nums[(n+2)]
            if add_n % 2 != 0:
                return True
        else: return False
            
            # print(add_n)
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
  
    


    