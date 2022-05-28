import os
html_template = open('template.html', 'r',encoding="utf-8").read()

# 将文件夹内所有文件的文件名与下载链接放在列表里拼合到html_template里
# 输入样例 {'filename':'filepath'}
def gen_html(output_path, title, file_list,save_path):
    content=''
    for filename, filepath in file_list.items():
        content += '<a href="{0}" download="{1}">{1}</a><br/>\n\t\t'.format(filepath,filename)
    html_str = html_template.format(title=title, content=content)
    with open(os.path.join(output_path, save_path), 'w',encoding="utf-8") as f:
        f.write(html_str)

def file_list_gen(path):
    file_list = {}
    for filename in os.listdir(path):
        file_list[filename] = os.path.join(path, filename).replace('\\', '/')
    return file_list

if __name__ == '__main__':
    file_list = file_list_gen('./download')
    gen_html('.', 'GFSS-PAPER', file_list, 'index.html')