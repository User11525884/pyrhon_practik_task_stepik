from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html ").read().decode('utf-8')
s = str(html)
split_code = s.split('<code>')
ans = []
for i in split_code:
    if '</code>' in i:
        ans.append(i.split('</code>')[0])
    else:
        continue
lib = {}
for i in ans:
    if i not in lib:
        lib[i] = 1
    else:
        lib[i] += 1
# for i, k in lib.items():
#  print(i, k)
sorted_lib = sorted(lib.items(), key=lambda x: x[1], reverse=True)
converted_dict = dict(sorted_lib[:3])
print(' '.join(converted_dict))
