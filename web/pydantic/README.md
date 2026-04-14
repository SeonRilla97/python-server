# Pydantic

데이터 검증 라이브러리

1. Schema / 데이터 유효성 검사
2. 정규식, 내장 검증로직( Email 등) 지원
3. Serialization / Deserialization (JSON / Dict 변환)
4. FastAPI , LangChain 데이터 구조 정의에서 다 사용함

---

모든곳에서 다 써야하는가?

Client의 입력데이터는 검증이 필요하지만 DB의 데이터는 이미 검증된 데이터가 저장된다.
따라서 Pydantic은 입력검증만, 비즈니스 로직 검증은 Service Layer에서 처리한다.

Client <-> FastAPI : Pydantic
FastAPI <-> DB : dataclass

다음을 구현

post 요청으로 request의 router.py를 참고해서 동일하게 main.py에 선언하여 swagger에 나타 낼것

1. URL Path Variable 에 Pydantic 적용 Path 임포트
2. Query Parameter 에 Pydantic 적용 Query 임포트
3. Body 에 Pydantic 적용
   - Email : emailStr 사용
   - Username : 최소/최대글자 (필수 입력)
   - password : 최소/최대글자 + 정규식(특수문자 포함)
   - password_confirm : password와 일치 (Custom Validation - After 이용)
   - age (선택)
   - country (선택/ default : Korea)

   - custom validation 에서 3가지의 유효성 검사 모두 구현 (Annotated 사용 & default=None(이는 예시일뿐) 까지 함께 이용)

post 요청으로 form-data를 받아서 처리하는 API를 구현

1. pydantic Validation을 적용하되, 별도 함수를 빼서 여기서 Model을 변환하고, 실패 시 VAlidation 및 RequestValidationError로 에러 내도록 변경 (Depends) - FastAPI에서 제공하는 Depends를 사용해서 구현함을 명시
