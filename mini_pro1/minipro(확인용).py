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
 #세션 연결 함수 인데 진ㅉ ㅏ안됨 개어려움 죽을맛임 진짜
 def create_session(username, role):
    
    #로그인 성공 시, 랜덤한 세션 ID를 생성하여 데이터베이스에 저장한다.
    
        session_id = str(uuid.uuid4())  # 랜덤한 세션 ID 생성
        conn = cx_Oracle.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
        cursor = conn.cursor()
    
        query = '''
        INSERT INTO sessions (session_id, username, role) VALUES (:1, :2, :3)
        '''
        cursor.execute(query, (session_id, username, role))
        conn.commit()
    
        return session_id

    def get_session(session_id):
    
        conn = cx_Oracle.connect(f'{username_m}/{password_m}@{host_m}:{port_m}/{sid_m}')
        cursor = conn.cursor()

        query = '''SELECT username, role FROM sessions WHERE session_id=:1'''
        cursor.execute(query, (session_id,))
        return cursor.fetchone()  # 세션 정보 반환

#====================================================================================================
class InventoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # 메인 위젯 설정
        self.setWindowTitle("재고 관리 프로그램")
        self.setGeometry(100, 100, 600, 400)

        # 메인 레이아웃
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # 제품 목록 테이블
        self.product_table = QTableWidget()
        self.product_table.setRowCount(3)  # 예시용 3개의 제품
        self.product_table.setColumnCount(2)  # 제품명과 이미지 경로
        self.product_table.setHorizontalHeaderLabels(["제품명", "이미지 경로"])
        layout.addWidget(self.product_table)

        # 테이블에 데이터 추가
        self.product_table.setItem(0, 0, QTableWidgetItem("제품 A"))
        self.product_table.setItem(0, 1, QTableWidgetItem("./images/product_a.png"))
        self.product_table.setItem(1, 0, QTableWidgetItem("제품 B"))
        self.product_table.setItem(1, 1, QTableWidgetItem("./images/product_b.png"))
        self.product_table.setItem(2, 0, QTableWidgetItem("제품 C"))
        self.product_table.setItem(2, 1, QTableWidgetItem("./images/product_c.png"))

        # QLabel: 제품 이미지 표시
        self.image_label = QLabel("이미지가 여기에 표시됩니다.")
        self.image_label.setFixedSize(300, 300)
        self.image_label.setStyleSheet("border: 1px solid black;")  # 테두리 추가
        self.image_label.setScaledContents(True)  # 이미지 크기를 QLabel 크기에 맞춤
        layout.addWidget(self.image_label)

        # 테이블에서 행을 선택했을 때 이벤트 연결
        self.product_table.cellClicked.connect(self.update_image)

    def update_image(self, row, column):
        # 선택된 행(row)의 이미지 경로 가져오기
        image_path = self.product_table.item(row, 1).text()

        # QLabel에 이미지 표시
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("이미지를 로드할 수 없습니다.")

            import sys
from PyQt5.QtWidgets import QApplication, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QMainWindow, QWidget
from PyQt5.QtGui import QPixmap
