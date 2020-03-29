# membo
バンドメンバー募集サイト

# Dependency
Python==3.6.1  
Django==2.2.9  
channels==2.4.0　チャットで必要  
channels-redis==2.4.1　チャットで必要。  
(redis==3.4.1)チャットでもしかしたら必要かも？  

# Setup
参考サイト
https://tutorial.djangogirls.org/ja/python_installation/

 ### pythonをインストール
https://www.python.org/downloads/release/python-361/ からPythonインストーラーをダウンロード。  

Mac OS X 64-bit/32-bit installer というファイルをダウンロード。  
ダウンロードできたら python-3.6.1-macosx10.6.pkg をダブルクリックして実行。  
インストールがうまくいったか確認するために、コマンドプロンプトを開いて [python3 --version] と打ち込む。  


 ### Djangoをインストール 
 * まずディレクトリ作る  
 $ mkdir (ディレクトリ名)  
 $ cd （ディレクトリ名）  
 * 仮想環境（環境名:myvenv(環境名は任意)）を作成  
 $ python3 -m venv myvenv  
 * 仮想環境を起動  
 $ source myvenv/bin/activate  
 コンソールでプロンプトの行頭に (myvenv) が付いたら、仮想環境(myvenv) を起動している。  
 この状態でDjangoをインストールする。
まずは、Djangoのパッケージ管理システムであるpipを最新のものにアップグレードする。  
 (myvenv)$ pip install --upgrade pip  
 そしてDjangoをインストール。  
 (myvenv)$ pip install Django==2.2.9  
 
 ### プロジェクトの作成  
 (myvenv)$ django-admin startproject membo  
 
 


# Usage
使い方。なるべく具体的に書く。サンプルも書く


# Authors
otkken2

# References
参考にした情報源（サイト・論文）などの情報、リンク