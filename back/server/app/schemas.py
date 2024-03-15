from datetime import datetime
from pydantic import BaseModel, EmailStr, Json, constr
from typing import Optional, Union, List


class PostitSchema(BaseModel):
    id: Optional[int]
    x: Optional[int]
    y: Optional[int]
    user_id: Optional[str]
    name: Optional[str]
    mbti: Optional[str]
    hobby: Optional[List[str]]
    socialID: Optional[str]
    emogi: Optional[int]
    height: Optional[str]
    militaryService: Optional[bool]
    bodyType: Optional[str]
    eyelid: Optional[bool]
    fashion: Optional[List[str]]
    sex: Optional[str]


class PostitDeleteSchema(BaseModel):
    id: int


class EmailSchema(BaseModel):
    email: str

class ChatSchema(BaseModel):
    chat_id: int
    sender_id: str
    content: str
    created_at: Optional[datetime]


class ChatRoomSchema(BaseModel):
    room_id: int
    room_name: str
    chat_list: List[Optional[ChatSchema]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_contribute = True


class UserBaseSchema(BaseModel):
    name: Optional[str]
    email: str
    role: Optional[str]
    sex: Optional[str]
    password: str
    postit: Optional[PostitSchema]
    chatRoom: Optional[List[str]]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    send_like: Optional[List[Optional[str]]]
    recive_like: Optional[List[Optional[str]]]

    class Config:
        from_contribute = True


class PostitMakeSchema(BaseModel):
    postit: Optional[PostitSchema]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_contribute = True


class PostitMoveSchema(BaseModel):
    user_id: str
    x: float
    y: float


class PostitRemoveSchema(BaseModel):
    user_id: str


class PostitListSchema(BaseModel):
    status: str
    postits: List[Optional[PostitSchema]]


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    hobby: Optional[List[str]]
    fashion: Optional[List[str]]
    mbti: Optional[str]
    socialID: Optional[str]
    emogi: Optional[int]
    height: Optional[str]
    militaryService: Optional[bool]
    bodyType: Optional[str]
    eyelid: Optional[bool]
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema
