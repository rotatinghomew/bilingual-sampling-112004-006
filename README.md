# 跨语作品主题的双框抽样与审阅校正

所有记录都是本地合成数据。CSV 为 UTF-8 且有首行字段名；JSON 空值表示未报告。

## 补充来源说明

- `frames.json`：作品底册，编号按报送版本， family_hint 只是原作品候选。F 是学校普查框，P 是平台普查框；相同 hint 的状态由 decisions 来件核实。rights 表示能否将文本用于审阅。
- `draws.json`：抽中信号可叠加，概率记录是抽签时登记的条件概率；按季的学校配额等概率，平台独立抽签，两阶段专题复核采用既定层。配置中的不同学校、平台样框相互独立；同校作品的抽取不能因此假定完全独立。
- `reviews.json`：quick 是简审；full_original 与 full_translation 为相应文种复核。reviewer 是跨馆匿名审阅员，不同 alias 的同一人不可视为两次盲审。空结果包括无许可及待回复。

## 本地检查

使用 Python 3.11 标准库。当前可运行的是来源契约检查：

```sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
```
