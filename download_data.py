from huggingface_hub import snapshot_download

import os

# Xác định đường dẫn đến thư mục data trong dự án DIME
data_path = "./data/food101"

# Tạo thư mục nếu chưa có
if not os.path.exists(data_path):
    os.makedirs(data_path)

# Tải bộ dữ liệu
snapshot_download(
    repo_id="ethz/food101", 
    repo_type="dataset", 
    local_dir=data_path,
    local_dir_use_symlinks=False
)

print(f"Đã tải dữ liệu thành công vào: {data_path}")