#!/usr/bin/env python
# coding=utf-8

import os
import sys
import oss2
import time
from sys import argv

prefix = '' if len(argv) < 2 else argv[1]
delimiter = '/' if len(argv) < 3 else argv[2]

# oss config
access_key_id = os.getenv('OSS_ACCESS_KEY_ID', '<AccessKeyId>')
access_key_secret = os.getenv('OSS_ACCESS_KEY_SECRET', '<AccessKeySecret>')
bucket_name = os.getenv('OSS_BUCKET', '<Bucket>')
endpoint = os.getenv('OSS_ENDPOINT', '<访问域名>')

def listUpdatedInfo(bucket):
    for i, object_info in enumerate(oss2.ObjectIterator(bucket, prefix=prefix, delimiter=delimiter)):
        # if apk_file_key in object_info.key:       
              
        print object_info.key, time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(object_info.last_modified)), "--" if not object_info.size else "- %.1fM" % (object_info.size / 1024 / 1024)
        # if ver_file_key in object_info.key:
        #     print  object_info.key, time.strftime('%Y-%m-%d %H:%M:%S',
        #                                           time.gmtime(object_info.last_modified)), "- %sbyte" % (
        #         object_info.size)


if __name__ == '__main__':
    print("oss sdk version:", oss2.__version__)
    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    
    listUpdatedInfo(bucket)