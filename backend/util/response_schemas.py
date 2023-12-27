base_responses = {
    400: {"content": {"application/json": {"example": {"detail": "Bad Request"}}}},
    401: {"content": {"application/json": {"example": {"detail": "Unauthorized"}}}},
    404: {"content": {"application/json": {"example": {"detail": "Not Found"}}}},
    422: {"content": {"application/json": {"example": {"detail": "Validation Error"}}}},
    500: {"content": {"application/json": {"example": {"detail": "Internal Server Error"}}}},
    # 400: {"description": "Bad Request"},
    # 401: {"description": "Unauthorized"},
    # 404: {"description": "Not Found"},
    # 422: {"description": "Validation Error"},
    # 500: {"description": "Internal Server Error"}
}

get_token_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {"access_token": "string",
                            "token_type": "string"}
            }
        },
    }
}

login_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {
                    "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjMiLCJpc3QiOjE3MDI4MDQwNDIsImV4cCI6MTcwMjgzMTA0Mn0.VpqvSNT5vKjbH_P43PogXU2r1vKIc2y0NQ3oAaRwZv7DYLgtQ9JoeK0Rfd8rNQOnMay1a10GlA7jyYq3LdAf0oyJAe8fvD4HfVLPj_0DiG2lsjJnsAC8-0S4JL0W25JT3-38Opft5xz5njO_3ETYbg991HFxrO2UD1yoSrDWJ8TC-zEAog835KzoXNNbsN_Tl8wZsK_jMhLv-C-q7fPy8qdRMnLQGP0p8OcsYNOXUCO98S_WiPaMXV54MbtqBu4IsToNC4VpFpFtQjdFmA_lQM4rK27bQN6jg1p4LUcUK1M6cSAeeE6J2Uhbf8n8chAQtiQZJ4_slv6VZF8V4S7vLg",
                    "token_type": "Bearer",
                    "phone_number": "123"
                }
            }
        },
    }
}

user_response = {
    **base_responses,
    200: {
        "content": {

            "application/json": {

                "example": {
                    "password": "$5$rounds=535000$b.dunRJUEr8TInFo$W6YDX/Uxk9vL2l5PJDwMg7ju.djaB.OyHLys5daMiSC",
                    "authorization": 1,
                    "id": "2bcf7ef7-dc5b-4585-b08a-4b059d82c749",
                    "phone_number": "123"
                },

                # "schema": {
                #     "User": {
                #         "title": "User",
                #         "type": "object",
                #         "properties": {
                #             "id": {
                #                 "title": "Id",
                #                 "type": "string",
                #                 "format": "uuid"
                #             },
                #             "phone_number": {
                #                 "title": "Phone Number",
                #                 "type": "string"
                #             },
                #             "password": {
                #                 "title": "Password",
                #                 "type": "string"
                #             },
                #             "authorization": {
                #                 "title": "Authorization",
                #                 "type": "integer",
                #                 "format": "int32"
                #             }
                #         }
                #     }
                # }
            }
        },
    }
}

user_create_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {
                    "message": "User Created"
                }
            }
        },
    }
}

user_password_update_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {
                    "message": "User Password Updated"
                }
            }
        },
    }
}

user_update_response = {}
user_delete_response = {}
all_user_response = {}
user_profile_response = {}
user_profile_update_response = {}
user_profile_create_response = {}
user_card_response = {}
user_card_update_response = {}
user_card_create_response = {}
user_card_delete_response = {}

hotel_create_response = {}
hotel_update_response = {}
hotel_delete_response = {}
hotel_get_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {
                    "hotel": {
                        "name": "string",
                        "id": "676ea61e-47c5-479f-bc56-00daddcd66fa",
                        "description": "string",
                        "city": "string",
                        "zip_code": "string",
                        "phone_number": "string",
                        "address": "string",
                        "state": "string"}
                }
            }
        },
    }

}
hotel_all_response = {
    **base_responses,
    200: {
        "content": {
            "application/json": {
                "example": {
                    "hotel": [
                        {
                            "id": "676ea61e-47c5-479f-bc56-00daddcd66fa",
                            "name": "string",
                            "description": "string",
                            "city": "string",
                            "zip_code": "string",
                            "phone_number": "string",
                            "address": "string",
                            "state": "string"
                        },
                        {
                            "id": "e92d615c-82a0-4662-8a18-843dcb4f2eae",
                            "name": "string",
                            "description": "string",
                            "city": "string",
                            "zip_code": "string",
                            "phone_number": "string",
                            "address": "string",
                            "state": "string"
                        },
                        {
                            "id": "eda1f403-7c1d-4d20-b8dc-8a898801fde8",
                            "name": "string",
                            "description": "string",
                            "city": "string",
                            "zip_code": "string",
                            "phone_number": "string",
                            "address": "string",
                            "state": "string"
                        }
                    ]
                }
            }
        },
    }

}
hotel_service_create_response = {}
hotel_service_update_response = {}
hotel_service_delete_response = {}
hotel_service_get_response = {}
hotel_service_all_response = {}

hotel_booking_create_response = {}
hotel_booking_update_response = {}
hotel_booking_delete_response = {}
hotel_booking_get_response = {}
hotel_booking_all_response = {}

user_hotel_rating_create_response = {}
user_hotel_rating_update_response = {}
user_hotel_rating_delete_response = {}
user_hotel_rating_get_response = {}
user_hotel_rating_all_response = {}

