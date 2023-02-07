@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user_profile = get_user_info()

    return full_user_profile


@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: int):

    full_user_profile = get_user_info(user_id)

    return full_user_profile


@app.post("/users", response_model=CreateUserResponse)
def add_user(full_profile_info: FullUserProfile):
    user_id = create_user(full_profile_info)
    created_user = CreateUserResponse(user_id=user_id)
    return created_user