from fastapi import APIRouter, Path, Query, Depends, Form
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator, ValidationError
from fastapi.exceptions import RequestValidationError
from typing import Annotated

router = APIRouter()

# ====================================================================================
# [Pydantic V2 공식 문서 기반 프로젝트 공통 표준]
# 1. 제약조건(Metadata): 무조건 Annotated 내부에 Field(...)로 정의한다.
# 2. 기본값(Default): 무조건 우측 = 연산자로 할당한다 (정적 타입 체커 지원 목적).
# 3. Optional(선택값): 파이썬 3.10+ 문법인 `T | None` 을 사용하며, 반드시 `= None` 을 할당해야 선택값으로 동작한다.
# ====================================================================================

# 1. 기본 모델 및 포함(Nested) 모델 정의
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# 2. 메인 Pydantic 모델 정의
class UserRegisterModel(BaseModel):
    # [Case 1] 필수값 + 제약조건 없음 (특수 타입 포함)
    email: EmailStr
    password_confirm: str
    
    # [Case 2] 필수값 + 제약조건 있음 (Annotated 패턴 사용)
    username: Annotated[str, Field(min_length=2, max_length=20, description="사용자명")]
    password: Annotated[str, Field(min_length=8, max_length=20, pattern=r".*[!@#$%^&*(),.?\":{}|<>].*", description="비밀번호(특수문자 포함)")]
    
    # [Case 3] 선택값 + 제약조건 없음 (| None 과 = None 조합)
    address: Address | None = None

    # [Case 4] 선택값 + 제약조건 있음 (제약조건은 Annotated 안, 기본값은 밖으로 빼기)
    # [Strict Mode 예시] Pydantic은 "29"(강제 형변환)를 자동으로 29로 변환하지만, Field(strict=True) 설정 시 오직 해당 타입만 엄격하게 검증합니다.
    # (주의: Form 데이터의 경우 HTTP 특성상 모든 값이 문자로 들어오므로 strict=True 적용 시 에러가 발생하기 쉽습니다. 주로 JSON Body 검증에 쓰입니다.)
    age: Annotated[int | None, Field(gt=0, lt=150, strict=True, description="나이")] = None
    
    # [Case 5] 기본값이 존재하는 명시적 타입 (선택값과 동일 원리)
    country: Annotated[str | None, Field(description="국가")] = "Korea"

    @field_validator("username")
    def validate_username(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Username must not be empty or whitespace only")
        return v

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isalpha() for char in v):
            raise ValueError("Password must contain at least one alphabetic character")
        return v

    @model_validator(mode="after")
    def validate_passwords_match(self):
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self

@router.post("/json/{user_id}")
async def register_user_json(
    user_id: Annotated[int, Path(title="User ID", ge=1)],
    user: UserRegisterModel,
    q: Annotated[str | None, Query(title="Query Parameter", max_length=50)] = None
):
    '''
    JSON Body로 데이터를 받아 Pydantic 모델로 유효성을 검사하는 API
    - URL Path Parameter: Path 유효성 검사 적용 (user_id)
    - Query Parameter: Query 유효성 검사 적용 (q)
    - Body: UserRegisterModel 적용 (EmailStr, Regex, Custom Validation 3가지, Nested Model 등 포함)
    '''
    
    # 3. Serialization(직렬화) / Deserialization(역직렬화) 예시
    # Pydantic Object -> Dict (직렬화)
    user_dict = user.model_dump()
    
    # Pydantic Object -> JSON 문자열 (직렬화)
    user_json_str = user.model_dump_json()
    
    # 역직렬화 테스트 (Dict -> Pydantic Object)
    recreated_user = UserRegisterModel.model_validate(user_dict)
    
    return {
        "message": "User registered successfully via JSON",
        "user_id": user_id,
        "query": q,
        "user_data_dump": user_dict, # 직렬화된 dict 객체 반환 
        "user_json_str": user_json_str
    }

def validate_form_data(
    email: Annotated[EmailStr, Form(description="이메일")],
    username: Annotated[str, Form(min_length=2, max_length=20, description="사용자명")],
    password: Annotated[str, Form(min_length=8, max_length=20, pattern=r".*[!@#$%^&*(),.?\":{}|<>].*", description="비밀번호")],
    password_confirm: Annotated[str, Form(description="비밀번호 확인")],
    age: Annotated[int | None, Form(gt=0, lt=150, description="나이")] = None,
    country: Annotated[str | None, Form(description="국가")] = "Korea"
):
    try:
        user = UserRegisterModel(
            email=email,
            username=username,
            password=password,
            password_confirm=password_confirm,
            age=age,
            country=country
        )
        return user
    except ValidationError as e:
        raise RequestValidationError(e.errors())

@router.post("/form")
async def register_user_form(
    user: Annotated[UserRegisterModel, Depends(validate_form_data)]
):
    '''
    form-data를 받아서 처리하는 API
    - FastAPI의 Depends를 사용하여 별도 함수(validate_form_data)에서 form-data 추출 후 Pydantic 모델과 매핑
    - 모델 변환/유효성 검사 실패 시 FastAPI의 RequestValidationError를 던지도록 처리 (Depends 방식)
    '''
    return {
        "message": "User registered successfully via Form-Data",
        "user_data": user
    }
