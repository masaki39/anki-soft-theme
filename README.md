# Anki Soft Theme

Anki（デスクトップ版）のメイン画面を見やすくするテーマアドオンです。

- 上部ツールバーをピル型に
- デッキ一覧をカード化し、新規・学習中・復習の件数を色付きバッジで表示
- 学習開始画面と下部ボタンをフラットなデザインに
- ライト／ダークモード両対応
- メインウィンドウの透明度を設定可能（`config.json` の `window_opacity`）

カードの中身（ノートタイプのテンプレート）には手を加えません。

## インストール（開発用）

```bash
ln -s "$(pwd)" ~/Library/Application\ Support/Anki2/addons21/soft_theme
```

Anki を再起動すると反映されます。

## 配布用パッケージ

```bash
zip -r soft_theme.ankiaddon __init__.py config.json config.md manifest.json web
```
