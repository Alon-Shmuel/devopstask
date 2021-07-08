from flask import send_file


# get the list of files in the s3 bucket.
def get_files_list(bucket):
    files_list = []
    for s3_file in bucket.objects.all():
        files_list.append(s3_file.key)
    return files_list


# find if specific file is in the s3 bucket.
def find_file(bucket, obj):
    for file_path in get_files_list(bucket):
        file_name = file_path.split('/')[-1]
        if obj == file_name:
            bucket.download_file(file_path, file_name)
            #            return f"{file_name} downloaded"
            return send_file(file_name, as_attachment=True)
    return f"no luck finding {obj}"
