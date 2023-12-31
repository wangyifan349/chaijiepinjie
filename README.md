# 文件拆解和拼接工具
文件拆解和拼接工具

文件拆解和拼接工具是一个用于将大文件拆解为多个较小文件块，以及将拆解后的文件块重新合并成原始文件的实用工具。

它还提供了文件完整性验证功能，以确保合并后的文件与原始文件完全一致。

功能特点

1.文件拆解：将一个大文件拆解为指定数量的较小文件块，便于传输、存储或处理。

2.文件拼接：将拆解后的文件块按顺序合并为原始文件，还原大文件的完整内容。

3.完整性验证：通过计算文件的哈希值（BLAKE2b），验证拼接后的文件与原始文件的一致性，确保数据完整性。

4.自动命名：自动为拆解和合并的文件生成唯一的文件名，避免文件名冲突。

5.易于使用：简单的函数调用接口，无需复杂的配置和参数设置。

请注意，拆解后的文件块和合并后的文件将与原始文件位于同一目录下，并在执行操作时自动生成一个名为 hash_table.txt 的哈希表文件，记录文件和文件块的哈希值。

贡献和问题反馈如果你发现任何问题、错误或有改进建议，欢迎通过 GitHub 上的 Issues 页面提出。我们欢迎任何贡献和改进，可以通过提交 Pull Request 来参与项目的开发和改进。




