import hashlib
import os
from functools import reduce
 
table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
 
def munged_class_name(path, name):
    h = hashlib.md5((path + '+' + name).encode('utf-8')).digest()
    i = reduce(lambda x, y: x * 256 + y, reversed(h), 0)
    s = ''
    while i > 0:
        s = table[i % 64] + s
        i //= 64
 
    return (
        os.path.splitext(os.path.basename(path))[0] + '__' +
        name + '___' +
        s[:5]
    )

_save_entry_locator = 'article div form menu button.{}'.format(munged_class_name('webextension/widgets/button.css', 'button'))
print(_save_entry_locator)

# _save_entry_locator = (By.CSS_SELECTOR, 'article div form menu '
#                        'button.button__button___267m4')

# ul li div.item-summary__item-summary___2v2KL
print(munged_class_name('webextension/manage/components/item-summary.css', 'item-summary'))
print(munged_class_name('webextension/widgets/button.css', 'button'))


# import hashlib
# import os

# table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

# def munged_class_name(path, name):
#     h = hashlib.md5(path + '+' + name).digest()
#     i = reduce(lambda x, y: x * 256 + ord(y), reversed(h), 0)
#     s = ''
#     while i > 0:
#         s = table[i % 64] + s
#         i /= 64

#     return (
#         os.path.splitext(os.path.basename(path))[0] + '__' +
#         name + '___' +
#         s[:5]
#     )

# print(munged_class_name("homepage", "homepage"))
# print(munged_class_name("ul li div.item-summary.py", "item-summary"))
# print(munged_class_name("src/webextension/widgets/button.js", "button"))

# homepage__homepage___2CPGF;
# ul li div.item-summary__item-summary___2v2KL

# _save_entry_locator = (By.CSS_SELECTOR, 'article div form menu '
#                        'button.button__button___267m4')
