#### 假想协议

假想了一个协议由以下部分组成。

1. 标识符：9字节，内容固定为`CANNONADE`。
2. 大炮数量N：1字节。
3. 大炮开火状态 * N：N比特。1为开火，0为不开火。
4. 补0：补满8比特。

| 标识符 | 大炮数量 N | 大炮开火状态 1 or 0 |    补 0     |
| ------ | ---------  | ------------------- | ---------- |
| 9 bytes|   1 byte   |         N bit       | 补满 8 bits |

#### 插件编译安装

见[Wireshark插件编译记录][1]

[1]: https://rainzhop.github.io/2015/02/01/wireshark-plugins-compile-notes/
