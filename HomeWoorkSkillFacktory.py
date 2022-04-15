def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       print('True')
   else:
       print('False')

check_palindrome('Не романтичное тру')