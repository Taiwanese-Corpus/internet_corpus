# 網路語料

整理隨手抓的小量語料，若需自動化大量處理，另開專案

## 產生yaml
```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install pyyaml
python 範例資料.py 
```
python用法
```python3
print(yaml.dump(夜市輸出資料, default_flow_style=False, allow_unicode=True))
with open('柱柱姊掃街變成來亂的.yaml','w') as 檔案:
    yaml.dump(夜市輸出資料,檔案, default_flow_style=False, allow_unicode=True)
```