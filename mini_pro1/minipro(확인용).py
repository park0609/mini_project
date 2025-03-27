#QT디자이너로 만든 UI와 연결시키는 기본 코드

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui, uic

# Oracle 모듈
import cx_Oracle as oci

## DB연결 설정
sid = 'XE'
host = 'localhost'
port = 1521
username = 'madang'
password = 'madang'
basic_msg = '학생정보 v 1.0'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        uic.loadUi('./toyproject/Studentdb.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

#========================================================================
# 이미지 추가 샘플
self.setWindowIcon(QIcon('./image/students.png')) #왼쪽 상단 아이콘 삽입
self."버튼명".setIcon(QIcon('이미지주소')) # 버튼 별 이미지 삽입
self."테이블 명".doubleClicked.connect(self.tblstudentDoubleClick) # 안에는 self와 함수명을 넣어 기능 부여

#========================================================================

# 버튼 수정 샘플
    def btn_mod_click(self):
        "입력컬럼1" = self.input_std_id.text()
        "입력컬럼2" = self.input_std_name.text()
        "입력컬럼3" = self.input_std_mobile.text()
        "입력컬럼4" = self.input_std_regyear.text()
        #...
        #print(std_id, std_name,std_mobile,std_regyear)

        if "입력컬럼1" == '' or "입력컬럼2" == '' or "입력컬럼3" == '' or "입력컬럼4" == '': #...
            QMessageBox.about(self,'경고','학생이름 또는 입학년도는 필수입니다!')
            return 
        else:
            print('DB수정진행')    
            values = (std_name,std_mobile,std_regyear,std_id) # 컬럼명 변경 
            if self.modData(values) == True: #옆 함수 아래로 연결
                QMessageBox.about(self,'수정성공','학생정보 수정완료!')
            else:
                QMessageBox.about(self,'수정실패','관리자에게 문의해주세요!')

            self.loadData() 
            self.clearInput()

            self.statusbar.showMessage(f'{basic_msg} | 수정완료')

    # 연결된 함수
    def modData(self, tuples):
        isSuccede = False 
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()
        try:
            conn.begin() 
            query = '''
                    쿼리는 간단하게 삭제 쿼리 작성
                    '''
            cursor.execute(query, tuples)
            conn.commit() 
            isSuccede = True 
        except Exception as e:
            print(e)
            conn.rollback() 
            isSuccede = False
        finally:
            cursor.close()
            conn.close()
        return isSuccede 
# 변경되는 사항이 없어 이대로 복사 붙여넣기후 함수명 올바르게 변경 후 디버깅진행

#===============================================================================================

#삭제버튼 클릭 시그널처리 함수
# 코드 사용할 땐 올바른 변수명과 함수명 이용 붙여넣고 확인

    def btn_del_click(self): # 함수명 변경
        std_id = self.input_std_id.text() 
        
        # std_id에 입력값이 없을 때 경고창 띄우기
        if std_id == '':
            QMessageBox.warning(self,'경고','학생이름 또는 입학년도는 필수입니다!')
            return 
        #입력값이 존재한다면 ID값을 통한 데이터 삭제
        else:
            print('DB삭제진행')
            # Oracle은 파라미터 타입에 민감. 정확한 타입을 사용해야함
            values = (int(std_id),)
            if self.delData(values) == True:# 함수명 맞춰야함
                QMessageBox.about(self,'삭제성공','학생정보 삭제완료!')
            else:
                QMessageBox.about(self,'삭제실패','관리자에게 문의해주세요!')

            self.loadData() 
            self.clearInput()

            self.statusbar.showMessage(f'{basic_msg} | 삭제완료')

    #D(DELETE)
    def delData(self, tuples): # 함수명 맞추기
        isSuccede = False 
        conn = oci.connect(f'{username}/{password}@{host}:{port}/{sid}')
        cursor = conn.cursor()
        try:
            conn.begin() 
            query = '''
                    맞는 쿼리 작성
                    '''
            cursor.execute(query, tuples)
            conn.commit() 
            isSuccede = True 
        except Exception as e:
            print(e)
            conn.rollback() 
            isSuccede = False
        finally:
            cursor.close()
            conn.close()
        return isSuccede
# 수정과 동일 변하는 값 없기에 이대로 함수명 올바르게 변경 후 복사 붙여넣고 디버깅 진행
#=====================================================================================================

    # 테이블위젯 데이터와 연관해서 화면 설정
    # 함수명 변경 및 컬럼명 변경 
    def makeTable(self, lst_student):
        self.tblstudent.setSelectionMode(QAbstractItemView.SingleSelection) # 단일 row선택모드
        self.tblstudent.setEditTriggers(QAbstractItemView.NoEditTriggers) #컬럼수 변경금지
        self.tblstudent.setColumnCount(4)
        self.tblstudent.setRowCount(len(lst_student))# 커서에 들어있는 데이터 길이만큼 row 생성
        self.tblstudent.setHorizontalHeaderLabels(['학생번호','학생이름','핸드폰','입학년도']) # 라벨 생성 은 맞춰서

        # 전달받은 cursor를 반복문으로 테이블 위젯에 뿌리는 작업
        for i, (std_id,std_name,std_mobile,std_regyear) in enumerate(lst_student):
            self.tblstudent.setItem(i, 0, QTableWidgetItem(str(std_id))) # oracle number타입은 뿌릴때 str()로 형변환 필요!
            self.tblstudent.setItem(i, 1, QTableWidgetItem(std_name))
            self.tblstudent.setItem(i, 2, QTableWidgetItem(std_mobile))
            self.tblstudent.setItem(i, 3, QTableWidgetItem(str(std_regyear)))
            

#====================================================================================================
#창변환 함수
# 시그널 연결 후 