#set page(paper: "a4", margin: (x: 20mm, y: 18mm), numbering: "1")
#set text(font: "Noto Sans CJK JP", size: 10.5pt, lang: "ja")
#set par(leading: 0.72em, justify: true)
#set heading(numbering: none)
#show raw: set text(font: "Noto Sans Mono CJK JP", size: 7.2pt)

#let code(path) = block(
  width: 100%, fill: rgb("#20252d"), inset: 9pt, radius: 3pt,
  raw(read(path), block: true, lang: "python"),
)
#let task(slide, title, path: none, body: none) = [
  *スライド #slide　#title*
  #v(6mm)
  #if path != none { code(path) }
  #v(5mm)
  #body
]

#align(center + horizon)[
  #text(size: 26pt, weight: "bold")[プログラミング応用]
  #v(18mm)
  #text(size: 22pt)[課題 10]
  #v(60mm)
  提出日：2026年7月16日 木曜日
  #v(35mm)
  #text(size: 14pt)[4年電子工学科 5番 近藤優樹]
]

#pagebreak()
#task(26, "標準モジュール math / random", path: "math_example.py", body: [
  #code("random_example.py")
  #v(5mm)
  `math.pi`を表示すると、mathモジュールが持つ円周率を利用できる。  
  `random.random`は関数そのものを表し、`random.random()`は0以上1未満の乱数を生成する。  
  関数を実行するには、名前の後ろに丸括弧が必要である。
])

#pagebreak()
#task(27, "ex12.py：自作計算モジュール", path: "module.py", body: [
  加算・減算・乗算・除算・べき乗の処理を、それぞれ関数として定義した。  
  ファイルを実行すると各関数が順番に呼び出され、10、10、25、5.0、125が得られる。  
  関数をまとめたファイルは、別のPythonファイルからモジュールとして利用できる。
])

#pagebreak()
#task(28, "module_test.py：time / sys", path: "module_test.py", body: [
  `time.time()`は1970年1月1日からの経過秒数を返すため、実行時刻で値が変わる。  
  `sys.path`は、Pythonがインポート対象を探すディレクトリの一覧である。  
  `sys`を表示すると、Pythonに組み込まれたモジュールであることも確認できる。
])

#pagebreak()
#task(30, "モジュール検索パスの一時追加", path: "path_example.py", body: [
  `sys.path.append()`を使い、自作モジュールがあるフォルダを検索先へ追加した。  
  今回は`C:\Users\noku\programming_class\homework_10\math`を検索先に指定している。  
  この変更はプログラムの実行中だけ有効で、Pythonを終了すると元に戻る。
])

#pagebreak()
#task(31, "ex12.pyをmodule.pyへ変更", path: "math/import_module.py", body: [
  スライド27で作成した`ex12.py`のファイル名を`module.py`へ変更した。  
  `import module`を実行すると、モジュール内に直接書かれた`print`文も順番に実行される。  
  そのため、インポートしただけで10、10、25、5.0、125が出力される。
])

#pagebreak()
#task(32, "module.power()の利用", path: "path_example.py", body: [
  #code("math/module_test.py")
  #v(5mm)
  `math`フォルダを検索パスへ追加した後で`module`をインポートし、`power(10, 3)`を呼び出した。  
  関数は10の3乗を計算するため、実行結果として1000が表示される。  
  `モジュール名.関数名()`と書くことで、関数の所属を明確にして利用できる。
])

#pagebreak()
#task([33・34], "__name__による直接実行の判定", path: "math/module.py", body: [
  #code("path_example.py")
  #v(4mm)
  #code("math/module_test.py")
  #v(5mm)
  `if __name__ == "__main__":`は、そのファイルが直接実行された場合だけ真になる。  
  if文がない場合は、インポート時にもモジュール内のすべての`print`文が実行される。  
  if文がある場合はテスト部分が実行されず、呼び出した`power(10, 3)`の1000だけが表示される。
])

#pagebreak()
#task(38, "パッケージ内のmodule1.py", path: "sub/sub1/module1.py", body: [
  `module1.py`には、テスト名と自身のファイルパスを表示する2つの関数がある。  
  `inspect.currentframe()`で現在の実行位置を取得し、`inspect.getfile()`でファイル名を調べる。  
  出力されたパスから、どのパッケージのモジュールが動いたか確認できる。
])

#pagebreak()
#task([39・40], "例1：module1とmodule2", path: "ex12_1.py", body: [
  `sub1`のmodule1と`sub2`のmodule2から、それぞれ2つの関数を呼び出した。  
  完全名は記述が長い一方、同名関数があっても所属先を明確に区別できる。  
  実行結果にはテスト名と、各モジュールが置かれたファイルパスが表示される。
])

#pagebreak()
#task(41, "例2：fromとエイリアス", path: "ex12_2.py", body: [
  `from sub.sub1 import module1`により、呼び出し時のパッケージ名を省略した。  
  module2には`m2`というエイリアスを付け、さらに短い名前で利用している。  
  例1と同じ結果を得ながら、読みやすく簡潔なコードになった。
])

#pagebreak()
#task(42, "例3：ワイルドカードインポート", path: "ex12_3.py", body: [
  `from ... import *`は、パッケージが公開する名前をまとめてインポートする。  
  記述は短くなるが、対象を制限しないと不要なモジュールまで読み込む可能性がある。  
  名前の衝突や出所の分かりにくさを避けるため、使用範囲には注意が必要である。
])

#pagebreak()
#task(43, "__init__.pyと__all__", path: "sub/sub1/__init__.py", body: [
  `__init__.py`はフォルダをパッケージとして扱うために用いられるファイルである。  
  `__all__`にモジュール名を指定すると、`import *`で公開する対象を制限できる。  
  今回はsub1でmodule1、sub2でmodule2、sub3でmodule3だけを公開した。
])

#pagebreak()
#task(44, "例4：sub3/module3", path: "sub/sub3/module3.py", body: [
  #code("sub/sub3/__init__.py")
  #v(4mm)
  #code("ex12_4.py")
  #v(5mm)
  新しく`sub3`フォルダと`module3.py`を作り、四則演算とべき乗の関数を定義した。  
  `__init__.py`の`__all__ = ["module3"]`によって、公開するモジュールを指定した。  
  `ex12_4.py`からmodule3をインポートし、`multiply(5, 7)`を呼び出している。  
  5掛ける7の計算結果として35が表示された。
])
