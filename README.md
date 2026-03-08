# RuxmingText

`RuxmingText` is a small Python utility package for converting text to/from hex-encoded UTF-8 and for extracting encoded byte pairs from strings like `=E6=88=91`.

## Features

- Convert a UTF-8 hex string into readable text (`hexStr_to_str`).
- Convert text into a UTF-8 hex string (`str_to_hexStr`).
- Extract hex byte pairs following a marker (default `=`) from a mixed string (`Obtain16Char`).
- Validate/extract grouped encoded segments from partially structured inputs (`Validate16Char`).

## Installation

### From local source

```bash
pip install .
```

### Development editable install

```bash
pip install -e .
```

## Quick start

```python
from RuxmingText.Convert_Char_v1a import (
    hexStr_to_str,
    str_to_hexStr,
    Obtain16Char,
    Validate16Char,
)

# Text -> hex
print(str_to_hexStr("开"))
# e5bc80

# Hex -> text
print(hexStr_to_str("e38090"))
# 【

# Pull out byte pairs after '=' symbols
raw = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1=82"
hex_payload = Obtain16Char(raw, "=")
print(hex_payload)
# E68891E698AFE8AFB7E6B182

print(hexStr_to_str(hex_payload.lower()))
# 我是请求

# Validate/extract complete grouped segments from truncated text
partial = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1"
validated = Validate16Char(partial, "=")
print(validated)
# E68891E698AFE8AFB7

print(hexStr_to_str(validated.lower()))
# 我是请
```

## Package layout

- `RuxmingText/Convert_Char_v1.py`: original script-style implementation with debugging enabled.
- `RuxmingText/Convert_Char_v1a.py`: cleaner import-friendly version (`DEBUG = False`) plus a `sample()` helper.
- `RuxmingText/__init__.py`: exports `sample` and `Validate16Char`.

## Notes

- Functions assume UTF-8 input/output.
- `hexStr_to_str` expects an even-length hex string and will raise if malformed.
- `Obtain16Char` and `Validate16Char` are lightweight parsers designed for encoded text patterns (for example, mail-style `=XX` byte tokens).

## License

MIT (see `LICENSE`).
