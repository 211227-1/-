# Telegram Sticker Studio

一个面向中文用户的 Telegram 表情包机器人项目：支持一键克隆、图片制贴纸、邀请裂变、可视化个人中心与管理员后台。

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Telegram-26A5E4?logo=telegram&logoColor=white)
![Repo Stars](https://img.shields.io/github/stars/211227-1/-?style=social)

## 项目亮点

- 粘贴 `t.me/addstickers/...` 即可自动克隆
- 发图片即可自动制作贴纸，支持连续添加
- 支持署名、视觉模式、适配模式、克隆策略
- 可视化个人中心：额度、最近记录、最近包、默认设置
- 可视化管理员后台：统计、用户检索、调额、群发、审计、外链设置
- 邀请裂变 + 额度策略（可设置新用户额度、邀请奖励、每日保底）
- 支持轮询与 Webhook 双模式部署

> 仅用于有授权的素材。请遵守版权与平台规则，禁止冒充或侵权发布。

## 功能总览

| 模块 | 能力 |
|---|---|
| 用户端 | 链接克隆、图片制贴纸、自动入包、改标题、包切换 |
| 个人中心 | 剩余额度、邀请人数、最近克隆、最近制作、最近邀请 |
| 管理后台 | 统计看板、用户搜索、额度调整、策略配置、群发通知、操作审计 |
| 运营工具 | 邀请链接、邀请海报二维码、外链按钮（交流群/作者） |
| 存储层 | 默认 JSON，支持切换 SQLite（`BOT_SQLITE_PATH`） |
| 运行模式 | `poll` 长轮询 / `webhook` 回调服务 |

## 快速开始

### 1) 安装依赖

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

### 2) 配置环境变量

复制 `.env.example` 为 `.env`，填写：

```env
BOT_TOKEN=123456:your-bot-token
ADMIN_USER_IDS=123456789
BOT_SERVE_MODE=poll
```

### 3) 启动机器人

```bash
python sticker_studio.py serve
```

## 新手使用流程

1. 给机器人发送 `https://t.me/addstickers/xxxx`，自动克隆。
2. 给机器人发送图片，自动制作贴纸。
3. 首次发图后会自动记录当前包，后续直接发图可持续添加。
4. 发送 `/center` 打开可视化个人中心。

## 常用命令

- `/center` 个人中心
- `/menu` 按钮菜单
- `/quota` 额度详情
- `/invite` 邀请链接
- `/invitecard` 邀请海报
- `/setmode <maker|clean|brand|circle|pixel|bw>`
- `/setfit <contain|cover>`
- `/setclonemode <copy|studio>`
- `/setmaketarget <ask|join|new>`
- `/settitle <新标题>` 或 `/settitle <短名|链接> | <新标题>`
- `/help` 新手帮助
- `/helpall` 完整命令帮助

## 管理员能力

- `/admin` 后台入口
- `/adminstats` 全局统计
- `/adminusers [page]` 用户列表
- `/adminfind <关键词> [过滤器]` 用户检索
- `/adminuser <user_id>` 用户详情
- `/adminquota <user_id> clone=<n> make=<n>` 设置额度
- `/adminbroadcast <内容>` 群发消息
- `/adminpolicy ...` 配置全局策略
- `/adminaudit [条数]` 操作审计日志
- `/adminexport [过滤条件]` 导出用户 CSV
- `/adminhealth` 运行健康状态

## 配置说明

主要配置项如下：

- `BOT_TOKEN` 机器人 Token（必填）
- `ADMIN_USER_IDS` 管理员用户 ID 列表
- `BOT_PROXY` 代理地址
- `BOT_FORCE_IPV4` 强制 IPv4（网络不稳时建议开启）
- `BOT_SQLITE_PATH` SQLite 数据库路径（可选）
- `BOT_SERVE_MODE` `poll` 或 `webhook`
- `BOT_WEBHOOK_URL` 公网 webhook 地址

完整示例见 [`.env.example`](./.env.example)。

## 常见问题

1. `Conflict: terminated by other getUpdates request`
同一个 Token 同时只能有一个轮询实例，关掉其他进程再启动。

2. `Cannot connect to host api.telegram.org:443`
检查网络或代理，必要时设置 `BOT_PROXY`，并尝试 `BOT_FORCE_IPV4=1`。

3. `STICKERS_TOO_MUCH`
当前包已满。程序已支持自动创建分包并继续添加。

4. `STICKER_*_DIMENSIONS` / `STICKER_PNG_DIMENSIONS`
上传图片尺寸不合规。建议使用 `studio + contain` 重新渲染后上传。

## 项目文档

- 项目书：[PROJECT_BOOK.md](./PROJECT_BOOK.md)
- 贡献指南：[CONTRIBUTING.md](./CONTRIBUTING.md)
- 安全策略：[SECURITY.md](./SECURITY.md)
- 变更记录：[CHANGELOG.md](./CHANGELOG.md)

## 开源协议

本项目使用 [MIT License](./LICENSE)。

## Star 支持

如果这个项目对你有帮助，欢迎点个 Star。

## 官方入口

👥 交流群: https://t.me/bqbkl  
🧑‍💻 联系作者: https://t.me/zuyuvip
