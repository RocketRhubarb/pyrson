# pyrson

A parser for Swedish personal numbers.

Usage:

```python
from pyrson import is_personal_number

is_personal_number('197802022389')
> True

is_personal_number('helloworld')
> False
```
