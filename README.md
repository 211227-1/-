# Telegram Sticker Studio

一个更强的 Telegram 表情包工具（CLI + 机器人服务）：
- 一键克隆现有表情包到你的账号
- 克隆与制作都支持自定义署名（制作人）
- 支持多种视觉模式 / 适配模式 / 克隆策略
- 发图片自动制作贴纸并入包
- 邀请裂变：邀请好友奖励次数，支持邀请海报二维码
- 配额系统：可限制每人克隆/制作次数，支持每日保底重置
- 断点续跑（失败重跑可继续）
- 可选 SQLite 持久化（`BOT_SQLITE_PATH`）

> 仅用于你有授权的素材。请遵守版权与平台规则，禁止冒充或侵权发布。

项目书见：`PROJECT_BOOK.md`

## 0) 最快开始

```bash
python sticker_studio.py
```

默认进入交互向导。

## 1) 环境准备

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

复制 `.env.example` 为 `.env` 并填入：

```env
BOT_TOKEN=123456:your-bot-token
ADMIN_USER_IDS=123456789,987654321

# 网络可选项（连不上 api.telegram.org 时使用）
BOT_PROXY=http://127.0.0.1:7890
BOT_FORCE_IPV4=1
BOT_TRUST_ENV=1
# BOT_API_BASE=https://api.telegram.org
# BOT_FILE_BASE=https://api.telegram.org
# BOT_SQLITE_PATH=.bot_data.db

# 可选：webhook 模式
# BOT_SERVE_MODE=webhook
# BOT_WEBHOOK_URL=https://your.domain/telegram/webhook
# BOT_WEBHOOK_PATH=/telegram/webhook
# BOT_WEBHOOK_HOST=0.0.0.0
# BOT_WEBHOOK_PORT=8080
# BOT_WEBHOOK_SECRET=your_secret_token
# BOT_RATE_WINDOW_SECONDS=10
# BOT_RATE_MAX_HITS=10
```

## 2) CLI 克隆（完整版）

```bash
python sticker_studio.py clone \
  --source "https://t.me/addstickers/OldPackByAnyBot" \
  --watermark "@mybrand" \
  --mode brand \
  --fit-mode contain \
  --clone-mode studio
```

参数说明：
- `--mode`: `maker|clean|brand|circle|pixel|bw`
- `--fit-mode`: `contain|cover`
- `--clone-mode`: `studio|copy`
- `clone-mode=copy` 时静态贴纸默认原样复制；若设置了署名会转为渲染后入包

说明：
- 静态贴纸可按模式重渲染并加署名
- 动画/视频贴纸按 Telegram 能力复制

## 3) CLI 本地制作

```bash
python sticker_studio.py create \
  --assets-dir assets \
  --new-short-name my_local_pack \
  --new-title "My Local Pack" \
  --watermark "@mybrand" \
  --mode maker \
  --fit-mode contain
```

## 4) 机器人服务模式（推荐）

启动：

```bash
python sticker_studio.py serve
```

Webhook 启动示例：

```bash
python sticker_studio.py serve --serve-mode webhook --webhook-url https://your.domain/telegram/webhook --webhook-port 8080
```

可选后台管理员（设置配额策略）：

```env
ADMIN_USER_IDS=123456789,987654321
```

### 4.1 基础使用
- 发链接：`https://t.me/addstickers/xxxx`（自动克隆）
- 发图片：自动制作贴纸并加入你的当前包（可连续添加）

### 4.2 克隆命令
- `/clone <source>`
- `/clone <source> | <watermark> | <new_title> | <new_short_name> | <mode> | <fit> | <clone_mode>`

示例：

```text
/clone https://t.me/addstickers/OldPack | @mybrand | My Clone Pack | brand | contain | studio
```

### 4.3 图片制作命令
- 直接发图片时，机器人会弹出按钮让你选择：
  - 加入当前包
  - 新建表情包
- 图片标题可写：`/make 😀 | 包标题 | 包短名 | @署名 | mode | fit`

示例：

```text
/make 😀 | 我的自动包 | my_auto_pack | @mybrand | pixel | cover
```

