import os,time
html_template = open('template.html', 'r',encoding="utf-8").read()

# 将文件夹内所有文件的文件名与下载链接放在列表里拼合到html_template里
# 输入样例 [['name','path'],['name','path']]
def gen_html(output_path, title, file_list, save_path):
    content=''
    print(file_list)
    for file in file_list:
        content += '<a href={href} download={href}>{filename}</a><br/>\n\t\t\t'.format(href=file[1], filename=file[0])
    html_str = html_template.format(title=title, content=content,time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    html_str += "\n<!-- Gen by GFSS. -->"
    with open(os.path.join(output_path, save_path), 'w',encoding="utf-8") as f:
        f.write(html_str)
#RETURN ['name','path'],['name','path']]
def file_list_gen(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append([file, os.path.join(root, file).replace('\\', '/')])
    #将 file_list按照文件名从长到短排序
    file_list.sort(key=lambda x: len(x[0]))
    return file_list

if __name__ == '__main__':
    file_list = file_list_gen('./download')
    gen_html('.', 'GFSS-PAPER', file_list, 'index.html')