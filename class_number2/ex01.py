import sys

def separator():
    print("SEPARATOR :")
    print(" ")
    print('P', 'Y', 'T', 'H', 'O', 'N')
    print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
    print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')
    print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
    print('P', 'Y', 'T', 'H', 'O', 'N', sep='     ')
    print('010', '7777', '1234', sep='-')
    print('python', 'google.com', sep='@')
    print(" ")

def end():
    # end
    print("END :")
    print(" ")
    print('welcom to', end='')
    print('IT News', end='')
    print('Web Site')
    print('welcom to', end=' ')
    print('IT News', end=' ')
    print('Web Site')
    print(" ")

def file_option():
    print("FILE OPTION :")
    print(" ")
    print('learn python', file=sys.stdout) # sysっていうのは、pythonの標準ライブラリの一つで、システムに関する情報や機能を提供するモジュールです。sys.stdoutは、標準出力を指すファイルオブジェクトで、print関数の出力先として使用されます。つまり、このコードは「learn python」という文字列を標準出力に表示することを意味しています。
    print()

def main():
    separator()
    end()
    file_option()

if __name__ == "__main__":
    main()