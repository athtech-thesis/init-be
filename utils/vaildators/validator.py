from errors.authorization_errors.authorization_error import MissingData, FormattingError


def is_valid_json(request):
    try:
        request.get_json()
        return True
    except ValueError as e:
        print(ValueError)
        raise FormattingError


def validate_json_request(json_request, *fields_to_validate):
    for field in fields_to_validate:
        if field not in json_request:
            raise MissingData
