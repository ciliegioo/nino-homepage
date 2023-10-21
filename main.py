import streamlit as st
from PIL import Image
import pandas as pd
import random
from streamlit_modal import Modal
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import folium


st.set_page_config(
    page_title='NINO_HOME',
    page_icon='✨'
)

sch_img = 'https://gangdong.dge.hs.kr/upload/schl/gangdongh/widg/M_visual.png'
club_img = Image.open('NULL 홍보지.jpg')
dog_img = Image.open('mini.jpg')
band_img = 'https://image.bugsm.co.kr/album/images/500/40790/4079061.jpg'
game_img = 'https://i.pinimg.com/564x/5a/26/ca/5a26ca4d4db8de541434ad1466d99af7.jpg'
schlogo_img = 'https://gangdong.dge.hs.kr/images/schl/web/gangdongh/sub/img0101_0401.png'
movie_img = 'https://i.pinimg.com/564x/03/9c/30/039c309ada7f4189559303944948cc71.jpg'
swim_img = 'https://i.pinimg.com/564x/4e/fc/f9/4efcf9ef0498d2eb4dc2364b36e56d27.jpg'
piano_img = 'https://i.pinimg.com/564x/6e/ff/a1/6effa154ab473877c1ae8c9d1be3c722.jpg'
m1graph = Image.open('등직운_그래프.png')
m2graph = Image.open('등가직운_그래프.png')
new1 = Image.open('갈릴레이사고실험.jpg')
new2_1 = Image.open('가속도힘그래프.jpg')
new2_2 = Image.open('가속도질량그래프.jpg')
ip = Image.open('충격운동.png')
sg = Image.open('초기화면.jpg')

