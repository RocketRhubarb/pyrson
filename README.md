# pyrson

A parser for Swedish personal numbers.

Usage:

```python
from pyrson import is_personal_number

is_personal_number('19780202-2389')
> True

is_personal_number('helloworld')
> False
```
