# 禁用词、条件用词与文风筛查

不要对科学英文作无条件的全局替换。同一个词可能是空泛修饰、定义明确的统计术语、专名或准确引用。先标明它为何被标记，再决定保留、改写、加限定、移到方法或退回核证。

## 哪些表达应禁止，哪些应复核

**证据禁用。** 在当前设计不支持的具体语境中禁止会改变事实的写法。例如，相关性写成 *caused*，没有优先权核验却写 *first ever*，以未检出差异声称 *equivalent*，把模型输出称为 *observed*。允许它们的条件取决于研究设计和所指主张，而不是替换词本身。换成 *may prove* 仍可能误导。

**项目禁用。** 某稿件已选定一个概念的规范词，就在该稿的术语表中记录禁止混用的近义词、拼写、连字符、单复数和允许语境。对原引文、文献题名、程序标识符、标准或量表专名分别处理。不要将一个稿件的术语裁决移植成全领域规定。

**文风复核。** 对编辑偏好，标记出现位置并人工判断作用。若措辞缺乏独立信息，删去后重读。若词有技术意义，保留并补足定义、尺度或证据。

| 常见触发词 | 在正文中要问 | 改写或保留的条件 |
|---|---|---|
| *obviously, clearly, evidently, undoubtedly, undeniably, of course* | 删副词后，证据是否仍能支持句子？ | 通常删除，给读者可见的对照。*Clearly visible* 在有明定可见性判据时可具体写明判据。 |
| *significant, significantly, highly significant* | 指统计判定、实际重要性还是数值大？ | 统计义要有检验、目标和报告值。实际义改为量级、方向或对决策的影响。P 值不衡量效应大小。 |
| *very, extremely, strongly, substantially, dramatically, markedly, strong, weak, moderate, striking, pronounced, marginal* | 以哪个基线、尺度或约定作判断？ | 写出差值和单位，若使用已定义的类别阈值，写出界限。保留 *marginal probability* 等定义明确的术语。 |
| *robust, stable, reliable, consistent, accurate, reproducible* | 是变化小、独立重复、对扰动不敏感、方向一致，还是与外部参照接近？ | 给出扰动集合、重复单元、参照与容忍界限中适用的几项。*Robust regression* 可以是正式方法名。 |
| *fundamental, essential, important, critical, pivotal, crucial, key, notable, meaningful, impactful* | 对哪一个解释、决策或误差有影响？ | 写改变了什么。*Critical temperature* 等具有定义的属性照常保留。 |
| *innovative, novel, groundbreaking, transformative, unprecedented, unique, first, state-of-the-art* | 搜索范围、最近可比工作和共同评价协议是否足以支持？ | 通常改写为可核的新增能力或在同一协议下的比较。*First measurement in this series* 是时序。它不等于领域首创。 |
| *prove, conclusively demonstrate, definitively establish, validate, confirm, guarantee* | 是否有推导、独立验证、预设判据或适用域内的保证？ | 数学证明可用 *prove*。验证某个性能维度时点明终点与范围。一次成功不支持笼统的“全面验证”。 |
| *causes, drives, determines, explains, underlies, mediates, leads to, results in, because, due to* | 是物理定义、受控干预、观察关联、事后解释，还是仅有时间先后？ | 因果措辞要对应识别设计。可核的程序因果正常保留，例如阈值规则确实怎样产生一个输出。不据此推断跨群体机制。 |
| *some, many, most, few, several, generally, typically, often, rarely, widely* | 范围和分母是什么？是样本计数、独立研究数量还是定性概括？ | 能计数时写 *[k] of [n]* 或相应比例。定性观察则写清采样范围，不伪造数字。 |
| *roughly, about, around, nearly, on the order of* | 是测量不确定、取整量还是想回避核数？ | 有测量或数量级理由才保留。阈值边界和关键结果要给足够有效位，不把精度不足的测量写成精确常数。 |
| *all, always, never, universal, entirely, exclusively, only, none* | 是否穷尽了声称的单位和观察窗口？零次数是否有可检出机会？ | 写出条件，例如 *No failures were recorded during the observation period*。避免将观察窗内的零写成永久不会发生。 |
| *may possibly, could potentially, appears to suggest, tends to generally* | 可以辨认哪一项具体的不确定性？ | 保留一个必要限定，再说未测的对象、较宽的区间或替代解释。 |
| *delve, showcase, underscore, foster, leverage, utilize, facilitate, elucidate, unveil* | 除了更正式，该动词比 *examine, report, use, help* 多说了什么？ | 可直接改成实际动作。具有专业意义的 *leverage* 或 *facilitation* 不按字面命中删除。 |
| *landscape, tapestry, realm, paradigm, interplay, framework, perspective, implications* | 能指出对应的对象、模型、操作关系或可执行决定吗？ | 用实义名词替换无明确所指的隐喻。*Framework* 若确指一套定义好的方法，说明组件和边界。 |
| *comprehensive, seamless, sophisticated, intricate, meticulous, holistic, elegant, scalable* | 哪个技术限定是辨认研究对象所必需的？ | 保留可操作定义，例如 *scalable to [specified input size] under [resource budget]*。删除没有测试的宣传语。 |
| *interestingly, surprisingly, importantly, notably, in fact, it is worth noting that, importantly enough* | 能否从实际比较推出“意外”或“重要”？ | 直接写观察和预期基线。意外若有预注册或理论预期，指出它与哪条预测不同。 |
| *not only … but also, not X but Y, distinct from, superior, outperformed* | 对比的双方是否真在同一尺度、样本及协议内测量？ | 有数据支持的对比保留。把只并列两个新名词的对照句还原成各自的事实。 |
| *failure, success, improvement, agreement, bias, efficiency, quality* | 判据、参照、方向与汇总层级是否定义？ | 不用宽泛词笼统覆盖多种终点。例如，观察到波动减小，不自动意味着更准确。 |

