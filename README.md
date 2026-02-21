# qq-group-archiver

NoneBot2 插件，自动归档 QQ 群聊图片和文件。

## 功能

- 自动保存指定群的图片到本地
- 自动保存群文件到本地
- 按 日期/群名/QQ号 分目录存储

## 依赖

- NoneBot2
- nonebot-adapter-onebot v11
- NapCatQQ
- httpx

## 安装

将 `save_image.py` 放入 NoneBot2 项目的 `plugins/` 目录下即可。

## 配置

编辑 `save_image.py` 中的 `TARGET_GROUPS` 字典，添加你要监控的群：

```python
TARGET_GROUPS = {
    1082969417: "Test",
    1080876483: "解构原典-三号",
    578992043:  "解构原典-二号",
}
```

## 目录结构

```
/data/image_collection/
  └── 2026-02-21/
      └── 群名/
          └── QQ号/
              └── 1771662179890.jpg

/data/file/
  └── 2026-02-21/
      └── 群名/
          └── QQ号/
              └── 文件名.pdf
```

## License

MIT
