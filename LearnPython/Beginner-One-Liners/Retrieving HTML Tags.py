import re


page = '''
<!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="Https://app.finxter.com/">test your Python skills</a>
<a href="Https://blog.finxter.com/recursion">Learn recursion</a>
<a href="Https://nostarch.com/">Great books from NoStarchPress</a>
<a href="Https://finxter.com/">Solve more Python puzzles</a>
</body>
</html>
'''

pattern = '"(.*?)">(.*?)<'

practice_tests = re.findall(pattern,page)

print(practice_tests)
for link,title in practice_tests:
    print(link,title)