## 文体复读的 21 种线索

这些是编辑动作，不用于判断作者身份。每一项都应在含义不变的前提下处理。以下顺序服务于复读。

| # | 阅读时发现什么 | 实际该做什么 |
|---|---|---|
| 1 | 装饰性高调词替代了动作 | 写出测量、比较或推导了什么，保留规范术语。 |
| 2 | 每句同样长，动词都埋在相同位置 | 一个证据句容纳必要限定，随后用短句交代意义。按信息量分句。 |
| 3 | 所有清单机械地凑成三项 | 实际有几项列几项，检查第三项是否在重复第一项。 |
| 4 | *It is important to note that* 等框架推迟事实 | 直接从事实起句。确有例外时指出例外如何改变解读。 |
| 5 | 段尾变成可套在任何论文上的格言 | 落在本研究的对象、条件、范围、决策或下一项已在段中建立的认识上。 |
| 6 | 最高级或“证明”语气掩盖证据边界 | 收窄到已测试的群体、基线与终点，开放尚未区分的解释。 |
| 7 | 修辞性对照不含真正可比的量 | 列出比较两端。若没有共同尺度，用两个独立陈述或删掉空对照。 |
| 8 | 镜像平行句式把一个事实说了两次 | 只保留真实平行的测量、组别或方向。 |
| 9 | 同义词轮换导致读者以为概念变了 | 将技术名词换回首次定义的词，再核图内标签。 |
| 10 | 用 *serves as* 等架子回避简单定义 | 表达身份可用 *is*。确实承担临时功能时，保留对应的角色动词。 |
| 11 | 句尾 *highlighting/demonstrating* 附加无依据推论 | 删除，或让它成为一句带有可核证据的独立判断。 |
| 12 | 名词化链模糊施事和动作 | 写清谁测什么。保留作为正式测量构念的名词。 |
| 13 | 每段从 *Furthermore/Moreover/Additionally* 开始 | 写具体逻辑，例如 *Under the same load*、*In the held-out batch*，或直接起句。 |
| 14 | 破折号承担主要论证关系 | 把比较拆成完整句或必要的局部说明。保留数学减号与区间。 |
| 15 | 同一名词前堆评价性形容词 | 问每个形容词是否定义采样、方法或条件，只保留影响含义的限定。 |
| 16 | 每段长度和“主张—补充—升华”弧线相同 | 让主发现有空间解释机制或范围，短对照只占需要的长度。 |
| 17 | 两层以上对冲重复表达不确定性 | 只留一层并说明证据限制。 |
| 18 | *Researchers have noted* 没有可追的来源 | 给支持该句的原始来源，或把句子标为本文待检的判断。 |
| 19 | 抽象名词端在空中 | 指出变量、对象和关系。找不到所指时删掉它。 |
| 20 | 开篇铺陈时代背景，尚未提出研究张力 | 从领域已知事实和具体未解问题开始。 |
| 21 | 发现没有具体对象、条件或比较 | 给可辨识的样本、方向或一个决定性数值。首句无需同时交代每个统计量。 |

另做三次收尾检查。**重复与导航。** 删已经说过的结论、空悬问句和章节预告，但保留帮助读者跨越真实推理断点的过渡。**认知占位。** 如果末句只说“这提供了见解”，改写为它具体区分了哪些解释。**无尺度概括。** 把“变化很大”“通常如此”换成可核的量或明确边界，必要时保留真实的不确定性。

## 术语裁决表

每个承重概念记录“概念、规范词、定义、单位／分母、同义替代是否允许、适用稿件、版本或裁决依据”。例如，若 *detection yield* 定义为“每个送检件中获得可判读信号的比例”，不能在下一段把它写成以阳性送检件为分母的 *sensitivity*。修改定义时分开标记“改了叫法”和“重算了估计量”，检查正文、图面、图注、表头、方法与补充材料。被锁定的旧版图不得擅自回写，在允许的修订稿里说明两种口径如何对应。
