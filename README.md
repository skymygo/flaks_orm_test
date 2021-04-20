# flaks_orm_test


필요 모듈

    pymysql
    sqlalchemy
    flask

실행법

    api_info.json과 db_info.json에 적절한 값을 입력한 후 api.py를 실행한다.

사용법

    1. 회사명 자동완성 (/search/company/name/<company>)
        검색하고자 하는 회사명을 입력한다.
        ex) ak를 검색하려면 /search/company/name/ak 를 입력한다

    2. 태그명으로 회사 검색(/search/company/tag/<tag>)
        검색하고자 하는 태그를 입력한다
        ex) tag_3를 검색하려면 /search/company/tag/tag_3 을 입력한다.

    3. 회사 태그 정보 추가 (/tag Method: Post)
        추가하려는 회사의 태그 정보를 입력한다. 태그 정보에는 언어 코드를 포함한다 (1=KOR, 2=ENG, 3=JAP ...)
        ex) ak회사에 tag_4를 추가하려면 /tag 위치로 { "company_name": "ak", "language_code": 1, "tag": "tag_4"}를 전송한다. (tag_add_test.py 참조)

    4. 회사 태그 정보 삭제 ( /tag/<company>/<tag> Method: Delete)
        삭제하려는 회사의 태그정보를 입력한다.
        ex) ak회사의 tag_4를 삭제하려면 /tag/ak/tag_4 를 Delete Method로 전달한다.

