import re

text = "abc123def456"
# rはraw文字列を示すプレフィックスで、バックスラッシュをエスケープせずに使用できるようにします。
# \dは数字を表す
# +は1回以上の繰り返しを意味します。
# \d+は数字が1文字以上続く

result = re.findall(r'\d+', text)
print(result) 

# Output: ['123', '456']
# https://regexr.com/ 正規表現を確認するサイト