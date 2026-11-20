# 跨语作品主题的双框抽样与审阅校正

所有记录都是本地合成数据。CSV 为 UTF-8 且有首行字段名；JSON 空值表示未报告。

## 补充来源说明

- `frames.json`：作品底册，编号按报送版本， family_hint 只是原作品候选。F 是学校普查框，P 是平台普查框；相同 hint 的状态由 decisions 来件核实。rights 表示能否将文本用于审阅。
- `draws.json`：抽中信号可叠加，概率记录是抽签时登记的条件概率；按季的学校配额等概率，平台独立抽签，两阶段专题复核采用既定层。配置中的不同学校、平台样框相互独立；同校作品的抽取不能因此假定完全独立。
- `reviews.json`：quick 是简审；full_original 与 full_translation 为相应文种复核。reviewer 是跨馆匿名审阅员，不同 alias 的同一人不可视为两次盲审。空结果包括无许可及待回复。
- `publication_ledger.json`：刊发台账保存实际出刊过的数字、拟约稿前提出的分组请求、底册可见截止日及另外两馆的双语补审时段。`count` 是整数原作品贡献件数，不是加权估计，也不表示每件作品只有一个主题；只可在同季、同可比主题、同基底上核算互斥学校组的合计。`protected_measure` 约束一次或多次刊发后可确定的小校贡献件数；发现旧表已经足以推出受保护件数的情形，保留原件，后续不把范围缩小，也不把该数字列成对外明细。`review_slots` 中 `return_by` 晚于排版日的资料不能计入该次征稿判断。

## 本地检查

使用 Python 3.11 标准库。当前可运行的是来源契约检查：

```sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
```
