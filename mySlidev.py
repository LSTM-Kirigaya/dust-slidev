import argparse
import os
import json
import shutil
import atexit
from colorama import Fore, Style, Back
from time import time
from typing import List, Dict
from html.parser import HTMLParser

import pandas as pd


INDEX_JSON = './index.json'
EXCLUDE_DIRS = ['components', 'node_modules', '.vscode', '.git']
PPT_SERVER_ROOT = 'ubuntu@101.43.239.71:/home/ubuntu/website/dust-slidev'



class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr_name, attr_value in attrs:
            if attr_name == 'href' or attr_name == 'src':
                _global_args['index_hrefs'].append(attr_value)

_global_args = {
    'args': None,
    'temps': [],        # 通过 dev 和 build 临时创建的文件
    'index_hrefs': []   # index.html中的所有的 href 的值
}

class MT:
    Error = 'error'
    Debug = 'debug'
    Info = 'info'

def color_report(message: str, mt: MT):
    flag = '[{}]'.format(mt)
    if mt == MT.Error:
        print(Fore.RED, flag, message, Style.RESET_ALL)

    
    if mt == MT.Debug:
        print(Fore.BLUE, flag, message, Style.RESET_ALL)


    if mt == MT.Info:
        print(Fore.GREEN, flag, message, Style.RESET_ALL)



def readJson(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as fp:
       obj = json.load(fp)
    return obj

def writeJson(path: str, obj: dict):
    with open(path, 'w', encoding='utf-8') as fp:
        json.dump(obj, fp, ensure_ascii=False, indent=4)

class ArgsType:
    build: bool
    dev: bool
    update: bool
    create: bool
    index_only: bool

    o: str
    i: str

def create_temp_files(args: ArgsType) -> bool:
    target_folder = args.i

    local_excludes = ['meta.json', os.path.basename(target_folder)]

    if not os.path.exists(target_folder):
        color_report("目标项目 " + target_folder + " 不存在", MT.Error)
        return False
    
    for file in os.listdir(target_folder):
        if file in local_excludes:
            continue
        file_path = os.path.join(target_folder, file)
        dst_path = file
        
        if os.path.isdir(file_path):
            shutil.copytree(file_path, dst_path)
        else:
            shutil.copy(file_path, dst_path)
        _global_args['temps'].append(file)
    
    return True

def build(args: ArgsType):
    if create_temp_files(args):
        name = os.path.basename(args.i)
        target_dist_path = os.path.join(args.i, name)
        os.system('slidev build -o ' + target_dist_path)
        
        index_path = os.path.join(target_dist_path, 'index.html')
        if not os.path.exists(index_path):
            color_report('index.html生成失败！', MT.Error)
            return

        # 加上 /ppt/name 的前缀
        prefix_url = '/ppt/' + name
        
        parser = MyHTMLParser()
        with open(index_path, 'r', encoding='utf-8') as fp: 
            html = fp.read()
            parser.feed(html)

        for href_value in _global_args['index_hrefs']:
            href_value: str
            if href_value.startswith('/assets'):
                adjust_href = prefix_url + href_value
                html = html.replace(href_value, adjust_href)
        
        with open(index_path, 'w', encoding='utf-8') as fp:
            fp.write(html)        

def dev(args: ArgsType):
    if create_temp_files(args):
        os.system('slidev')

def create(args: ArgsType):
    out_path = os.path.basename(args.o)
    if not os.path.exists(out_path):
        os.mkdir(out_path)
    meta = {
        'name': '',
        'path': out_path,
        'password': '',
        'cover': '',
        'create_ts': time(),
        'tags': []
    }

    meta_path = os.path.join(out_path, 'meta.json')
    writeJson(meta_path, meta)

    slidesMdPath = os.path.join(out_path, 'slides.md')
    if not os.path.exists(slidesMdPath):
        with open(slidesMdPath, 'w', encoding='utf-8') as fp:
            pass
    

def transform_dist_to_server(folder: str):
    target_dist = os.path.join(folder, folder)
    
    local_file_globs = os.path.join(folder, folder)
    scp_command = 'scp -r ' + local_file_globs + ' ' + PPT_SERVER_ROOT
    color_report(scp_command, MT.Info)
    os.system(scp_command)

def update(args: ArgsType):

    metas: List[Dict] = []
    dictorys: List[str] = []

    for dictory in os.listdir('.'):
        if os.path.isdir(dictory) and dictory not in EXCLUDE_DIRS:
            meta_path = os.path.join(dictory, 'meta.json')
            if not os.path.exists(meta_path):
                color_report( 'meta文件' + meta_path + '找不到，请检查项目是否损坏！', MT.Error)
                return
            meta = readJson(meta_path)
            
            if len(meta['name']) == 0:
                color_report(meta_path + '中的 name 属性为空，请补全！', MT.Error)
                return
            
            if 'create_ts' not in meta:
                color_report(meta_path + '中的 create_ts 属性缺失，请补全！', MT.Error)
                return   
            dictorys.append(dictory)
            metas.append(meta)

    # 最晚创建的放在最前面
    metas.sort(key=lambda m : m['create_ts'], reverse=True)
    index_meta = {
        'content': [],
        'index': {}
    }
    count = 0
    for meta in metas:
        meta.pop('create_ts')
        index_meta['content'].append(meta)
        index_meta['index'][meta['name']] = count
        count += 1
    
    writeJson(INDEX_JSON, index_meta)

    
    # 发送 index.json
    color_report('发送 index.json', MT.Info)
    os.system('scp index.json ' + PPT_SERVER_ROOT)

    if args.index_only:
        return

    # 根据 -t 参数选择性发送PPT文件
    if args.i:
        color_report('发送 {}'.format(args.i), MT.Info)
        transform_dist_to_server(args.i)
    else:
        for dictory in dictorys:
            color_report('发送 {}'.format(dictory), MT.Info)
            transform_dist_to_server(dictory)


@atexit.register
def clear_temp():
    pre_count = len(_global_args['temps'])
    if pre_count > 0:
        for file in _global_args['temps']:
            if os.path.exists(file):
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.remove(file)

        clear_flag = True
        for file in _global_args['temps']:
            if os.path.exists(file):
                clear_flag = False
                color_report('临时文件清理失败，请手动删除文件：{}'.format(file), MT.Error)
        
        if clear_flag:
            color_report('临时文件清理结束', MT.Info)







if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    commands = ['build', 'dev', 'create', 'update']

    parser.add_argument('-o', type=str, help='输出构建目录路径')
    parser.add_argument('-i', type=str, help='构建、运行或者同步服务器的项目名')

    parser.add_argument('--build', action='store_true')
    parser.add_argument('--dev', action='store_true')
    parser.add_argument('--create', action='store_true')
    parser.add_argument('--update', action='store_true')
    parser.add_argument('--index_only', action='store_true')

    
    args: ArgsType = parser.parse_args()
    _global_args['args'] = args

    for attr in dir(args):
        if attr.startswith('_'):
            continue
        value = getattr(args, attr)
        if value and attr in commands:
            globals()[attr](args)