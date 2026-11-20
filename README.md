# 联办招募的路径归因与贡献复议

联办席位的引荐证据和确认来往。一个活动席位合计贡献最多为 1；份额用百分数，接受记录以申请组为单位。 数据均为合成。

CSV 使用 UTF-8、首行字段名，`-` 表示来源未填；JSON 使用原生布尔、字符串及数字。没有另行给定时，`seq` 只用于还原各条来件的先后，不是业务日期。

## 来源说明

- `attendance.csv`：仅 checked=1 是已核实到场。alias_of 非空表示签到补登记号，指向同一个活动的原席位。
- `evidence.csv`：verified 是固定联接；possible 是尚未定案的候选。code 非空且标记 single 时全活动最多用一次；pair 非空时同 pair 下所有证据同时采纳或均不采纳，每条 verified 的 share 是固定份额。possible 的 share 是该路径可归因份额；未采纳为零。
- `claims.csv`：一组仲裁申请最少需确认 min；accepted 的 amount 为实际签认份额。撤回以指向原证据编号的 adjudication 为准；未经更正的申请仍对应原活动。

## 数据清单

- `program.json`：配置对象。
- `attendance.csv`：`seat`, `activity`, `person`, `checked`, `checkin`, `alias_of`。
- `evidence.csv`：`id`, `seat`, `partner`, `at`, `type`, `code`, `use`, `pair`, `share`。
- `claims.csv`：`seq`, `claim`, `activity`, `partner`, `kind`, `min`, `amount`。
- `adjudication.csv`：`seq`, `id`, `kind`, `evidence`, `related`。

## 本地检查

使用 Python 3.11 标准库，无需安装第三方依赖。构建检查和来源契约测试：

```sh
python3 -m compileall -q tests
python3 -m unittest discover -s tests -v
```
