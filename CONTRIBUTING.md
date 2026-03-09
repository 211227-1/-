# 贡献指南

感谢你愿意参与这个项目。

## 提交 Issue

- 提交前请先搜索是否已有同类问题
- 描述尽量包含：
- 运行环境（Python 版本、系统）
- 复现步骤
- 实际结果与期望结果
- 报错日志或截图

## 提交 Pull Request

1. Fork 仓库并创建分支
2. 完成功能或修复后自测
3. 提交 PR 并说明改动背景、改动点、验证方式

建议命名规范：

- `feat: ...` 新功能
- `fix: ...` 问题修复
- `docs: ...` 文档更新
- `refactor: ...` 重构
- `test: ...` 测试相关

## 本地开发

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python -m unittest -q
```

## 注意事项

- 严禁提交真实 `BOT_TOKEN` 或 `.env`
- 涉及 Telegram API 行为变更，请补充复现与回归测试说明
- 对用户可见文案改动，优先保持中文一致性与可读性
