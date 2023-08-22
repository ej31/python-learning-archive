import pandas as pd
import random


# mockup DataFrame을 생성하는 함수
def create_mockup_dataframe(rows, columns):
    # 샘플 열 이름의 리스트 생성
    column_names = [f'Column_{i}' for i in range(columns)]

    # 열 이름과 무작위 값으로 구성된 딕셔너리 생성
    data = {col: [random.randint(1, 100) for _ in range(rows)] for col in column_names}

    # 딕셔너리를 사용하여 DataFrame 생성
    df = pd.DataFrame(data)

    return df


# DataFrame을 JSON 파일로 저장하는 함수
def save_to_json(df, file_name):
    # DataFrame을 JSON 파일로 저장
    df.to_json(file_name)
    print(f'{file_name} 파일이 성공적으로 저장되었습니다.')


# JSON 파일에서 DataFrame을 불러오는 함수
def load_from_json(file_name):
    # JSON 파일에서 DataFrame 읽기
    df = pd.read_json(file_name)
    print(f'{file_name} 파일이 성공적으로 불러와졌습니다.')
    return df

if __name__ == '__main__':
    # 예제 사용법
    rows = 10
    columns = 5
    mockup_df = create_mockup_dataframe(rows, columns)

    # DataFrame을 JSON 파일로 저장
    file_name_1 = 'mockup_data_1.json'
    file_name_2 = 'mockup_data_2.json'
    save_to_json(mockup_df, file_name_1)
    save_to_json(mockup_df, file_name_2)

    # JSON 파일에서 DataFrame 불러오기
    loaded_df = load_from_json(file_name_1)

    # 불러온 DataFrame 출력
    print(loaded_df)
    print(loaded_df.sort_values("Column_0"))