#!/usr/bin/env python
# coding=utf-8

import os
import sys
import oss2
import time
from sys import argv

input_filename = argv[1]
target_dir = ""
if len(argv) > 2:
    target_dir = argv[2]

ALLOWED_FILE_MIMETYPE = {
    ".plist": "application/x-plist",
    ".ipa": "application/octet-stream",
    ".html": "text/html",
    ".png": "image/png",
    ".ver": "plain/text",
    ".ver2": "plain/text",
    ".apk": "application/vnd.android.package-archive",
    ".dmg": "application/x-apple-diskimage",
    ".exe": "application/octet-stream"
}

# oss config
access_key_id = os.getenv('OSS_ACCESS_KEY_ID', '<AccessKeyId>')
access_key_secret = os.getenv('OSS_ACCESS_KEY_SECRET', '<AccessKeySecret>')
bucket_name = os.getenv('OSS_BUCKET', '<Bucket>')
endpoint = os.getenv('OSS_ENDPOINT', '<访问域名>')

def listUpdatedInfo(bucket):
    for i, object_info in enumerate(oss2.ObjectIterator(bucket)):
        # if apk_file_key in object_info.key:
        print object_info.key, time.strftime('%Y-%m-%d %H:%M:%S',
                                             time.gmtime(object_info.last_modified)), "- %.1fM" % (
            object_info.size / 1024.0 / 1024)
        # if ver_file_key in object_info.key:
        #     print  object_info.key, time.strftime('%Y-%m-%d %H:%M:%S',
        #                                           time.gmtime(object_info.last_modified)), "- %sbyte" % (
        #         object_info.size)

def upload_files_in(target, dir): 
    remote_target_dir = target

    if len(remote_target_dir) == 0:
        remote_target_dir = dir

    for file in os.listdir(dir):
        name, ext = os.path.splitext(file)
        
        if ALLOWED_FILE_MIMETYPE.has_key(ext):
            mime_type = ALLOWED_FILE_MIMETYPE.get(ext, "")

            upload_file(remote_target_dir, dir + file)


def upload_file(target, file):
    remote_target_dir = target
    base_file_name = os.path.basename(file) 
    if len(remote_target_dir) == 0:
        remote_target_dir = os.path.dirname(file) + "/"
    
    if remote_target_dir == "./":
        remote_target_dir = ""

    mime_type = ALLOWED_FILE_MIMETYPE.get(os.path.splitext(file)[1])

    with open(file, 'rb') as f:
        result = bucket.put_object(remote_target_dir + base_file_name, f, headers={'Content-Type': mime_type})

    print remote_target_dir + base_file_name, mime_type, "uploaded!"

if __name__ == '__main__':
    print  "oss sdk version:", oss2.__version__
    # 创建Bucket对象，所有Object相关的接口都可以通过Bucket对象来进行
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

    if len(target_dir) > 0 and not target_dir.endswith("/"):
        target_dir += "/"

    name, ext = os.path.splitext(input_filename)

    print name, ext
    if len(ext) == 0:
        if (not name.endswith("/")):
            name += "/"
        upload_files_in(target_dir, name)
    else:
        if ALLOWED_FILE_MIMETYPE.has_key(ext):
            upload_file(target_dir, input_filename)
