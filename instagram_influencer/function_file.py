import os
import pandas as pd

def read_file(*relative_parts):

    relative_path = os.path.join(*relative_parts)
    abs_path = os.path.abspath(relative_path)
    ext = os.path.splitext(abs_path)[1].lower()
    ext = ext.lstrip('.') 

    if  ext == 'xlsx':
        try:
            df = pd.read_excel(abs_path)
            # print("엑셀 파일이 성공적으로 읽혔습니다.")
            return df
        except Exception as e:
            print(f"에러원인 : {e}")
            return None
