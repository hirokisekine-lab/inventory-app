# 在庫管理アプリ

Pythonの学習用に作成した、CLIベースの在庫管理アプリです。

## 使用しているデザインパターン
- Strategy: 商品ごとの割引計算
- Factory: 商品タイプに応じたインスタンス生成
- Observer: 在庫追加時の通知(メール・Slack)
- Singleton: アプリ全体の設定管理
- Decorator: 商品へのオプション(ギフトラッピング等)の追加

## テスト
pytestによる単体テストを実装しています。

\`\`\`bash
pytest --cov=item --cov=inventory --cov=factory
\`\`\`
