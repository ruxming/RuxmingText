# RuxmingText（中文说明）

> 说明：当前英文 `README.md` 作为 **Version 1** 保留不变；本文件是对应的中文版本说明。

`RuxmingText` 是一个轻量级 Python 文本处理工具包，主要用于：

- UTF-8 文本与十六进制字符串之间的互转；
- 从类似 `=E6=88=91` 这类编码片段中提取字节对并还原文本。

## 功能概览

- `hexStr_to_str`：将 UTF-8 十六进制字符串转换为可读文本。
- `str_to_hexStr`：将文本转换为 UTF-8 十六进制字符串。
- `Obtain16Char`：从混合字符串中提取标记符（默认 `=`）后面的十六进制字节对。
- `Validate16Char`：从可能不完整的编码文本中校验并提取完整分组。

## 安装

### 本地安装

```bash
pip install .
```

### 开发模式安装

```bash
pip install -e .
```

## 快速开始

```python
from RuxmingText.Convert_Char_v1a import (
    hexStr_to_str,
    str_to_hexStr,
    Obtain16Char,
    Validate16Char,
)

# 文本 -> 十六进制
print(str_to_hexStr("开"))
# e5bc80

# 十六进制 -> 文本
print(hexStr_to_str("e38090"))
# 【

# 从 '=' 形式的编码中提取字节
raw = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1=82"
hex_payload = Obtain16Char(raw, "=")
print(hex_payload)
# E68891E698AFE8AFB7E6B182

print(hexStr_to_str(hex_payload.lower()))
# 我是请求

# 对不完整编码做分组校验提取
partial = "i am request,=E6=88=91=E6=98=AF=E8=AF=B7=E6=B1"
validated = Validate16Char(partial, "=")
print(validated)
# E68891E698AFE8AFB7

print(hexStr_to_str(validated.lower()))
# 我是请
```

## 包结构说明

- `RuxmingText/Convert_Char_v1.py`：原始脚本实现（调试输出默认开启）。
- `RuxmingText/Convert_Char_v1a.py`：更适合作为库导入使用的版本（`DEBUG = False`），并提供 `sample()`。
- `RuxmingText/__init__.py`：导出 `sample` 与 `Validate16Char`。

## 使用注意事项

- 所有转换逻辑默认基于 UTF-8。
- `hexStr_to_str` 需要输入合法且长度为偶数的十六进制字符串，否则会抛错。
- `Obtain16Char` 与 `Validate16Char` 是面向 `=XX` 这类编码片段的轻量提取逻辑。

## 许可证

MIT（见 `LICENSE`）。
