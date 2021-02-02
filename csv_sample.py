# CSV 데이터 처리 유틸기능 클래스

import pandas as pd
import os

class SweepPoint:

    df_all_data = None

    def __init__(self, ):
        return

    def openFile_csv(self, str_file_path):
        # 경로 예제 --> GUI에서 open dialog 사용해서 호출 해야 함.
        base_dir = 'D:/00_WORK/00_github/rsViewer/01_data/'
        csv_file = '2021-01-13.csv'  # 'sales_per_region.xlsx'
        csv_dir = os.path.join(base_dir, csv_file)

        # Input : Excel 파일 (의류정보고시) ======================
        idx_col = '품번'  # ini 파일입력 되도록 수정해야 함. (ini 파일은 변경이 예상되는 것들을 별도 입력 가능하도록 한 것임.

        self.df_all_data = pd.read_csv(csv_dir, names=['Freq.', 'Val.'], skiprows=[0])
        print(self.df_all_data)

    def cal_average(self):
        df = self.df_all_data
        print(df['Val.'].mean())

    def get_average(self):
        return self.df_all_data['Val.'].mean()

if __name__ == '__main__':
    # 판다스 Dataframe 많은 데이터 출력하기
    #pd.set_option('display.max_row', 500)
    #pd.set_option('display.max_columns', 100)

    # Input : 품번 =======================================
    sp = SweepPoint()
    sp.openFile_csv('test_path')
    sp.cal_average()
