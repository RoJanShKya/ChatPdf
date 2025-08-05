def http_status(status):
    match status:
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case _:
            return "UNKOWN STATUS"
print (http_status(406))