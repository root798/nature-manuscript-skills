# 检查用词，再决定是否修改

在写作 skill 目录内执行以下命令。检查器使用 Python 3 标准库，读取 UTF-8 正文或标准输入，不修改文件。为获得可解释的结果，从 LaTeX、引用、代码和数学表达式中选出需要审校的英语段落，保留换行。匹配在单行内完成，位置从 1 开始。

~~~sh
python3 scripts/check_prose.py results.txt
python3 scripts/check_prose.py results.txt --terms assets/term-lock.example.tsv --section Results
python3 scripts/check_prose.py results.txt --terms my-terms.tsv --strict-terms --json
~~~

通用词表给出复核问题。比如 “robust estimator” 可以是正式方法名；“the estimates were robust” 则需要说明对哪种扰动、在哪个样本上稳健。遇到 “this suggests” 时，先核所指观察以及它支持的推断。检查器不能判断论证是否正确，也不能判断谁写了稿件。

术语表的四列分别是 scope、avoid、preferred 和 meaning。每行只锁一个已有定义的概念。scope 可填 `*` 或与 `--section` 一致的章节名，默认章节为 Results。示例旧称 *board deviation index* 在这个虚构项目中始终对应以 mV 计的 *absolute voltage error*。若文中另有 *error rate*，它可以指错误次数占比，应逐处核对定义。规则按完整词或词组匹配，大小写不敏感。

普通复核提示返回 0。使用 `--strict-terms` 且发现术语冲突时返回 1；输入错误返回 2。无命中只说明没有匹配该词表，语态、主语、比较是否同层以及图文结论仍需逐句审读。

术语统一先建立[概念与名称映射](terminology-and-referents.zh-CN.md)，再把无歧义的旧称放入检查器。检查器不理解指代或分析层级；同一个词在另一段指不同的真实对象时，不能设成全稿自动替换。图内标签还须读取实际渲染文件核对。
