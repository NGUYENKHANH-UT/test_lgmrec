import pandas as pd
import os

DATA_DIR = './data/clothing/'
INPUT_TXT = os.path.join(DATA_DIR, 'clothing.txt')
OUTPUT_INTER = os.path.join(DATA_DIR, 'clothing.inter')

def convert_dragon_to_lgmrec():
    print(f"--- Đang đọc dữ liệu từ: {INPUT_TXT} ---")
    if not os.path.exists(INPUT_TXT):
        print(f"Lỗi: Không tìm thấy file {INPUT_TXT}")
        return

    df = pd.read_csv(INPUT_TXT, sep='\t')

    if 'timestamp' not in df.columns:
        df['timestamp'] = 0.0
    else:
        df['timestamp'] = df['timestamp'].astype(float)

    df.rename(columns={
        'user_id': 'user_id:token',
        'item_id': 'item_id:token',
        'timestamp': 'timestamp:float',
    }, inplace=True)

    cols_to_keep = ['user_id:token', 'item_id:token', 'timestamp:float', 'x_label']
    df_final = df[cols_to_keep]

    df_final.to_csv(OUTPUT_INTER, sep='\t', index=False)
    print(f"✓ Đã chuyển đổi thành công! File lưu tại: {OUTPUT_INTER}")
    print(f"Mẫu dữ liệu:\n{df_final.head(3)}")

if __name__ == '__main__':
    convert_dragon_to_lgmrec()