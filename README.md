# aliyun-oss-scripts

## Prerequisites
- Python 2.x
- pip install oss2

## Setup Environment Variables
```
export OSS_ACCESS_KEY_ID=<Your Aliyun OSS access key>
export OSS_ACCESS_KEY_SECRET=<Your Aliyun OSS access secret>
export OSS_BUCKET=<Your Aliyun OSS bucket>
export OSS_ENDPOINT=<Your Aliyun OSS endpoint>
```

## Usage
### list
```
python oss-list.py
# or
python oss-list.py <folder_name>/
```

### upload
```
python oss-uploader.py ./<file_name>
# or
python oss-uploader.py <dir_name>
```

### delete
```
python oss-remove.py
# then input file/dir names one by one, each stand the whole line, 
# for example:
# foo.txt
# bar.pdf 

# to terminate either enter a empty name, or [ctrl-c]
```

