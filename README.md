# Abbrev

Calculate a set of unambiguous abbreviations for a set of strings. Inspired by <https://apidock.com/ruby/Abbrev/abbrev>.

## Example

```python
from abbrev import abbrev

abbrev("foo", "bar", "baz")

# {"f": "foo", "fo": "foo", "foo": "foo", "bar": "bar", "baz": "baz"}
```