with st.sidebar:
    menu = option_menu("Menu", ['About Me', 'About My School', 'About My Club', 'Mini Game', 'Digital Textbook'],
                       icons=['bi bi-emoji-sunglasses', 'bi bi-mortarboard',
                              'bi bi-geo', 'bi bi-dice-2', 'bi bi-book'],
                       menu_icon="app-indicator", default_index=0,
                       styles={
        "container": {"padding": "4!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "15px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#b6d7a8"},
        "nav-link-selected": {"background-color": "#6aa84f"},
    }
    )

################
# 자기소개
################
if menu == 'About Me':
    st.header('About Me')
    tab1, tab2 = st.tabs(['ABOUT', 'What I love'])

    with tab1:
        st.header('조은경(Cho Eunkyeong)')
        st.write('_🎂:grey[2006.04.04]_')
        st.write('_📧:grey[slowhale19@gmail.com]_')
        st.write('게임개발자가 꿈인 강동고 조은경입니다😊')

    with tab2:
        bar1, bar2, bar3 = st.columns([2, 2, 2])
        with bar1:
            st.image(dog_img)
            st.image(movie_img)
        with bar2:
            st.image(band_img)
            st.image(swim_img)
        with bar3:
            st.image(game_img)
            st.image(piano_img)

################
# 학교소개
################
elif menu == 'About My School':
    st.header('About My School')

    st.image(sch_img)
    st.subheader('대구강동고등학교')
    st.write('대구광역시 동구 금강로 65 :grey[(053)231-6320-6322]')

    bar1, bar2 = st.columns([3, 4])

    with bar1:
        st.image(schlogo_img)
    with bar2:
        st.write('교장 : 정희석')
        st.write('교훈 : 인의예지')
        st.write('교목 : 주목')
        st.write('교화 : 목련')

    m = folium.Map(location=[35.8655, 128.7294], zoom_start=30)
    folium.Marker(
        [35.8655, 128.7294], popup="Liberty Bell", tooltip="Liberty Bell"
    ).add_to(m)

    st_data = st_folium(m, width=725)

################
# 동아리소개
################
elif menu == 'About My Club':
    st.header('About My Club')

    bar1, bar2 = st.columns([2, 3])

    with bar1:
        st.image(club_img, caption='동아리 홍보지')

    with bar2:
        st.subheader('NULL')
        st.write(':blue[코딩 동아리 2021~]')
        st.write('부장 : 조은경')

        df = pd.DataFrame({
            '활동': ['컴퓨터 기초', 'Java 학습', '협업 프로젝트', '아두이노', '게임 제작'],
            '진행': ['완료', '완료', '진행 중', '진행 중', '예정']
        })
        st.dataframe(df)

################
# 관심분야 - 게임
################
elif menu == 'Mini Game':
    # 자동차 레이스
    st.subheader('Guess the winner')

    def race(car_choice):
        car = ['CAR-A', 'CAR-B']
        winner = random.choice(car)
        return winner

    car_choice = st.radio('어느 자동차가 레이싱에서 이길까요?', ['CAR-A', 'CAR-B'])
    st.image(sg, width=430)
    if st.button('Start Race'):
        winner = race(car_choice)

        if winner == 'CAR-A':
            st.write(
                "![CAR-A Win](https://media.giphy.com/media/aFWDAtSg629s55LvFD/giphy.gif)")
        else:
            st.write(
                "![CAR-B Win](https://media.giphy.com/media/aDhOb9AtoKXMhafJO4/giphy.gif)")

        if winner == car_choice:
            st.write(winner, 'win!')
            st.success('Win!')
        else:
            st.write(winner, 'win!')
            st.error('Fail')

################
# 디지털교과서
################
else:
    chap = st.sidebar.radio(
        'Chapter', options=['힘과 운동', '운동량과 충격량'])

    if chap == '힘과 운동':
        st.header('Digital Textbook')
        st.subheader('_힘과 운동_', divider='gray')

        st.write(
            '운동 : 물체의 위치가 시간에 따라 변하는 것  '
            '\n이동거리 : 물체가 이동한 경로의 길이 (크기有 방향×)')

        bar1, bar2 = st.columns([2, 2])
        with bar1:
            st.latex(r'''속력 = \frac{이동 거리}{걸린 시간} (단위:m/s)''')
            st.latex(r'''속도 = \frac{변위}{걸린 시간} (단위:m/s)''')
        with bar2:
            st.latex(r'''가속도 = \frac{나중 속도 - 처음 속도}{걸린 시간}''')
            st.latex(r'''= \frac{속도 변화량}{걸린 시간} (단위:m/s^2)''')

        with st.expander('등속 직선 운동'):
            st.write(
                '= 등속도 운동  \n 물체의 속도가 일정한 운동 (물체의 빠르기와 운동 방향 변하지×)  '
                '\n\nex:무빙워크, 에스컬레이터, 컨베이어 벨트 등')
            st.image(m1graph)
        with st.expander('등가속도 직선 운동'):
            st.write('물체의 가속도의 크기와 방향이 일정하게 변하는 운동')
            st.image(m2graph)
        with st.expander('등속 원운동'):
            st.write(
                '물체가 원 궤도를 따라 일정한 속력으로 회전하는 운동  '
                '\n물체의 속력 일정하고 운동 방향은 매 순간 원궤도에 접하는 접선 방향  '
                '\n\nex:회전 관람차, 회전 그네, 선풍기의 회전하는 날개 등')
        with st.expander('기타'):
            st.write(
                '속력과 운동 방향이 모두 변하는 운동  '
                '\n\nex:진자 운동, 수평으로 던진 물체의 운동, 포물선 운동 등')

        st.write('━━━━━━━━━━━━  \n')
        st.write(
            '힘 : 물체의 모양이나 운동 상태를 변화시키는 원인 [N]  '
            '\n알짜힘(합력) : 한 물체에 여러 힘이 작용할 때 물체에 작용한 모든 힘을 합한 것')
        st.caption('한 물체에 작용하는 합력이 0일 때, 이 힘들이 서로 평형을 이룬다고 하며, 물체는 힘의 평형 상태에 있다.')

        modal_n1 = Modal(key="newton1", title="뉴턴 운동 제 1법칙 (관성 법칙)")
        modal_n2 = Modal(key="newton2", title="뉴턴 운동 제 2법칙 (가속도 법칙)")
        modal_n3 = Modal(key="newton3", title="뉴턴 운동 제 3법칙 (작용 반작용 법칙)")
        open_modal_n1 = st.button('뉴턴 운동 제 1법칙 (관성 법칙)')  # 라이트 버전만 가능
        if open_modal_n1:
            with modal_n1.container():
                st.caption('관성 : 물체가 자신의 운동 상태를 계속 유지하려는 성질')
                st.write(
                    '물체에 작용하는 알짜힘이 0일 때, 정지해 있는 물체는 계속 정지해있고,  '
                    '\n운동하는 물체는 계속 등속 직선 운동을 한다.  '
                    '\n\nex : 달리던 버스가 갑자기 멈추면 승객들이 앞으로 넘어진다')
                st.image(new1)
        open_modal_n2 = st.button('뉴턴 운동 제 2법칙 (가속도 법칙)')
        if open_modal_n2:
            with modal_n2.container():
                st.write(
                    '가속도는 물체에 작용하는 알짜힘에 비례하고 질량에 반비례한다.  '
                    '\n가속도의 방향은 물체에 작용하는 알짜힘의 방향과 같다.  '
                    '\n\nex : 달리던 버스가 갑자기 멈추면 승객들이 앞으로 넘어진다')
                st.image(new2_1)
                st.image(new2_2)
        open_modal_n3 = st.button('뉴턴 운동 제 3법칙 (작용 반작용 법칙)')
        if open_modal_n3:
            with modal_n3.container():
                st.caption(
                    '힘은 두 물체 사으이 상호 작용으로 항상 쌍으로 작용하며,  '
                    '\n상호 작용하는 두 힘의 크기는 서로 같고, 방향은 반대이다.  '
                    '\n물체 A와 B가 상호작용할 때, A가 B에 작용하는 힘을 작용이라 하면,  '
                    '\nB가 A에 작용하는 힘은 반작용이라고 한다.')
                st.write(
                    '작용과 반작용은 항상 크기가 같도 방향은 반대이다  '
                    '\n\nex : 로켓이 가스를 분출하며 날아간다, 노를 저어 배가 나아간다 등')

    else:
        st.header('Digital Textbook')
        st.subheader('_운동량과 충격량_', divider='gray')

        st.write('운동량 : 물체의 운동하는 정도를 나타낸 물리량 [p]')
        st.write(
            '운동량 보존 법칙 : 물체가 충돌할 때 외부에서 힘이 작용하지 않으면  '
            '\n충돌 전과 충돌 후 물체들의 운동량의 합은 일정하게 보존된다.')
        st.latex(r'''p = mv (단위 : kg \cdot m/s)''')
        st.latex(
            r'''\Delta	 p = p - p_{0} = mv - mv_{0} (단위 : kg \cdot m/s)''')

        st.write('충격량 : 물체의 충돌할 때 물체가 받는 충격의 정도를 나타낸 물리량 [I]')
        st.latex(r'''I = F \Delta t = mv = mv_{0} (단위 : N \cdot s)''')

        st.write('━━━━━━━━━━━━  \n')
        with st.expander('충격량과 운동량의 관계'):
            st.image(ip)
            st.latex(
                r'''F = ma = m(\frac{v-v_{0}}{\Delta t}) = \frac{mv - mv_{0}}{\Delta t}''')
            st.latex(r'''F \Delta t = mv - mv_{0}''')
            st.latex(r'''I = \Delta p''')
        with st.expander('충격량과 힘의 관계'):
            st.latex(
                r'''F \Delta t \rightarrow F = \frac{I}{\Delta t} = \frac{\Delta p}{\Delta t}''')

            st.latex(r'''I \propto F (\Delta t : 일정)''')
        st.write('━━━━━━━━━━━━  \n')

        st.write('충격력 : 물체가 충돌할 때 받는 힘')
        st.latex(r'''F \propto \frac{1}{\Delta t} (I : 일정)''')
        st.write('충격력을 길게 하여 충격력을 감소시키는 예 : 자동차 범퍼, 번지저프 줄, 포수 글러브 등')