### 4.4 个人中心与默认配置（按用户保存）
- `/setmaker @mybrand` 或 `/setwm @mybrand`
- `/clearmaker` 或 `/clearwm`
- `/setmode <maker|clean|brand|circle|pixel|bw>`
- `/setfit <contain|cover>`
- `/setclonemode <copy|studio>`
- `/setmaketarget <ask|join|new>` 设置发图默认去向
- `/settitle <新标题>` 修改当前包标题
- `/settitle <短名|链接> | <新标题>` 修改指定包标题
- `/setpack <short_name> | <title>`
- `/usepack <short_name> | <title>` 切换当前包
- `/packlist` 查看最近包
- `/clearpack`
- `/center` 个人中心（可视化按钮面板）
- `/menu` 打开按钮菜单（同 `/center`）
- `/profile` 查看当前配置（简版）
- `/modes` 查看模式说明
- `/help` 简版帮助（新手）
- `/helpall` 完整命令帮助
- `/invite` 获取邀请链接
- `/invitecard` 获取邀请海报（含二维码）

### 4.5 按钮面板能力
- 个人中心支持按钮切页：额度、最近记录、最近表情包、设置
- 个人中心支持外链按钮：加入交流群、联系作者（后台可配）
- 设置支持按钮切换：视觉模式 / 适配模式 / 克隆策略 / 发图去向
- 设置支持按钮改标题：修改当前包标题
- 图片发送后支持按钮选择“加入当前包 / 新建表情包”
- 最近表情包支持按钮一键切换当前包
- 管理员支持按钮后台：统计、策略、外链设置、用户列表分页、用户详情、操作日志审计
- 用户详情支持可视化调额：克隆/制作 +1、+5、-1、自定义增减
- `/quota` 查看剩余次数
- `/me` 查看 user id
- `/help` 查看帮助

连续添加逻辑：
1. 你第一次发图制作后，机器人会自动把目标包设为“当前包”。
2. 后续直接再发图，会继续加到这个当前包。
3. 你也可以随时用 `/usepack` 手动切换到别的包继续添加。

### 4.6 邀请裂变与次数限制

- 每个用户有 `clone` 和 `make` 两类剩余次数。
- 次数用完后，机器人会提示邀请好友并给出邀请链接。
- 好友通过你的邀请链接 `https://t.me/<bot>?start=ref_<你的uid>` 首次绑定后，你会获得奖励次数。
- 个人中心会显示最近邀请记录。
- 支持每日保底重置（可后台配置开关和数量）。

管理员可用命令：

- `/admin` 后台总览入口
- `/adminstats` 全局使用统计
- `/adminusers [page]` 用户列表分页
- `/adminfind <关键词> [uid:123 active:true min_clone_done:5]` 搜索用户（支持过滤）
- `/adminexport [过滤条件]` 导出用户 CSV
- `/adminhealth` 查看运行健康状态
- `/adminuser <user_id>` 查看单个用户详情（次数、邀请、最近行为、当前包）
- `/adminbroadcast <内容>` 群发文本消息
- `/adminpolicy` 查看全局策略
- `/adminpolicy free_clone=3 free_make=5 invite_reward_clone=2 invite_reward_make=3 enforce_limits=1 daily_reset_enabled=1 daily_free_clone=1 daily_free_make=2`
- `/adminquota <user_id> clone=<n> make=<n>` 手动调整单个用户剩余次数
- `/adminaudit [条数]` 查看后台操作日志（审计）
- 外链设置建议在后台按钮中完成：`外链设置 -> 设置交流群/设置作者联系方式`

## 5) 常见问题

1. `SHORT_NAME_OCCUPIED`
   - 换一个短名（`--new-short-name` 或 `/clone` 里传短名）。
2. `USER_NOT_FOUND`
   - 让目标用户先私聊 bot 发一条消息。
3. `STICKER_*_DIMENSIONS`
   - 工具会自动适配 512，极端图建议换图。
4. `STICKERS_TOO_MUCH`
   - 当前包已满时，机器人会自动新建分包并继续加入。
5. `Cannot connect to host api.telegram.org:443`
   - 先确认代理可用，再在 `.env` 设置 `BOT_PROXY=http://127.0.0.1:7890`。
   - 若是 IPv6/解析不稳，设置 `BOT_FORCE_IPV4=1` 后重启。
   - 也可先测试：`Invoke-WebRequest https://api.telegram.org -UseBasicParsing`。

## 6) 安全建议

- token 泄露后请去 BotFather 立即 rotate。
- 不要把 `.env` 提交到公共仓库。

## 7) 发布到 GitHub（公开仓库）

```bash
git init
git add .
git commit -m "feat: initial public release"
git branch -M main
git remote add origin <你的仓库地址>
git push -u origin main
```
