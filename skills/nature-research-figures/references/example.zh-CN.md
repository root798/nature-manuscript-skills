# 可运行示例：配对测量和差值来自同一张表

![配对测量与差值的合成示例](../assets/example-figure.svg)

输入为[完全虚构的 CSV](../assets/example-readings.csv)，含五个试样、两个设置，每个试样在每个设置下有两次读数。本例仅演示图、数据和文字间的勾稽关系。

从该 skill 的目录运行：

```bash
python3 -m pip install matplotlib
python3 scripts/render_example.py --out build
```

也可以用相同表头的自有数据运行 `python3 scripts/render_example.py --data readings.csv --out build`。每个试样占一行，每个设置恰好有两个有限、非负的时间值，试样标识必须唯一。生成 PDF、SVG、PNG 和含逐试样均值及差的 CSV。输入含缺测、负值、重复标识或不同重复数时，需要先按研究协议决定分母与纳入规则，并调整脚本。

**怎样读图。** Panel a 中，圆表示设置 A、菱形表示 B。点是两次读数的算术平均值，浅色线伸到这两次读数的最小值和最大值。Panel b 对每个试样取 B 的均值减去 A 的均值，虚线为零。例如试样 A，设置 A 的 12 和 14 ms 得到 13 ms；设置 B 的 9 和 11 ms 得到 10 ms。因此 b 的第一个点位于 −3 ms。五个配对差依次为 −3、−2、−1、−3、−1 ms，等权平均为 −2.0 ms。图中线段表示观察范围，没有给出置信区间。

**Results 示例。** Readout time was shorter under setting B for all five synthetic specimens. The mean paired difference was −2.0 ms (B minus A), with specimen differences ranging from −3 to −1 ms.

**Caption 示例。** Readout time under two settings. **a**, Mean time for each specimen under setting A (rose circles) and setting B (slate diamonds). Segments span the two readings for each specimen and setting. **b**, Within-specimen differences in mean readout time (B minus A). The dashed line denotes zero. Data are synthetic.

如需重画独立色卡，运行 `python3 scripts/render_palette_atlas.py`。它从同一个 JSON 读取颜色，输出 [palette-atlas.svg](../assets/palette-atlas.svg)。换色时改配置、重出真实示例和色卡，再复核图注色名。
