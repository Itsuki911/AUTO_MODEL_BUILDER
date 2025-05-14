# Auto Model Builder

このプロジェクトは、AIモデルの自動開発を支援するシステムです。

## ディレクトリ構造
- `scripts/`: 各種スクリプト
- `data/`: 学習データ
- `models/`: 学習済みモデル
- `reports/`: 生成されたレポート

## セットアップ方法
1. 仮想環境を有効化します:
   ```
   source venv/bin/activate
   ```

2. Streamlitアプリを起動します:
   ```
   streamlit run app.py
   ```

## 必要なライブラリ
- Streamlit
- PyPDF2
- pandas
- transformers
- huggingface-hub
- matplotlib
- seaborn
- fpdf
- torch
- scikit-learn
- requests
