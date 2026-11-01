# 检查用词，再决定是否修改

在写作 skill 目录内执行以下命令。检查器使用 Python 3 标准库，读取 UTF-8 正文或标准输入，不修改文件。为获得可解释的结果，从 LaTeX、引用、代码和数学表达式中选出需要审校的英语段落，保留换行。匹配在单行内完成，位置从 1 开始。

~~~sh
python3 scripts/check_prose.py results.txt
python3 scripts/check_prose.py results.txt --terms assets/term-lock.example.tsv --section Results
python3 scripts/check_prose.py results.txt --terms my-terms.tsv --strict-terms --json
~~~

通用词表给出复核问题。比如 “robust estimator” 可以是正式方法名；“the estimates were robust” 则需要说明对哪种扰动、在哪个样本上稳健。遇到 “this suggests” 时，先核所指观察以及它支持的推断。检查器不能判断论证是否正确，也不能判断谁写了稿件。

术语表的四列分别是 scope、avoid、preferred 和 meaning。每行只锁一个已有定义的概念。scope 可填 `*` 或与 `--section` 一致的章节名；默认章节为 Results。示例中 “error rate” 仅在作者确认所指为连续绝对误差时需要改。若测量的确是错误次数的比例，应使用比例所对应的术语。规则按完整词或词组匹配，大小写不敏感。

普通复核提示返回 0。使用 `--strict-terms` 且发现术语冲突时返回 1；输入错误返回 2。无命中只说明没有匹配该词表，语态、主语、比较是否同层以及图文结论仍需逐句审读。
