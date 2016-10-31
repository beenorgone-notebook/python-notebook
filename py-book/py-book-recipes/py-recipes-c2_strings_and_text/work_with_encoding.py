# PROBLEM: In Unicode, certain characters can be represented by more than
# one valid sequence of code points:
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalape\u0303o'
print(s1, s2)  # Spicy Jalapeño Spicy Jalapẽo
