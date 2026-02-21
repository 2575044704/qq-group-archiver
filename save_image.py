import httpx
import time
from datetime import datetime
from pathlib import Path
from nonebot import on_message, on_notice
from nonebot.adapters.onebot.v11 import GroupMessageEvent, GroupUploadNoticeEvent, Bot

IMAGE_DIR = Path("/data/image_collection")
FILE_DIR = Path("/data/file")
#格式： 群号码: "群名"
TARGET_GROUPS = {
    12345678: "相思相爱一家人",
    *********: "群名",
    *******:  "群名",
}

# 保存图片
save_img = on_message(priority=10, block=False)

@save_img.handle()
async def handle_img(event: GroupMessageEvent):
    group_name = TARGET_GROUPS.get(event.group_id)
    if not group_name:
        return
    for seg in event.message:
        if seg.type == "image":
            url = seg.data.get("url", "")
            if not url:
                continue
            today = datetime.now().strftime("%Y-%m-%d")
            user_dir = IMAGE_DIR / today / group_name / str(event.user_id)
            user_dir.mkdir(parents=True, exist_ok=True)
            async with httpx.AsyncClient() as client:
                resp = await client.get(url)
                if resp.status_code == 200:
                    filename = f"{int(time.time() * 1000)}.jpg"
                    (user_dir / filename).write_bytes(resp.content)

# 保存群文件
save_file = on_notice(priority=10, block=False)

@save_file.handle()
async def handle_file(bot: Bot, event: GroupUploadNoticeEvent):
    group_name = TARGET_GROUPS.get(event.group_id)
    if not group_name:
        return
    file_info = event.file
    if not file_info:
        return
    res = await bot.get_group_file_url(
        group_id=event.group_id,
        file_id=file_info.id,
        busid=file_info.busid,
    )
    url = res.get("url", "")
    if not url:
        return
    today = datetime.now().strftime("%Y-%m-%d")
    user_dir = FILE_DIR / today / group_name / str(event.user_id)
    user_dir.mkdir(parents=True, exist_ok=True)
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code == 200:
            filename = file_info.name or f"{int(time.time() * 1000)}"
            (user_dir / filename).write_bytes(resp.content)
